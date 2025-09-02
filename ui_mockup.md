# Streamlit App UI Mockup

## Main Application Interface

### Header Section
```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    🤖 AI-Powered Streamlit Application                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  [Settings] [History] [Help]                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Input Section (Left Panel)
```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 📝 PROMPT CONFIGURATION                                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ System Prompt:                                                              │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ You are a helpful AI assistant that provides accurate and detailed     │ │
│ │ responses based on the given context.                                  │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ Context:                                                                    │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ [Upload File] or [Paste Text]                                          │ │
│ │                                                                         │ │
│ │ ┌─────────────────────────────────────────────────────────────────────┐ │ │
│ │ │ Enter or upload your context information here...                   │ │
│ │ │                                                                     │ │
│ │ │ (Supports: .txt, .pdf, .docx, .md files)                          │ │
│ │ └─────────────────────────────────────────────────────────────────────┘ │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ Question/Query:                                                             │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ What would you like to ask about the provided context?                │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ [🔄 Clear All]                    [🚀 Send to AI]                     │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ Model Selection:                                                            │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ [Dropdown: GPT-4, Claude-3, Llama-3, etc.]                           │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ Advanced Options:                                                           │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ Temperature: [0.1] ────────── [0.9]                                   │ │
│ │ Max Tokens: [1000]                                                    │ │
│ │ Stream Response: ☑️                                                   │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Response Section (Right Panel)
```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 💬 AI RESPONSE                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Response Status:                                                            │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ 🔄 Processing... (Streaming response from Openrouter)                 │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ AI Response:                                                                │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ Based on the context you provided, here is my analysis...             │ │
│ │                                                                         │ │
│ │ The key points from your context are:                                  │ │
│ │ • Point 1                                                              │ │
│ │ • Point 2                                                              │ │
│ │ • Point 3                                                              │ │
│ │                                                                         │ │
│ │ [Response continues streaming in real-time...]                         │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ Response Actions:                                                           │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ [📋 Copy] [💾 Save] [🔄 Regenerate] [📊 Analyze]                     │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ Conversation History:                                                       │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ Previous Conversations:                                                 │ │
│ │ ┌─────────────────────────────────────────────────────────────────────┐ │ │
│ │ │ Q: How does the system work?                                        │ │
│ │ │ A: The system processes...                                          │ │
│ │ └─────────────────────────────────────────────────────────────────────┘ │ │
│ │ ┌─────────────────────────────────────────────────────────────────────┐ │ │
│ │ │ Q: What are the benefits?                                           │ │
│ │ │ A: The main benefits include...                                     │ │
│ │ └─────────────────────────────────────────────────────────────────────┘ │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Footer Section
```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 📊 MONITORING & ANALYTICS (Langfuse Integration)                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Performance Metrics:                                                        │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ Response Time: 2.3s | Tokens Used: 1,247 | Cost: $0.023              │ │
│ │ Model: GPT-4 | API Calls: 47 | Success Rate: 98.5%                    │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ [📈 View Analytics] [🔍 Debug Logs] [⚙️ Settings]                    │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Key UI Features

### 1. **Responsive Layout**
- Two-column design: Input panel (left) and Response panel (right)
- Collapsible sections for better space utilization
- Mobile-friendly responsive design

### 2. **Input Components**
- **System Prompt**: Large text area for defining AI behavior
- **Context Input**: File upload + text input with drag-and-drop support
- **Question Field**: Clean text input for user queries
- **Model Selection**: Dropdown for choosing AI models
- **Advanced Options**: Sliders and toggles for fine-tuning

### 3. **Response Display**
- **Real-time Streaming**: Live text appearance as AI responds
- **Status Indicators**: Clear feedback on processing state
- **Action Buttons**: Copy, save, regenerate, and analyze options
- **Conversation History**: Scrollable list of previous interactions

### 4. **Monitoring Dashboard**
- **Performance Metrics**: Response time, token usage, costs
- **Analytics**: Usage patterns and model performance
- **Debug Tools**: Logs and error tracking

### 5. **Visual Design Elements**
- **Color Scheme**: Professional dark/light theme options
- **Icons**: Intuitive icons for all actions and sections
- **Typography**: Clear hierarchy with readable fonts
- **Spacing**: Consistent padding and margins throughout

### 6. **User Experience Features**
- **Auto-save**: Automatic saving of conversations
- **Keyboard Shortcuts**: Quick access to common actions
- **Tooltips**: Helpful hints for complex features
- **Progress Indicators**: Visual feedback for long operations

This mockup provides a comprehensive UI design that covers all the requirements from project.md while maintaining a clean, professional appearance that's intuitive for users to navigate and use effectively.
