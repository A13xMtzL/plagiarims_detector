from sklearn.metrics import pairwise

#Recibé 2 textos
#Regresa resultados usando diferenciación por coseno

# def preparation(suspicious_embedding, original_embeddings, suspicious_text):
    
#     suspicious_word_count_plagiarims = 0

#     # Cosine similarity calculation sentence by sentence
#     for i in range(len(original_embeddings)):
#         for j in range(len(suspicious_embedding)):
#             cosine_result = pairwise.cosine_similarity(original_embeddings[i],suspicious_embedding[j])
#             if cosine_result[0][0] > 0.75:
#                 suspicious_word_count_plagiarims += len(suspicious_text[j].split(" "))* cosine_result[0][0]


#     return suspicious_word_count_plagiarims

def preparation(suspicious_embedding, original_embeddings):

    cosine_result = pairwise.cosine_similarity(original_embeddings,suspicious_embedding)


    return cosine_result