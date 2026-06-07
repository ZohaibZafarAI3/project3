__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="Company Assistant", page_icon="🏢")

@st.cache_resource
def init():
    # USE THE SAME MODEL YOU USED LOCALLY
    model = SentenceTransformer('all-mpnet-base-v2')
    
    class EF:
        def __init__(self, m):
            self.m = m
        def __call__(self, input):
            if isinstance(input, str):
                input = [input]
            return self.m.encode(input).tolist()
        def embed_query(self, input):
            if isinstance(input, str):
                input = [input]
            return self.m.encode(input).tolist()
    
    client = chromadb.PersistentClient(path='./chroma_db')
    
    # Try to get existing collection (from uploaded chroma.sqlite3)
    try:
        collection = client.get_collection("company_policies")
        print("✅ Using uploaded chroma_db")
    except:
        print("❌ Collection not found, creating new...")
        collection = client.create_collection(
            name="company_policies",
            embedding_function=EF(model)
        )
        # Add sample data if needed
        docs = [
            'Employees receive 20 paid vacation days per year.',
            'Employees can work from home up to 3 days per week.',
            'Employees receive 90 days of paid maternity leave.'
        ]
        collection.add(documents=docs, ids=['v', 'r', 'm'])
    
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
            emb = model.encode([prompt]).tolist()
            res = collection.query(query_embeddings=emb, n_results=1)
            ans = res['documents'][0][0] if res['documents'][0] else "Not found"
        st.write(ans)
    st.session_state.messages.append({"role": "assistant", "content": ans})
