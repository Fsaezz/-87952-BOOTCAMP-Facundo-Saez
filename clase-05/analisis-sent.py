from transformers import pipeline #la linea transformer es el nombre de la libreria hf

classifier = pipeline("sentiment-analysis", 
                      model="tabularisai/multilingual-sentiment-analysis") #Classifier es una variable a la que le asigno el llamado de la funcion, en model le paso el modelo a usar 

print(classifier.model)

# Le pregunto a la persona con un input, luego lo paso por mi modelo y printeo el resultado

pregunta = input("Que te parecio?")

result = classifier(pregunta)
print(result)