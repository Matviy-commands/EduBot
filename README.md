
# EduBot Project

## Overview

The EduBot project is designed to process and visualize vector data from various documents using advanced machine learning techniques. This tool allows you to visualize and explore document embeddings in both 2D and 3D space, making it easier to understand the relationships between different data points.

## Features

- **Vector Store Integration**: Integrates with the Chroma vector store for efficient document embedding management.
- **Dimensionality Reduction**: Uses t-SNE to reduce high-dimensional vector data into 2D or 3D visualizations.
- **Interactive Visualizations**: Generates interactive Plotly visualizations to explore data.
- **Document Classification**: Classifies documents based on their metadata and assigns colors to visualize them in different categories.

## Setup

To set up the EduBot project, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/Matviy-commands/EduBot.git
   ```

2. Navigate to the project directory:
   ```bash
   cd EduBot
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     .env\Scriptsctivate
     ```
   - On MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

6. Create a `.env` file and add the required API keys and environment variables (e.g., OpenAI API key).

## Usage

1. Run the `visualize_vectors.py` script to generate 2D and 3D visualizations of the vector store.
   ```bash
   python visualize_vectors.py
   ```

2. The visualizations will be saved as HTML files (`visualization_2d.html` and `visualization_3d.html`) and opened in your default web browser.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **OpenAI**: For providing the GPT-3/4 API for text embeddings.
- **Chroma**: A powerful vector store for managing embeddings.
- **Plotly**: For interactive data visualizations.
