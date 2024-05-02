import tensorflow_hub as hub

# Universal Sentence Encoder
module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
model = hub.load(module_url)
print ("module %s loaded" % module_url)

# Función para correr el modelo
def embed(input):
    return model(input)