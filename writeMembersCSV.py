import json
import csv
# First Name
# Last Name
# Position
# Email


class Member:
    # Propiedades
    firstName = ""
    lastName = ""
    position = ""
    email = ""

    listaMiembros = []

    # Constructor
    def __init__(self, firstName, lastName, position, email):
        self.firstName = firstName
        self.lastName = lastName
        self.position = position
        self.email = email

    # def addMembersToAList(self, listaMiembros):
        # Crea la lista de objetos con firstName, lastName, position, email

    # def constructMembersList(self, emailMember):
    #     emailMember = emailMember.split("@")
    #     positionEmail = " "
    #     if "alu." in s:
    #         positionEmail = "ALU"
    #     elif "fp." in s:
    #         positionEmail = "FP"
    #     else:
    #         positionEmail = "PROF"

    #     self.firstName = emailMember[0]
    #     self.lastName = " "
    #     self.position = positionEmail
    #     self.email = "@".join(emailMember)

    


def checkPosition(position):
    positionEmail = " "
    if "alu." in position:
        positionEmail = "ALU"
    elif "fp." in position:
        positionEmail = "FP"
    else:
        positionEmail = "PROF"
    
    return positionEmail


def WriteMembersIntoCSV(arrayOfMembers):

    with open("listaMiembrosGophish.csv",mode="w") as csv_file:
        fieldnames = ['First_Name', 'Last_Name', 'Position', 'Email']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for member in arrayOfMembers:
            emailSplited = member.split("@")
            firstName = emailSplited[0]
            lastName = " "
            position = checkPosition(emailSplited[1])
            email = "@".join(emailSplited)
            x = Member(firstName,lastName,position,email)
            writer.writerow({'First_Name': x.firstName, 'Last_Name': x.lastName,'Position': x.position, 'Email': x.email})
    

 

