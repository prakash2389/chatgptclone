import os
import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

os.environ["OPEN_AI_API_KEY"] = os.getenv("OPEN_AI_API_KEY")

# Initialize the ChatOpenAI model
model = ChatOpenAI(
    api_key=os.getenv("OPEN_AI_API_KEY"),
    model="gpt-4o-mini"
)

st.title("ChatGPT like clone by Prakash")

if "openai_model" not in st.session_state:
    st.session_state.openai_model = "gpt-3.5-turbo"

if "openai_temperature" not in st.session_state:
    st.session_state.openai_temperature = 0.2

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])



# Get user input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("ai"):
        # Get ChatGPT response
        response = model.invoke([{"role" : m["role"], "content": m["content"]} for m in st.session_state.messages],
                                stream = True
        )
        st.session_state.messages.append({"role": "ai", "content": response.content})
        st.markdown(response.content)



