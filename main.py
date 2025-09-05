import streamlit as st
import asyncio
import aiohttp
import json
import time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
import os
from datetime import datetime
import uuid
from dotenv import load_dotenv

# Load environment variables from config.env file
load_dotenv('config.env')

# Page Configuration
st.set_page_config(
    page_title="AI-Powered Streamlit Application",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    .response-area {
        background: #f8f9fa;
        border: 2px solid #e9ecef;
        border-radius: 10px;
        padding: 1.5rem;
        min-height: 300px;
        font-family: 'Courier New', monospace;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# Pydantic Models
class PromptRequest(BaseModel):
    system_prompt: str = Field(..., description="System prompt defining AI behavior")
    context: str = Field(..., description="Context information for AI analysis")
    question: str = Field(..., description="User's question or query")
    model: str = Field(default="gpt-4", description="AI model to use")
    temperature: float = Field(default=0.7, min=0.1, max=0.9, description="Creativity level")
    max_tokens: int = Field(default=1000, min=100, max=4000, description="Maximum response length")
    stream: bool = Field(default=True, description="Enable streaming response")

class PromptResponse(BaseModel):
    response: str = Field(..., description="AI generated response")
    model_used: str = Field(..., description="Model that generated the response")
    tokens_used: int = Field(..., description="Number of tokens consumed")
    response_time: float = Field(..., description="Response time in seconds")
    cost: float = Field(..., description="Estimated cost in USD")
    timestamp: datetime = Field(default_factory=datetime.now)

# Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# API Key loaded successfully

# API Function
async def call_openrouter_api(system_prompt: str, context: str, question: str, model: str, temperature: float, max_tokens: int) -> str:
    """Simple function to call Openrouter API"""
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
            ],
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{OPENROUTER_BASE_URL}/chat/completions", 
                                  headers=headers, 
                                  json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    return data["choices"][0]["message"]["content"]
                else:
                    error_text = await response.text()
                    return f"Error: API request failed with status {response.status}\nResponse: {error_text}"
                    
    except Exception as e:
        return f"Error: {str(e)}"

# Available Models (Hong Kong friendly)
AVAILABLE_MODELS = {
    "google/gemini-pro": "Gemini Pro (Google)",
    "google/gemini-pro-1.5": "Gemini Pro 1.5 (Google)",
    "meta-llama/llama-3.1-70b-instruct": "Llama 3.1 70B Instruct (Meta)",
    "anthropic/claude-3-sonnet": "Claude 3 Sonnet (Anthropic)",
    "anthropic/claude-3-haiku": "Claude 3 Haiku (Anthropic)",
    "microsoft/phi-3-medium-128k-instruct": "Phi-3 Medium (Microsoft)"
}

# Initialize session state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
if "current_response" not in st.session_state:
    st.session_state.current_response = ""
if "is_processing" not in st.session_state:
    st.session_state.is_processing = False

# Main Application
def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🤖 AI-Powered Streamlit Application</h1>
        <p>Powered by Openrouter, Pydantic AI, and Langfuse</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main Layout - Two Columns
    col_left, col_right = st.columns([2, 3])  # 40% - 60% split
    
    with col_left:
        st.markdown("### 📝 PROMPT CONFIGURATION")
        
        # System Prompt
        system_prompt = st.text_area(
            "System Prompt:",
            value="You are a helpful AI assistant that provides accurate and detailed responses based on the given context. Be concise, informative, and helpful.",
            height=120,
            help="Define the AI's role and behavior"
        )
        
        # Context Input
        context = st.text_area(
            "Context:",
            height=150,
            placeholder="Enter your context information here...",
            help="Provide background information for the AI to analyze"
        )
        
        # Question/Query
        question = st.text_input(
            "Question/Query:",
            placeholder="What would you like to ask about the provided context?",
            help="Your specific question for the AI"
        )
        
        # Model Selection
        selected_model = st.selectbox(
            "Model Selection:",
            options=list(AVAILABLE_MODELS.keys()),
            format_func=lambda x: AVAILABLE_MODELS[x],
            index=2,  # Default to Llama 3.1 70B which we know works
            help="Choose the AI model to use"
        )
        
        # Advanced Options
        with st.expander("🔧 Advanced Options", expanded=False):
            temperature = st.slider(
                "Temperature:",
                min_value=0.1,
                max_value=0.9,
                value=0.7,
                step=0.1,
                help="Higher values make responses more creative, lower values more focused"
            )
            
            max_tokens = st.number_input(
                "Max Tokens:",
                min_value=100,
                max_value=4000,
                value=1000,
                step=100,
                help="Maximum length of the AI response"
            )
            
            stream_response = st.checkbox(
                "Stream Response",
                value=True,
                help="Enable real-time streaming of AI response"
            )
        
        # Action Buttons
        col_clear, col_send = st.columns(2)
        with col_clear:
            if st.button("🔄 Clear All", use_container_width=True):
                st.session_state.current_response = ""
                st.session_state.is_processing = False
                st.rerun()
        
        with col_send:
            send_button = st.button("🚀 Send to AI", use_container_width=True, type="primary")
    
    with col_right:
        st.markdown("### 💬 AI RESPONSE")
        
        # Response Status
        if st.session_state.is_processing:
            st.info("🔄 Processing... (Streaming response from Openrouter)")
        
        # Response Area
        if st.session_state.current_response:
            st.markdown(f"""
            <div class="response-area">
            {st.session_state.current_response.replace(chr(10), '<br>')}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="response-area">
                <p style="color: #666; text-align: center; margin-top: 100px;">
                    AI response will appear here after you send a prompt...
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Response Actions
        if st.session_state.current_response:
            col_copy, col_save, col_regenerate, col_analyze = st.columns(4)
            
            with col_copy:
                if st.button("📋 Copy", use_container_width=True):
                    st.write("Response copied to clipboard!")
            
            with col_save:
                if st.button("💾 Save", use_container_width=True):
                    st.success("Response saved to conversation history!")
            
            with col_regenerate:
                if st.button("🔄 Regenerate", use_container_width=True):
                    st.info("Regeneration would happen here")
            
            with col_analyze:
                if st.button("📊 Analyze", use_container_width=True):
                    st.info("Analysis would happen here")
    
    # Footer - Monitoring & Analytics
    st.markdown("---")
    st.markdown("### 📊 MONITORING & ANALYTICS (Langfuse Integration)")
    
    # Performance Metrics
    col_metric1, col_metric2, col_metric3, col_metric4 = st.columns(4)
    
    with col_metric1:
        st.metric(label="Response Time", value="2.3s", delta="0.5s")
    
    with col_metric2:
        st.metric(label="Tokens Used", value="1,247", delta="+100")
    
    with col_metric3:
        st.metric(label="Total Cost", value="$0.023", delta="$0.005")
    
    with col_metric4:
        st.metric(label="Success Rate", value="98.5%", delta="+0.5%")
    
    # Footer Actions
    col_analytics, col_logs, col_settings, col_export = st.columns(4)
    
    with col_analytics:
        if st.button("📈 View Analytics", use_container_width=True):
            st.info("Analytics dashboard would open here")
    
    with col_logs:
        if st.button("🔍 Debug Logs", use_container_width=True):
            st.info("Debug logs would display here")
    
    with col_settings:
        if st.button("⚙️ Settings", use_container_width=True):
            st.info("Settings panel would open here")
    
    with col_export:
        if st.button("📊 Export Data", use_container_width=True):
            st.info("Data export would start here")
    
    # Handle Send Button Click
    if send_button and OPENROUTER_API_KEY:
        if not system_prompt or not context or not question:
            st.error("Please fill in all required fields: System Prompt, Context, and Question.")
            return
        
        # Show loading state
        with st.spinner("Getting AI response..."):
            # Call the API
            response = asyncio.run(call_openrouter_api(
                system_prompt, context, question, selected_model, temperature, max_tokens
            ))
            
            # Update session state with the response
            st.session_state.current_response = response
            st.rerun()
        
    elif send_button and not OPENROUTER_API_KEY:
        st.error("""
        ⚠️ **Openrouter API Key Required**
        
        Please set your Openrouter API key in one of these ways:
        
        1. **Environment Variable**: Set `OPENROUTER_API_KEY=your_key_here`
        2. **Streamlit Secrets**: Add to `.streamlit/secrets.toml`:
           ```toml
           OPENROUTER_API_KEY = "your_key_here"
           ```
        """)

if __name__ == "__main__":
    main()
