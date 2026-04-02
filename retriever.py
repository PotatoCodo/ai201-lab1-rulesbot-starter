import chromadb
from chromadb.utils import embedding_functions
from config import CHROMA_COLLECTION, CHROMA_PATH, EMBEDDING_MODEL, N_RESULTS

# Embedding function and ChromaDB client are initialized once at module load.
# sentence-transformers downloads the model on first use — this may take
# 30–60 seconds the very first time. Subsequent runs use a local cache.
_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL
)
_client = chromadb.PersistentClient(path=CHROMA_PATH)
_collection = _client.get_or_create_collection(
    name=CHROMA_COLLECTION,
    embedding_function=_ef,
    metadata={"hnsw:space": "cosine"},
)


def get_collection():
    """Return the ChromaDB collection. Used by app.py during ingestion."""
    return _collection


def embed_and_store(chunks):
    """
    Embed a list of chunks and store them in the vector database.

    TODO — Milestone 1 (complete after chunk_document):

    `chunks` is the list returned by chunk_document(). Each item is a dict:
      - "text"     : the chunk text
      - "game"     : the game name
      - "chunk_id" : a unique identifier

    Use _collection.add() to store them. It takes:
      - documents : list of strings  → the chunk texts
      - metadatas : list of dicts    → store {"game": ...} here so retrieve()
                                       can surface which game a result came from
      - ids       : list of strings  → use chunk_id

    After adding, print the total number of chunks stored so you can confirm
    everything made it in before moving on.
    """
    pass


def retrieve(query, n_results=N_RESULTS):
    """
    Find the most relevant rule chunks for a user's question.

    TODO — Milestone 2:

    Use _collection.query() to run a semantic search. It takes:
      - query_texts : a list containing your query string
      - n_results   : how many results to return
      - include     : what to return — use ["documents", "metadatas", "distances"]

    Return a list of dicts, each with:
      - "text"     : the chunk text
      - "game"     : the game name (pull this from metadatas)
      - "distance" : the similarity score (lower = more similar for cosine)

    Note: _collection.query() returns nested lists (one per query). You only
    have one query, so you'll want index [0] to get the actual results.
    """
    if _collection.count() == 0:
        return []

    # Your implementation here.
    return []
