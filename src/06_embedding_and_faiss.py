embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

chunk_embeddings = embedding_model.encode(chunks)
print(chunk_embeddings.shape)

dimension = chunk_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(chunk_embeddings))
