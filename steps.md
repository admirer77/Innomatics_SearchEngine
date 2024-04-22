# Transcript Semantic Search Engine

Welcome to our Transcript Semantic Search Engine project! This Python 3.9-based tool is designed for retrieving transcripts of movies, TV shows, and anime through user queries. It harnesses natural language processing (NLP) and machine learning (ML) techniques to create an intuitive interface for exploring and interacting with transcript data.

## Key Features

- **Semantic Search:** Find transcripts based on queries containing character names or descriptions.
- **Chunking Strategy:** Break transcripts into manageable chunks for efficient processing with vectorization models.
- **Vector Database:** Utilize ChromaDB, an open-source vector database, to store and retrieve transcript vectors effectively.
- **Web Application:** Develop an interactive web interface using Streamlit for users to input queries, browse transcripts, and download desired files.

## Requirements

Ensure you have the following installed:

- Python 3.9
- Streamlit
- ChromaDB
- BERT Sentence Transformer
- Other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/admirer77/Innomatics_SearchEngine.git
    ```

2. Navigate to the project directory:

    ```
    cd Innomatics_SearchEngine
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit web application:

    ```
    streamlit run app.py
    ```

2. Open the web application in your browser and start using the search engine.

## Note

Due to its size, the database file cannot be provided on GitHub. If you need the database, please contact us at [your email or preferred communication channel] and we'll be happy to assist you.
