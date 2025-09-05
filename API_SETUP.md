# API Key Setup Instructions

## How to Configure Your Openrouter API Key

1. **Get your API key** from [Openrouter](https://openrouter.ai/keys)

2. **Edit the config.env file** and replace `your_api_key_here` with your actual API key:
   ```
   OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

3. **Save the file** and restart your Streamlit application

## Security Note
- Never commit your actual API key to version control
- The `config.env` file is already in `.gitignore` to protect your credentials
- Keep your API key private and secure

## Alternative Setup Methods
You can also set the API key using:
- **Environment variable**: `set OPENROUTER_API_KEY=your_key_here` (Windows)
- **Streamlit secrets**: Add to `.streamlit/secrets.toml`

## Testing
Once configured, the application will automatically detect your API key and enable the AI functionality.
