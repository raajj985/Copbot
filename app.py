import streamlit as st
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import openai
import pickle

# Set up Sambanova API
client = openai.OpenAI(
    api_key="02a3309f-ab10-4283-9f8b-a1f0e17bd231",  # Replace with your actual API key
    base_url="https://api.sambanova.ai/v1",
)

# Load SentenceTransformer model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Use local paths
cache_file = 'embeddings_cache_copbot.pkl'  # Ensure this file is in your project directory

# Load embeddings & metadata safely
try:
    with open(cache_file, 'rb') as f:
        texts, metadata, embeddings = pickle.load(f)
except FileNotFoundError:
    st.error("Error: The embeddings cache file was not found. Please check your file path.")
    st.stop()
except Exception as e:
    st.error(f"Error loading embeddings: {e}")
    st.stop()

# Build FAISS index
d = embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(embeddings)

# Function to retrieve similar components
def retrieve_context(query, top_k=2):
    query_embedding = embedder.encode([query], convert_to_numpy=True).astype('float32')
    distances, indices = index.search(query_embedding, top_k)
    retrieved_texts = [texts[i] for i in indices[0]]

    # Truncate each retrieved text to a fixed number of characters
    max_chars = 1000  # Adjust this value as needed
    truncated_texts = [text[:max_chars] for text in retrieved_texts]

    context = "\n".join(truncated_texts)
    return context

# Function to generate AI-based recommendation
def qa_chain(query, top_k=2):
    context = retrieve_context(query, top_k)
    prompt = f"""You are a helpful assistant specialized in providing information for law enforcement in Tamil Nadu.

Based on the following context of legal and procedural information:
{context}

Answer the following query with a detailed response:
{query}
"""
    messages = [
        {"role": "system", "content": "You are a helpful assistant for law enforcement in Tamil Nadu."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model="Meta-Llama-3.3-70B-Instruct",
        messages=messages,
        temperature=0.1,
        top_p=0.1
    )

    return response.choices[0].message.content

# Streamlit UI
st.set_page_config(page_title="CopBot AI Assistant", page_icon="🚔", layout="wide")
st.title("🚔 CopBot AI Assistant")

# Sidebar for FAQs
st.sidebar.header("FAQs")
faqs = {
    "What are the legal procedures for handling a public gathering?": "Details about legal procedures...",
    "How to report a crime?": "Steps to report a crime...",
    "What are the emergency contact numbers?": "List of emergency contact numbers...",
    "How to apply for a police clearance certificate?": "Procedure for applying for a police clearance certificate...",
    "What are the traffic rules in Tamil Nadu?": "Information about traffic rules..."
}

selected_faq = st.sidebar.selectbox("Select a FAQ", list(faqs.keys()))
st.sidebar.info(faqs[selected_faq])

# User Inputs
st.header("Ask CopBot")
query = st.text_area("Enter your query related to law enforcement in Tamil Nadu")

# Generate recommendation on button click
if st.button("Get Answer"):
    if query.strip():
        with st.spinner("Generating response..."):
            answer = qa_chain(query, top_k=2)
        st.success("Here’s the response to your query:")
        st.write(answer)
    else:
        st.warning("Please enter a valid query.")

# Additional styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 10px;
    }
    .stTextArea textarea {
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
