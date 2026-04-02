# Spec: `chunk_document()`

**File:** `ingest.py`
**Status:** Spec incomplete — fill in all blank fields before implementing

---

## Purpose

Split a single rule book document into smaller chunks suitable for embedding and semantic retrieval. Each chunk should carry enough context to be meaningful on its own when retrieved in response to a user query.

---

## Input / Output Contract

**Inputs:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `text` | `str` | The full text of a rule book document |
| `game_name` | `str` | The name of the game this document belongs to (e.g., `"Catan"`) |

**Output:** `list[dict]`

Each dict in the returned list must contain exactly these keys:

| Key | Type | Description |
|-----|------|-------------|
| `"text"` | `str` | The chunk text |
| `"game"` | `str` | The game name (passed through from `game_name`) |
| `"chunk_id"` | `str` | A unique identifier for this chunk (e.g., `"catan_0"`, `"catan_1"`) |

Returns an empty list `[]` if the input text is empty or produces no valid chunks.

---

## Design Decisions

*Complete the fields below before writing any code. Use your AI tool in Plan or Ask mode to help you reason through what belongs here — but the decisions are yours.*

---

### Splitting approach

*How will you split the document text into segments? Describe the method — not the code.*

```
[your answer here]
```

---

### Chunk size

*What is the target size of each chunk, and in what unit (characters, words, tokens, paragraphs)?*

```
[your answer here]
```

---

### Overlap

*Will chunks overlap? If yes, by how much and why? If no, explain why overlap isn't necessary for this document type.*

```
[your answer here]
```

---

### Minimum chunk length

*What is the minimum length a chunk must be to be included? What do you do with segments that are shorter than this?*

```
[your answer here]
```

---

### Rationale

*In 2–3 sentences: why does this strategy fit rule book text specifically? What would break if you used a different approach?*

```
[your answer here]
```

---

### Known limitations

*What does this strategy get wrong or handle poorly? What kinds of rules or passages will be chunked badly by your approach?*

```
[your answer here]
```

---

## Implementation Notes

*Fill this in after implementing, before moving to Milestone 2.*

**Actual chunk count produced across all 8 rule books:**

```
[your answer here]
```

**One thing that surprised you or didn't match your spec:**

```
[your answer here]
```
