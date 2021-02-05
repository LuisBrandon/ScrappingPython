import json
x = {
    "firstname":"PepeGarcia",
    "secondName":"",
    "email":"yolo@gmail.com",
    "position":"prof"
}

y = json.dumps(x)

print(y)

emailPrueba = "joseluissalassalguero@iesromerovargas.com"
posicionArroba = emailPrueba.find("@")
emailPrueba = emailPrueba.split('@')

print(emailPrueba[0])

#Así podría comprobar si en la parte del dominio del correo es profesor, alumnado de ESO/BACH o de fp. str.find("alu") str.find("fp") 
s = "This be a string"
if s.find("is") == -1:
    print("No 'is' here!")
else:
    print("Found 'is' in the string.")