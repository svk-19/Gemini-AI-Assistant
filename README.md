# 🤖 Gemini AI Assistant

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://gemini-ai-assistant-iq7fvbgzzpw43mnfxexgbt.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Gemini](https://img.shields.io/badge/Google%20Gemini-API-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

> A conversational AI chatbot with 3 specialist AI modes, persistent memory, and a clean Streamlit interface — powered by Google Gemini API.

🔗 **[Try it live →](https://gemini-ai-assistant-iq7fvbgzzpw43mnfxexgbt.streamlit.app/)**

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧠 Conversation Memory | Remembers full chat history within session |
| 🎭 3 AI Modes | Career Mentor, Python Teacher, Technical Interviewer |
| 💬 Chat History | View and scroll through past messages |
| 📥 Download Chat | Export your conversation as a text file |
| 🗑️ Clear Chat | Reset session instantly |
| 🌙 Dark UI | Clean, responsive Streamlit interface |

---

## 🛠 Tech Stack

- **Language:** Python
- **Framework:** Streamlit
- **AI Model:** Google Gemini API (`gemini-2.0-flash`)
- **Memory:** Session-based conversation history

---

## 🚀 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/svk-19/Gemini-AI-Assistant.git
cd Gemini-AI-Assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your API key
# Create a .streamlit/secrets.toml file and add:
# GEMINI_API_KEY = "your_key_here"

# 4. Run the app
streamlit run streamlit_app.py
```

---

## 📁 Project Structure
