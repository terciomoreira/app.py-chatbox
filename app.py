import streamlit as st

# Configuração da página
st.set_page_config(page_title="Meu Chatbox", page_icon="🤖")
st.title("💬 Chatbox Simples")

# Inicializa o histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada do utilizador
if prompt := st.chat_input("Diga o que quer"):
    # Adiciona mensagem do utilizador ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta lógica do bot (podes personalizar aqui)
    response = f"Tu disseste: {prompt}. Eu sou um bot básico!"
    
    # Exibe resposta do bot
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
