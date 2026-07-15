from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

cached_embeddings = {

}

def embed(files):
    embeddings = []
    new_descriptions = []


    for file in files.values():
        if file["description"] in cached_embeddings:
            embeddings.append(cached_embeddings[file["description"]])
        else:
            new_descriptions.append(file["description"])
    
    new_embeddings = model.encode(new_descriptions)
    embeddings.append(new_embeddings)

    for description, embedding in zip(new_descriptions, new_embeddings):
        cached_embeddings[description] = embedding
    return embeddings
