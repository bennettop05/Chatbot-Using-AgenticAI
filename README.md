# 🤖 Agentic AI Chatbot

A conversational AI chatbot built using **LangChain**, **Hugging Face Transformers**, **Tavily Search API**, and **Streamlit**.  
This agent uses tools like file readers and live web search to intelligently answer user queries in a chat interface.

---

## 🚀 Features

- 💬 Conversational AI with memory
- 🔍 Internet search using Tavily
- 📂 File reader tool (read `.txt` files)
- 🤝 Hugging Face LLM (Mistral 7B Instruct)
- 🧠 LangChain ReAct Agent
- 🖥️ Streamlit-based UI

---

## 🧱 Project Structure

agentic_ai/
│
├── agent/
│ └── chatbot_agent.py # Sets up the LangChain agent
│
├── models/
│ └── hf_model.py # Loads Hugging Face LLM
│
├── tools/
│ └── file_reader.py # Custom file reading tool
│
├── app.py # Command-line chat interface
├── ui_streamlit.py # Streamlit chatbot UI
├── .env # API keys (Tavily, Hugging Face)
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🔧 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/agentic_ai.git
cd agentic_ai
2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # macOS/Linux
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add your API keys to .env:
ini
Copy
Edit
HUGGINGFACEHUB_API_TOKEN=your_hf_token
TAVILY_API_KEY=your_tavily_token
💻 Run the Chatbot (CLI)
bash
Copy
Edit
python app.py
🌐 Run the Streamlit App
bash
Copy
Edit
streamlit run ui_streamlit.py
Then open the browser URL shown to chat with your AI agent.

📚 Tools Used
LangChain

Hugging Face Transformers

Tavily API

Streamlit

🧠 Agent Architecture
This agent uses the Conversational ReAct (Reason + Act) pattern from LangChain to:

Understand natural language input

Decide when to use tools (search or file read)

Generate helpful and contextual responses

