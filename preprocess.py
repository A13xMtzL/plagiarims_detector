import re

#Procesamos la información de estos textos cambiando todo a minusculas, separando todo por oraciones y borrando caracteres especiales

def preprocessing(file, test = False):
    
    if not test:
        # Reading files
        with open(file, "r", encoding="utf_8") as document:
            document = document.read()
    else:
        document = file

    # Turn to lowercase
    filtered_doc = document.lower()

    # Split per sentence
    filtered_doc = filtered_doc.split(".")

    # Remove empty strings
    filtered_doc = list(filter(None, filtered_doc))

    # Remove elements that are less than 2 characters long
    filtered_doc = [x for x in filtered_doc if len(x) > 2]

    # Define the pattern to match everything that is a special character
    pattern = r"[^\w\s]"

    # Remove special characters
    for i in range(len(filtered_doc)):
        filtered_doc[i] = re.sub(pattern, "", filtered_doc[i])
    
    # Return preprocessed file as a string
    return filtered_doc
