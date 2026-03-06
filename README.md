# LM Studio AI Powered Chatbot

A lightweight Python interface that connects to LM Studio to enable natural language conversations with locally-hosted Large Language Models (LLMs). The project allows users to run AI chatbots completely offline using open-source models like Llama, Mistral, and Qwen on their personal computers.

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Project Structure 
```text
ai_chatbot/
├── chatbot.py      # Main chatbot code
├── README.md       # This file
└── requirements.txt # Python dependencies
```

## How to Setup 
## Step 1 : Install Python Packages

```bash
pip install requests
```
## Step 2 : Download & Install LM Studio
- Go to https://lmstudio.ai
- Download for Windows/Mac/Linux 
- Install LM Studio

## Step 3 : Download a Model in LM Studio
- Open LM Studio
- Click "Model Search" tab (left sidebar)
- Search for "phi-2" or "Qwen2.5-0.5B" (small & fast).
- Click "Download"
- Wait for download to complete

## Step 4 : Load the Model

- Go to "Chat" tab (left sidebar)
- Click "Select a model". (at bottom-left corner of the prompt/)
- Choose your downloaded model
- Click "Load"

## Step 5 : Start Local Server
- Go to "Developer" tab (left sidebar)
- Go to "Local Server" tab (left sidebar)
- Click "Start Server"
- Wait for "Server is running" message 
- Keep LM Studio open

## Step 6 : Run the Chatbot

```bash
python chatbot.py
```

## 🛠️ Technical Stack
- Language: Python 3
- Core Library: requests for HTTP communication 
- AI Platform: LM Studio (local LLM server)
- Protocol: REST API (OpenAI-compatible endpoint)
- Models Supported: Any LM Studio compatible model (Llama, Mistral, Phi, Qwen, etc.)

## ✨ Key Features
- Local & Private - No data leaves your computer 
- Simple Interface - Clean Python class with intuitive methods 
- Auto-Detection - Automatically finds LM Studio server port 
- Error Handling - Robust connection and timeout management 
- Interactive CLI - Built-in chat interface for easy testing 
- Model Agnostic - Works with any model loaded in LM Studio

## 🚀 How It Works
- User → Types message in Python script 
- Python Code → Sends HTTP request to LM Studio 
- LM Studio → Processes with local LLM (e.g., Qwen2.5-0.5B)
- Local LLM → Generates intelligent response 
- Python Code → Returns response to user
