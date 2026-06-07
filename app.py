import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="Company Assistant", page_icon="🏢")

@st.cache_resource
def init():
    model = SentenceTransformer('all-mpnet-base-v2')
    client = chromadb.PersistentClient(path='./chroma_db')
    collection = client.get_collection("company_policies")
    return collection, model

collection, model = init()

if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title("🏢 Company Knowledge Assistant")

with st.sidebar:
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask a question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Searching..."):
            query_embedding = model.encode([prompt]).tolist()
            results = collection.query(query_embeddings=query_embedding, n_results=1)
            answer = results['documents'][0][0] if results['documents'][0] else "Not found"
        st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})