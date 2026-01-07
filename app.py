import os
import sys

import pandas as pd
import streamlit as st

from src.config import AppConfig
from src.Custome_Exception import CustomException

from src.controller.chat_controller import ChatController
from src.llm.create_pandas_agent import AgentManager


# Load Pandas agent
agent_manager = AgentManager()

# Ensure Upload Directory
upload_dir = os.path.dirname(AppConfig.UPLOADED_CSV_PATH)
os.makedirs(upload_dir, exist_ok=True)

# Page config 
st.set_page_config(page_title="InsightGen AI",layout="wide")

st.title("📊 InsightGen AI – Data Analysis Chatbot")
st.markdown("Upload a CSV file to start analyzing your data using GenAI.")
st.divider()

# ---------- Session defaults ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "model" not in st.session_state:
    st.session_state.model = agent_manager.create_model()

# ---------- Upload UI ----------

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    uploaded_file = st.file_uploader("Upload your CSV file",type=["csv"])

# ---------- Handle uploaded file ----------
if uploaded_file is not None:
    # Save CSV using AppConfig path
    with open(AppConfig.UPLOADED_CSV_PATH, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ File uploaded successfully!")

    df = pd.read_csv(AppConfig.UPLOADED_CSV_PATH)
    st.session_state.df = df

    pandas_agent = agent_manager.create_pandas_agent(model=st.session_state.model, df=df)
    chat_controller = ChatController(pandas_agent)
    st.session_state.controller = chat_controller

    st.subheader("🔍 Preview of Uploaded Data")
    st.dataframe(df.head())
    st.divider()

# ---------- Render previous chat ----------
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# ---------- Chat input ----------
question = st.chat_input(
    "Ask something like: 'What are the column names and their types?'"
)

if question:
    # User message
    st.session_state.messages.append({"role": "user", "content": question})
    st.chat_message("user").write(question)

    controller = st.session_state.get("controller")

    if controller is None:
        assistant = st.chat_message("assistant")
        assistant.write("Please upload a CSV first.")
    else:
        with st.spinner("Thinking..."):
            response = controller.ask(question)
            code, answer = agent_manager.format_agent_response(response)

            assistant = st.chat_message("assistant")

            if code and code != "No code executed":
                assistant.markdown("**🧾 Code executed:**")
                assistant.code(code, language="python")
        
            assistant.markdown("**📤 Output:**")
            assistant.write(answer)

            # Store readable output only in history
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )