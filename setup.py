#!/usr/bin/env python3
"""
Setup script for AI-Powered Streamlit Application
"""
import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up AI-Powered Streamlit Application")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Create virtual environment
    if not os.path.exists("venv"):
        if not run_command("python -m venv venv", "Creating virtual environment"):
            sys.exit(1)
    else:
        print("✅ Virtual environment already exists")
    
    # Activate virtual environment and install dependencies
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:  # macOS/Linux
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    # Install requirements
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Installing dependencies"):
        sys.exit(1)
    
    # Check if config.env exists
    if not os.path.exists("config.env"):
        print("⚠️  config.env not found. Please create it with your API key:")
        print("   OPENROUTER_API_KEY=your_api_key_here")
    else:
        print("✅ config.env found")
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Add your Openrouter API key to config.env")
    print("2. Run: python -m streamlit run main.py")
    print("3. Open your browser to the URL shown")

if __name__ == "__main__":
    main()
