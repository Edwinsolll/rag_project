import streamlit as st
import os
import chat

st.title("PDF Chatbot")
st.caption("Ask questions about your document")

# chat history stored in session
if "messages" not in st.session_state:
    st.session_state.messages = []

# display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# input box at bottom
if question := st.chat_input("Ask a question..."):
    
    # show user message
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    # get and show answer
    with st.chat_message("danceing"):
        with st.spinner("cycle..."):
            response = chat.answer(question)
        st.write(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})