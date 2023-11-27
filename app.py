import streamlit as st
from chatbot import predict_class, get_response, intents

st.title("👨🏻‍💻 Asistente virtual")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
# Display a first message when the app is rerun
if "first_message" not in st.session_state:
    st.session_state.first_message = True

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Enviar primer mensaje al usuario 
if st.session_state.first_message:
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown("Hola, ¿cómo puedo ayudarte?")
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": "Hola, ¿cómo puedo ayudarte?"})

    st.session_state.first_message = False
    
# React to user input
if prompt := st.chat_input("¿Cómo puedo ayudarte?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    #get the response from the chatbot
    insts = predict_class(prompt) # Predict the class of the user's input
    res = get_response(insts, intents) # Get a response from the chatbot

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(res)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": res})



