import os
import time
import webbrowser
from dotenv import load_dotenv
import numpy as np
from sklearn.manifold import TSNE
import plotly.graph_objects as go
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


# Download API key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Підключення до бази векторів Chroma
persist_directory = "vector_db"
embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

# Get all documents and vectors
docs = vectordb._collection.get(include=["embeddings", "metadatas", "documents"])

vectors = np.array(docs["embeddings"])
documents = docs["documents"]
doc_types = [meta.get("doc_type", "unknown") for meta in docs["metadatas"]]

# Simple color mapper
colors = [[ 'green', 'red', 'yellow'][['des_school', 'our_team', 'intro'].index(t)] for t in doc_types]

def visualize_2d():
    tsne = TSNE(n_components=2, perplexity=5, random_state=42)
    reduced_vectors = tsne.fit_transform(vectors)

    # Create the 2D scatter plot
    fig = go.Figure(data=[go.Scatter(
        x=reduced_vectors[:, 0],
        y=reduced_vectors[:, 1],
        mode='markers',
        marker=dict(size=5, color=colors, opacity=0.8),
        text=[f"Type: {t}<br>Text: {d[:100]}..." for t, d in zip(doc_types, documents)],
        hoverinfo='text'
    )])

    fig.update_layout(
        title='2D Chroma Vector Store Visualization',
        scene=dict(xaxis_title='x',yaxis_title='y'),
        width=800,
        height=600,
        margin=dict(r=20, b=10, l=10, t=40)
    )
    fig.write_html('visualization_2d.html')

def visualize_3d():
    tsne = TSNE(n_components=3, perplexity=5,random_state=42)
    reduced_vectors = tsne.fit_transform(vectors)

    # Create the 3D scatter plot
    fig = go.Figure(data=[go.Scatter3d(
        x=reduced_vectors[:, 0],
        y=reduced_vectors[:, 1],
        z=reduced_vectors[:, 2],
        mode='markers',
        marker=dict(size=5, color=colors, opacity=0.8),
        text=[f"Type: {t}<br>Text: {d[:100]}..." for t, d in zip(doc_types, documents)],
        hoverinfo='text'
    )])

    fig.update_layout(
        title='3D Chroma Vector Store Visualization',
        scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'),
        width=900,
        height=700,
        margin=dict(r=20, b=10, l=10, t=40)
    )
    fig.write_html('visualization_3d.html')

if __name__ == "__main__":
    visualize_2d()
    visualize_3d()
    time.sleep(1)
    webbrowser.open("visualization_2d.html")
    webbrowser.open("visualization_3d.html")
    print("Готово! Візуалізації відкрито в браузері.")