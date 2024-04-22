import re
import nltk
import collections
import chromadb
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

def text_preprocessing(corpus, processing_flag):
    # Compiled regular expressions for patterns
    patterns = [
        re.compile(r'\d+\r\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}'),
        re.compile(r'\r\nWatch any video online with Open-SUBTITLES\r\nFree Browser extension: osdb.link/ext\r\n\r\n\r\n'),
        re.compile(r'Please rate this subtitle at www.osdb.link/agwma\r\nHelp other users to choose the best subtitles'),
        re.compile(r'(\r\n)+'),
        re.compile(r'<[/]?\w+>')
    ]
    # Stopwords
    stop_words = set(stopwords.words('english'))

    # Remove patterns
    for pattern in patterns:
        corpus = re.sub(pattern, '', corpus)

    # Remove special characters and convert to lowercase
    corpus = re.sub('[^a-zA-Z]', ' ', corpus).lower()

    # Tokenize
    words = word_tokenize(corpus)

    # Stemming or Lemmatization
    if processing_flag == "stemming":
        # Stemming
        stemmer = SnowballStemmer(language='english')
        processed_text = ' '.join(stemmer.stem(word) for word in words if word not in stop_words)
    else:
        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        processed_text = ' '.join(lemmatizer.lemmatize(word) for word in words if word not in stop_words)

    return processed_text

def getResults(query, processing_flag):
    # Preprocess the query text
    processed_query = text_preprocessing(query, processing_flag)
    print(processed_query)

    # Create a persistent client for ChromaDB
    client = chromadb.PersistentClient(path=r"M:\innomatics\project4\Project\db_all\ChromaDB")
    # Create or get a collection
    collection = client.get_or_create_collection(name='transcripts', metadata={"hnsw:space": "cosine"})

    # Read the names file
    names_df = pd.read_csv(r'M:\innomatics\project4\Project\data\names_df.csv')

    # Query with ChromaDB
    results = collection.query(
        query_texts=[processed_query],
        n_results=20
    )

    print(results)

    # Get distinct names from results
    ids = results['ids'][0]
    distinct_names = []
    seen_parent_ids = set()
    for result_id in ids:
        parent_id = result_id.split('-')[0]
        if parent_id not in seen_parent_ids:
            seen_parent_ids.add(parent_id)
            name = names_df.loc[int(parent_id), 'name']
            distinct_names.append(name)

    return distinct_names[:10]
