# IZVEIDOSIM KONTAKTU APLIKĀCIJU IZMANTOJOT:
# Funkcijas
# Datu struktūras (JSON)
# File I/O
import json

contacts = []

def LoadContacts():
    with open('contacts.json', 'r', encoding='UTF8') as file:        
        data = json.load(file)
        contacts = data

def PrintContacts():
    for contact in contacts:
        print(f"{contact['name']} {contact['surname']} {contact['number']} {contact['email']}")

def AddContact():
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    number = input('Enter number: ')
    email = input('Enter email: ')

    contact = {
        'name': name, 
        'surname': surname, 
        'number': number,
        'email': email
    }

    contacts.append(contact)

def SaveContacts():
    with open('contacts.json', 'w', encoding='UTF8') as file:
        json.dump(contacts, file, indent=4)

LoadContacts()
while(True):
    response = input('A-add new, P-print, E-exit: ')
    if response == 'A':        
        AddContact()
        SaveContacts()
    elif response == 'P':
        PrintContacts()
    elif response == 'E':
        print('Bye bye!')
        break