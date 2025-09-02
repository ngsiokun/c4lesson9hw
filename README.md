# 🤖 AI-Powered Streamlit Application

A sophisticated Streamlit web application that leverages Openrouter's AI models to provide intelligent, context-aware responses with real-time streaming capabilities.

## ✨ Features

- **🤖 AI Integration**: Seamlessly connects with Openrouter API for access to multiple AI models
- **📝 Three-Input System**: System prompt, context, and question/query inputs
- **🔄 Real-time Streaming**: Live AI response streaming for better user experience
- **🎛️ Advanced Controls**: Temperature, max tokens, and model selection
- **📊 Monitoring Dashboard**: Performance metrics and analytics integration
- **💾 Conversation History**: Save and review previous interactions
- **📱 Responsive Design**: Beautiful, modern UI that works on all devices

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up API Keys

#### Option A: Environment Variables
```bash
export OPENROUTER_API_KEY="your_api_key_here"
```

#### Option B: Streamlit Secrets (Recommended)
Create `.streamlit/secrets.toml`:
```toml
OPENROUTER_API_KEY = "your_api_key_here"
```

### 3. Run the Application

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

## 🔧 Configuration

### Available AI Models
- **GPT-4** (OpenAI) - Most capable, highest cost
- **GPT-4 Turbo** (OpenAI) - Fast, cost-effective
- **Claude 3 Opus** (Anthropic) - Creative and analytical
- **Claude 3 Sonnet** (Anthropic) - Balanced performance
- **Llama 3 70B** (Meta) - Open source alternative
- **Gemini Pro** (Google) - Google's latest model

### Advanced Options
- **Temperature**: Controls creativity (0.1 = focused, 0.9 = creative)
- **Max Tokens**: Limits response length (100-4000 tokens)
- **Stream Response**: Enable real-time streaming

## 📁 Project Structure

```
c4lesson9hw/
├── main.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── project.md             # Project documentation
├── ui_mockup.md           # UI design specifications
├── layout_visualization.md # Layout structure
└── visual_mockup_simple.html # Interactive HTML mockup
```

## 🎯 How It Works

### 1. **Input Configuration**
- **System Prompt**: Define the AI's role and behavior
- **Context**: Provide background information for analysis
- **Question**: Ask your specific query

### 2. **AI Processing**
- Sends structured prompt to Openrouter API
- Processes response with streaming or batch mode
- Calculates usage metrics and costs

### 3. **Response Display**
- Real-time streaming of AI responses
- Action buttons for copy, save, regenerate
- Conversation history tracking

### 4. **Monitoring**
- Performance metrics dashboard
- Token usage and cost tracking
- Success rate monitoring

## 🔑 API Key Setup

### Get Openrouter API Key
1. Visit [Openrouter.ai](https://openrouter.ai)
2. Create an account
3. Generate an API key
4. Add to your environment or Streamlit secrets

### Supported File Types
- **Text Files**: `.txt`, `.md`
- **Documents**: `.pdf`, `.docx` (basic support)

## 🛠️ Development

### Prerequisites
- Python 3.8+
- Streamlit 1.28.0+
- Pydantic 2.0.0+
- aiohttp 3.8.0+

### Local Development
```bash
# Clone repository
git clone <your-repo>
cd c4lesson9hw

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
streamlit run main.py --server.port 8501
```

### Environment Variables
```bash
OPENROUTER_API_KEY=your_key_here
LANGFUSE_PUBLIC_KEY=your_langfuse_key  # Optional
LANGFUSE_SECRET_KEY=your_langfuse_secret  # Optional
```

## 📊 Monitoring & Analytics

The application includes a comprehensive monitoring dashboard:

- **Response Time**: Track API performance
- **Token Usage**: Monitor AI model consumption
- **Cost Tracking**: Estimate API costs
- **Success Rate**: Track request success/failure

## 🔮 Future Enhancements

- [ ] **Langfuse Integration**: Advanced analytics and monitoring
- [ ] **File Processing**: Enhanced PDF and document support
- [ ] **User Authentication**: Multi-user support
- [ ] **API Rate Limiting**: Smart request throttling
- [ ] **Export Features**: Save conversations and analytics
- [ ] **Custom Models**: Support for fine-tuned models

## 🐛 Troubleshooting

### Common Issues

1. **API Key Not Found**
   - Ensure environment variable is set correctly
   - Check Streamlit secrets file location
   - Restart the application after setting keys

2. **Streaming Not Working**
   - Verify `stream_response` checkbox is enabled
   - Check network connectivity to Openrouter
   - Ensure API key has streaming permissions

3. **Model Not Available**
   - Verify model name in `AVAILABLE_MODELS`
   - Check Openrouter model availability
   - Ensure API key has access to selected model

### Debug Mode
Enable debug logging by setting:
```bash
export STREAMLIT_LOG_LEVEL=debug
```

## 📚 API Documentation

### Openrouter API
- [Openrouter Documentation](https://openrouter.ai/docs)
- [Model Pricing](https://openrouter.ai/models)
- [API Reference](https://openrouter.ai/docs/api)

### Streamlit
- [Streamlit Documentation](https://docs.streamlit.io)
- [Component Gallery](https://docs.streamlit.io/library/api-reference)
- [Deployment Guide](https://docs.streamlit.io/streamlit-community-cloud)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Openrouter**: For providing access to multiple AI models
- **Streamlit**: For the amazing web app framework
- **Pydantic**: For robust data validation
- **Community**: For feedback and contributions

---

**Happy AI Prompting! 🚀**

For support or questions, please open an issue in the repository.
