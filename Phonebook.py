"""This program takes details of peopble (Name, Phone number etc)
and makes a phonebook!"""

import csv
import pandas as pd

class Dir:
    """The calss Dir stores phonebook"""
    
    def __init__(d, firstname, surname, number):
        d.f = firstname
        d.s = surname
        d.n = number
        
    def desc(d):
        entry = f"{d.f} {d.s}, Number: {d.n}"
        return entry.title()

print(
    "\t Following information is already saved in Phonebook_output.txt: \n")
file = 'phonebook_output.txt'
with open(file) as f:
    if file == 'phonebook_output.txt':
        c = f.readlines()
    else:
        print("File does not exist!")
    
for lines in c:
    print(lines.rstrip())
    
x = []
y = 0
print("\n\t This program creates a contact book. Please enter requested details! \n")
while y != 'exit':
    f = str(input("Enter Firstname: "))
    if f.isalnum() == True and f.isalpha() == False:
        f = input("Please enter only letters: ")
    s = str(input("Enter Surname: "))
    if s.isalnum() == True and s.isalpha() == False:
        s = input("Please enter only letters: ")
    n = input("Enter telephone number: ")
    if n.isnumeric() == False:
        n = input("Please enter only numbers: ")
    e1 = Dir(f, s, n)
    x.append(e1.desc())
    print("Type any key if you want to enter next person's information or type exit to quit: ")
    y = input()
print("Output saved in 'phonebook_output.csv' Goodbye!")

with open(file, 'a', newline='') as f:
    w = csv.writer(f, delimiter='\n')
    z = csv.writer(f, delimiter=' ')
    w.writerow(x)
