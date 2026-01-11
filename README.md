# 📊 InsightGen AI — GenAI-Powered Data Analysis Chatbot

InsightGen AI is an **interactive GenAI-powered data analysis chatbot** that allows users to upload CSV files, ask natural language questions about the data, and receive **executed pandas code, outputs, visualizations, and an auto-generated Jupyter notebook** — all powered by a **locally hosted LLaMA model via Ollama**.

This project demonstrates **Agentic AI**, **local LLM deployment**, and **end-to-end automated exploratory data analysis (EDA)**.

---
## 🎬 Demo Video
https://github.com/user-attachments/assets/2fefb065-e70b-4cc3-b4ff-87b82683ca81

---

## 🚀 Key Features

- 📂 Upload CSV files for analysis
- 💬 Ask natural language questions about your data
- 🧠 Local LLM inference using **LLaMA (Ollama)**
- 🧮 Automatic pandas code generation & execution
- 📊 Matplotlib visualizations rendered in Streamlit
- 📓 Auto-generated **EDA Jupyter notebook**
- ⬇️ Download notebook at any time
- 🔁 Session-based chat history
- 🛡️ Robust error handling & UI stability

---

## 🧠 System Architecture
```
User
↓
Streamlit UI (app.py)
↓
ChatController
↓
LangChain Pandas Agent
↓
Local LLaMA (Ollama)
↓
Pandas / Matplotlib Execution
↓
Notebook Generation + UI Rendering
```
---

## 📁 Project Structure
```
InsightGen-AI/
│
├── app.py # Streamlit application entry point
├── requirements.txt # Python dependencies
├── README.md # Project documentation
│
├── data/
│ ├── uploads/
│ │ └── uploaded_csv.csv
│ └── generated_notebook/
│ └── eda_notebook_*.ipynb
│
├── src/
│ ├── controller/
│ │ └── chat_controller.py
│ │
│ ├── llm/
│ │ └── create_pandas_agent.py
│ │
│ ├── notebook/
│ │ └── notebook_writer.py
│ │
│ ├── config.py
│ └── Custome_Exception.py
│
└── insightenv/ # Local Python virtual environment
```
---

## 🧰 Tech Stack

- **Frontend**: Streamlit  
- **LLM**: LLaMA (via Ollama)  
- **Agent Framework**: LangChain (Pandas Agent)  
- **Data Processing**: Pandas, NumPy  
- **Visualization**: Matplotlib  
- **Notebook Handling**: nbformat  
- **Language**: Python 3.11  

---

## ⚙️ Local Setup Instructions

### 1️ Clone the Repository
```bash
git clone https://github.com/your-username/InsightGen-AI.git
cd InsightGen-AI
```
### 2️ Create Virtual Environment
```bash
python3.11 -m venv insightenv
source insightenv/bin/activate
```

### 3️ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4 Install & Run Ollama (Local LLM)
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.1:8b
ollama run llama3.1:8b
```
### 5 Run the Application
```bash
streamlit run app.py
```
