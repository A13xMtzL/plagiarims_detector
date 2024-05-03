from collections import Counter

# # # Universal Sentence Encoder
# # module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
# # model = hub.load(module_url)
# # print ("module %s loaded" % module_url)

# # # Función para correr el modelo
# # def embed(input):
# #     return model(input)

# --------------Seción de código para la comparación de texto--------------
# # # # from collections import Counter
# # # # from sklearn.feature_extraction.text import CountVectorizer

# # # # def word_occurrences_in_vectors(vector1, vector2):
# # # #     # Create Counters for each vector
# # # #     counter1 = Counter(vector1)
# # # #     counter2 = Counter(vector2)
    
# # # #     # Initialize lists to store counts for each vector
# # # #     counts_vector1 = []
# # # #     counts_vector2 = []
    
# # # #     # Iterate over unique words in both vectors
# # # #     unique_words = set(vector1 + vector2)
# # # #     for word in unique_words:
# # # #         # Get the count of the word in each vector
# # # #         count_vector1 = counter1[word]
# # # #         count_vector2 = counter2[word]
        
# # # #         # Append the counts to the respective lists
# # # #         counts_vector1.append(count_vector1)
# # # #         counts_vector2.append(count_vector2)
    
# # # #     return counts_vector1, counts_vector2

# # # # # Example usage
# # # # vector1 = ["apple", "banana", "apple", "orange"]
# # # # vector2 = ["banana", "grape", "apple", "banana"]

# # # # counts_vector1, counts_vector2 = word_occurrences_in_vectors(vector1, vector2)

# # # # print("Counts in vector1:", counts_vector1)
# # # # print("Counts in vector2:", counts_vector2)

# --------------Seción de código para la comparación de texto--------------
from sklearn.preprocessing import OneHotEncoder

"""def word_occurrences_in_vectors(vector1, vector2):
    counter1 = Counter(vector1)
    counter2 = Counter(vector2)
    
    # Initialize lists to store counts for each vector
    counts_vector1 = []
    counts_vector2 = []
    
    # Iterate over unique words in both vectors
    unique_words = set(vector1 + vector2)
    for word in unique_words:
        # Get the count of the word in each vector
        count_vector1 = counter1[word]
        count_vector2 = counter2[word]
        
        # Append the counts to the respective lists
        counts_vector1.append(count_vector1)
        counts_vector2.append(count_vector2)
    
    return counts_vector1, counts_vector2"""

def word_occurrences_in_vectors(vector1, vector2):
    """
    Función para contar la cantidad de palabras en común entre dos vectores.
    """
    # Convertir listas en tuplas para hacerlas hashables
    vector1 = tuple(vector1)
    vector2 = tuple(vector2)
    
    # Crear Counters para cada vector
    counter1 = Counter(vector1)
    counter2 = Counter(vector2)
    
    # Inicializar listas para almacenar recuentos para cada vector
    counts_vector1 = []
    counts_vector2 = []
    
    # Crear un conjunto de palabras únicas en ambos vectores
    unique_words = set(vector1 + vector2)
    
    # Iterar sobre las palabras únicas en ambos conjuntos
    for word in unique_words:
        # Obtener el recuento de la palabra en cada vector
        count_vector1 = counter1[word]
        count_vector2 = counter2[word]
        
        # Agregar los recuentos a las listas respectivas
        counts_vector1.append(count_vector1)
        counts_vector2.append(count_vector2)
        print(counts_vector1)
        print(counts_vector2)
    
    return counts_vector1, counts_vector2





# Example usage
vector1 = ["apple", "banana", "apple", "orange"]
vector2 = ["banana", "grape", "apple", "banana"]

one_hot_vector1  = word_occurrences_in_vectors(vector1, vector2)
print("One-hot vector for vector1:", one_hot_vector1)

#-------------section------------- 
#!! Sección del código para la comparación de vectores

# from io import StringIO
# from Lexer import Lexer, Tag
# def preprocessText(text):
#     lexer = Lexer(StringIO(text))
    
#     token_list = []
#     token = lexer.scan()
    
#     while token.getTag() != Tag.EOF:
#         token_list.append(token)
#         token = lexer.scan()

#     return " ".join([str(token) for token in token_list])

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np


# # # Read and preprocess the code
# # with open("code1.txt", "r", encoding="utf-8") as file:
# #     code_1 = preprocessText(file.read())

# # with open("code2.txt", "r", encoding="utf-8") as file:
# #     code_2 = preprocessText(file.read())
def __words_occurrences_in_vectors(vector1, vector2):
    # Creamos un objeto CountVectorizer con stop_words establecido en None
    vectorizer = CountVectorizer(stop_words=None)

    # Calculamos los recuentos de palabras
    word_count = vectorizer.fit_transform([vector1, vector2])

    # Con esto podemos saber si el texto tiene o no una palabra
    binary_word_count = word_count.toarray() > 0

    # Calculamos las frecuencias de términos dividiendo los recuentos de palabras por el número total de palabras
    tf = pd.DataFrame(word_count.toarray(), columns=vectorizer.get_feature_names_out())
    tf = tf.div(tf.sum(axis=1), axis=0)

    # Calculamos los valores IDF con la fórmula
    idf_values = np.log((2 / (np.sum(binary_word_count, axis=0) + 1))) + 1

    # Creamos un DataFrame para los valores IDF
    idf_df = pd.DataFrame(
    idf_values, index=vectorizer.get_feature_names_out(), columns=["idf"]
    )

    # Calculamos TF*IDF
    tf_idf_1 = tf.iloc[0] * idf_df["idf"]
    tf_idf_2 = tf.iloc[1] * idf_df["idf"]

    # Calculamos el producto punto 
    dot_product = np.dot(tf_idf_1, tf_idf_2)

    # Calculamos las normales
    norm_1 = np.linalg.norm(tf_idf_1)
    norm_2 = np.linalg.norm(tf_idf_2)

    # Usamos la fórmula para calcular la similitud del coseno
    cosine_similarity = dot_product / (norm_1 * norm_2)

    # Imprimimos las frecuencias de términos, los valores IDF y los valores TF*IDF
    print("\nFrecuencias de términos:\n", tf)
    print("\nValores IDF:\n", idf_df)
    print("\nTF*IDF para Texto 1:\n", tf_idf_1)
    print("\nTF*IDF para Texto 2:\n", tf_idf_2)
    print("\n\n----------------------------------- ")
    print(f"Los códigos tienen un {cosine_similarity*100:.4f} % de similitudes.")
    print("----------------------------------- ")