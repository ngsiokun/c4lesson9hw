#!/usr/bin/env python3
"""
Demo script for the AI-Powered Streamlit Application
This script demonstrates how to use the application programmatically
"""

import asyncio
import os
from main import PromptRequest, call_openrouter_api, stream_openrouter_response

async def demo_basic_request():
    """Demonstrate a basic API request"""
    print("🚀 Demo: Basic API Request")
    print("=" * 50)
    
    # Create a sample request
    request = PromptRequest(
        system_prompt="You are a helpful AI assistant that explains complex topics simply.",
        context="Machine learning is a subset of artificial intelligence that enables computers to learn and make decisions from data without being explicitly programmed.",
        question="What are the main types of machine learning?",
        model="gpt-4",
        temperature=0.7,
        max_tokens=500,
        stream=False
    )
    
    print(f"System Prompt: {request.system_prompt}")
    print(f"Context: {request.context}")
    print(f"Question: {request.question}")
    print(f"Model: {request.model}")
    print(f"Temperature: {request.temperature}")
    print(f"Max Tokens: {request.max_tokens}")
    print(f"Stream: {request.stream}")
    print()
    
    # Check if API key is available
    if not os.getenv("OPENROUTER_API_KEY"):
        print("⚠️  No OPENROUTER_API_KEY found in environment variables")
        print("   Set it with: export OPENROUTER_API_KEY='your_key_here'")
        return
    
    try:
        print("📡 Sending request to Openrouter...")
        response = await call_openrouter_api(request)
        
        print("✅ Response received!")
        print(f"Response: {response.response}")
        print(f"Model Used: {response.model_used}")
        print(f"Tokens Used: {response.tokens_used}")
        print(f"Response Time: {response.response_time:.2f}s")
        print(f"Cost: ${response.cost:.4f}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

async def demo_streaming_request():
    """Demonstrate a streaming API request"""
    print("\n🔄 Demo: Streaming API Request")
    print("=" * 50)
    
    # Create a sample request
    request = PromptRequest(
        system_prompt="You are a creative storyteller who writes engaging short stories.",
        context="A young programmer discovers an ancient computer in their grandmother's attic.",
        question="Write a short story about what happens when they turn it on.",
        model="gpt-4",
        temperature=0.9,
        max_tokens=800,
        stream=True
    )
    
    print(f"System Prompt: {request.system_prompt}")
    print(f"Context: {request.context}")
    print(f"Question: {request.question}")
    print(f"Model: {request.model}")
    print(f"Temperature: {request.temperature}")
    print(f"Max Tokens: {request.max_tokens}")
    print(f"Stream: {request.stream}")
    print()
    
    # Check if API key is available
    if not os.getenv("OPENROUTER_API_KEY"):
        print("⚠️  No OPENROUTER_API_KEY found in environment variables")
        print("   Set it with: export OPENROUTER_API_KEY='your_key_here'")
        return
    
    try:
        print("📡 Sending streaming request to Openrouter...")
        print("📝 Response (streaming):")
        print("-" * 30)
        
        full_response = ""
        async for chunk in stream_openrouter_response(request):
            print(chunk, end="", flush=True)
            full_response += chunk
        
        print("\n\n✅ Streaming complete!")
        print(f"Total response length: {len(full_response)} characters")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def demo_pydantic_models():
    """Demonstrate Pydantic model validation"""
    print("\n🔧 Demo: Pydantic Model Validation")
    print("=" * 50)
    
    try:
        # Valid request
        valid_request = PromptRequest(
            system_prompt="You are a helpful assistant.",
            context="This is some context.",
            question="What is this?",
            temperature=0.5,
            max_tokens=1000
        )
        print("✅ Valid request created successfully")
        print(f"   Temperature: {valid_request.temperature}")
        print(f"   Max Tokens: {valid_request.max_tokens}")
        
        # Invalid request (will raise validation error)
        print("\n🔄 Testing validation...")
        invalid_request = PromptRequest(
            system_prompt="",  # Empty string (invalid)
            context="",        # Empty string (invalid)
            question="",       # Empty string (invalid)
            temperature=1.5,   # Out of range (invalid)
            max_tokens=5000    # Out of range (invalid)
        )
        
    except Exception as e:
        print(f"❌ Validation error (expected): {str(e)}")

def demo_available_models():
    """Show available AI models"""
    print("\n🤖 Demo: Available AI Models")
    print("=" * 50)
    
    from main import AVAILABLE_MODELS
    
    for model_id, model_name in AVAILABLE_MODELS.items():
        print(f"• {model_id}: {model_name}")
    
    print(f"\nTotal models available: {len(AVAILABLE_MODELS)}")

def main():
    """Run all demos"""
    print("🤖 AI-Powered Streamlit Application - Demo Suite")
    print("=" * 60)
    
    # Demo Pydantic models (no API key needed)
    demo_pydantic_models()
    
    # Demo available models (no API key needed)
    demo_available_models()
    
    # Demo API requests (API key needed)
    print("\n" + "=" * 60)
    print("🌐 API Demo (requires OPENROUTER_API_KEY)")
    print("=" * 60)
    
    # Run async demos
    asyncio.run(demo_basic_request())
    asyncio.run(demo_streaming_request())
    
    print("\n" + "=" * 60)
    print("🎉 Demo complete!")
    print("=" * 60)
    print("\nTo run the full Streamlit app:")
    print("  streamlit run main.py")
    print("\nTo set your API key:")
    print("  export OPENROUTER_API_KEY='your_key_here'")

if __name__ == "__main__":
    main()
