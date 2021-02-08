import json

x = {
    "firstname":"PepeGarcia",
    "secondName":"",
    "email":"yolo@gmail.com",
    "position":"prof"
}

y = json.dumps(x)

print(y)

emailPrueba = "correodeprueba@pruebaprueba.com"
emailPrueba = emailPrueba.split('@')

print(f'first name: {emailPrueba[0]}, last name = " " position: {emailPrueba[1]}, email {"@".join(emailPrueba)}')

#Así podría comprobar si en la parte del dominio del correo es profesor, alumnado de ESO/BACH o de fp. str.find("alu") str.find("fp") 
s = "correodeprueba@alu.iesromerovargas.com"
positionEmail = " "
# if s.find("fp."):
#     positionEmail = "FP"
# if s.find("alu."):
#     positionEmail = "ALU"
# elif s.find("fp.") == -1 and s.find("alu.") == -1:
#     positionEmail = "PROF"

if "alu." in s:
    positionEmail = "ALU"
elif "fp." in s:
    positionEmail = "FP"
else:
    positionEmail = "PROF"



print(positionEmail)