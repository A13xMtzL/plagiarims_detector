from sklearn.metrics import pairwise
import numpy as np

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

# def preparation(suspicious_embedding, original_embeddings):

#     #print('original: ',original_embeddings)
#     #print('chospechoso: ',suspicious_embedding)
#     cosine_result = pairwise.cosine_similarity(original_embeddings,suspicious_embedding)


#     return cosine_result

import numpy as np

import numpy as np

def cosSimilarity(vectorOfVectors):
    max_length = max(len(vec) for vec in vectorOfVectors)

    # Pad shorter vectors with zeros
    padded_vectors = [np.pad(vec, (0, max_length - len(vec)), 'constant') for vec in vectorOfVectors]

    for i in range(len(padded_vectors)):
        padded_vectors[i] = np.array(padded_vectors[i])

    print("Lengths of padded vectors:", [len(vec) for vec in padded_vectors])  # Debugging

    num = padded_vectors[0]

    for i in range(1, len(padded_vectors)):
        print("Shapes of num and vector:", num.shape, padded_vectors[i].shape)  # Debugging
        num = num * padded_vectors[i]

    num = np.sum(num)
    den = 1

    for i in range(len(padded_vectors)):
        den *= np.sqrt(np.sum(padded_vectors[i] ** 2))

    return num / den

