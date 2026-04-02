import os
from config import DOCS_PATH


def load_documents():
    """Load all .txt rule documents from the docs folder."""
    documents = []
    for filename in sorted(os.listdir(DOCS_PATH)):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCS_PATH, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            game_name = filename.replace(".txt", "").replace("_", " ").title()
            documents.append({
                "game": game_name,
                "filename": filename,
                "text": text,
            })
    print(f"Loaded {len(documents)} rule document(s): {[d['game'] for d in documents]}")
    return documents


def chunk_document(text, game_name):
    """
    Split a rule document into chunks ready for embedding.

    TODO — Milestone 1:

    Right now this returns an empty list, so nothing gets stored and RulesBot
    can't answer anything. Your job is to implement a chunking strategy.

    Before writing code, talk through these questions with your group:
      - What's a reasonable chunk size for rule book text? Too small and you
        lose context. Too large and retrieval becomes imprecise.
      - Should chunks overlap? What would overlap help preserve?
      - How will you attach the game name to each chunk so retrieval knows
        which game an answer came from?

    Your function should return a list of dicts. Each dict must have:
      - "text"     : the chunk text (str)
      - "game"     : the game name, e.g. "Catan" (str)
      - "chunk_id" : a unique identifier, e.g. "catan_0", "catan_1" (str)

    A simple starting point: split on double newlines (paragraphs), then
    filter out any chunks that are too short to be useful.
    """
    return []
