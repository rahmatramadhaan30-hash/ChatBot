import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# 1. Setup UI Streamlit
st.set_page_config(page_title="Asisten Rahmat", page_icon="🤖")
st.title("🤖 Asisten Rahmat")
st.caption("Asisten AI gaul yang siap bantu jelasin istilah IT & Data Science rumit pakai bahasa santai!")

# 2. Setup API Key langsung agar tidak perlu input manual
groq_api_key = "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"

# 3. Inisialisasi LLM via Groq (Llama 3)
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="openai/gpt-oss-120b",
    temperature=0.8,
    max_tokens=512
)

# 4. Setup Prompt Template (Persona Chatbot)
system_prompt = """
Kamu adalah 'Asisten Rahmat', seorang asisten AI yang sangat ahli di bidang Data Science, AI, dan Programming.
Gaya bahasamu santai, asik, pakai bahasa pergaulan anak muda Indonesia (lo, gue, bro, sis), tapi tetap sopan dan informatif.
Tugas utamamu adalah menjelaskan konsep teknis yang rumit menjadi SANGAT SEDERHANA menggunakan analogi kehidupan sehari-hari yang *relatable*.
"""
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{user_input}")
])

# 5. Setup Memory Chat
if "messages" not in st.session_state:
    st.session_state.messages = []
if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.header("Menu")
    if st.button("Obrolan Baru"):
        if st.session_state.messages:
            st.session_state.history.append(st.session_state.messages.copy())
        st.session_state.messages = []

    st.subheader("Riwayat")
    for i, chat in enumerate(reversed(st.session_state.history), 1):
        st.markdown(f"**Chat #{len(st.session_state.history) - i + 1}**")
        for msg in chat:
            st.markdown(f"- **{msg['role']}**: {msg['content']}")
        st.markdown("---")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Input User & Logic Response
if user_input := st.chat_input("Tanya apa aja seputar IT atau Data Science, Bro!"):
    
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Asisten Rahmat lagi mikir bentar..."):
            try:
                chain = prompt_template | llm
                response = chain.invoke({"user_input": user_input})
                
                st.markdown(response.content)
                st.session_state.messages.append({"role": "assistant", "content": response.content})
            except Exception as e:
                st.error(f"Waduh error bro: {e}")