# EduBot – (Dev Version)

**EduBot** is an intelligent bot created to assist students, applicants, and university staff. It uses modern LLM technologies, vector knowledge bases, and a user-friendly web interface.
This repository contains the development version of **EduBot**, focusing on visualizing document embeddings using dimensionality reduction techniques. The data comes from a structured markdown-based knowledge base processed into vector format.

---

## 📦 Project Structure

```
EduBot/
├── main/
│   ├── main.ipynb                # Notebook for embedding + visualization
│   ├── visualize_vectors.py      # CLI tool for UMAP / PCA visualizations
│   └── vector_db/                # Chroma vector database
│
├── knowledge-base/               # Source markdown content grouped by theme
│   ├── university/
│   ├── our_team/
│   ├── des_school/
│   └── intro/
│
├── requirements.txt
├── environment.yml
└── README.md
```

---

## 🚀 Setup

- PC people please follow the instructions in [SETUP-PC.md](SETUP-PC.md)
- Mac people please follow the instructions in [SETUP-mac.md](SETUP-mac.md)  
- Linux people please follow the instructions in [SETUP-linux.md](SETUP-linux.md)

The are also PDF versions of the setup instructions in this folder if you'd prefer.

---

## ⚙️ Usage

### 🔹 Step 1: Prepare the Knowledge Base

Ensure your `main/knowledge-base/` folder contains `.md` files grouped by folders. These documents will be converted into vector embeddings.

### 🔹 Step 2: Generate or Load Vectors

If you don't yet have a Chroma vector DB (`main/vector_db/`), use your embedding pipeline (e.g. `main.ipynb`) to generate and persist embeddings.

> This step requires OpenAI API key and LangChain setup (not included in this version).

### 🔹 Step 3: Run the Visualization Tool

```bash
1. Run the `visualize_vectors.py` script in Jupyter Lab to generate 2D and 3D visualizations of the vector store.
   ```bash
   !python visualize_vectors.py
   ``````

This script loads your Chroma vector DB and generates two HTML files:
- `visualization_2d.html` — PCA 2D projection
- `visualization_3d.html` — UMAP 3D plot

> You can customize vector field, metadata fields, or output paths inside the script.

---

## 📌 Output

All visualizations are saved as interactive HTML files in the `main/` folder. You can open them in your browser.

---

## 🧠 Notes

- This project is modular and designed to be integrated into a larger AI assistant (EduBot).
- The main goal here is to explore vector space clustering and document similarity visually.
- For full chatbot or Gradio integration, refer to the deployment version or separate branches.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.