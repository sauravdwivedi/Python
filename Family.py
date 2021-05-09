"""The program finds names of all people who have no children
belonging to same family tree for generations"""

import csv

class Family:
    """A class representing people belonging to same family"""
    
    def __init__(self, name, dob, m_name, m_dob, f_name, f_dob):
        """Initializes attributes from given parameters"""
        self.name = name
        self.dob = dob
        self.m_name = m_name
        self.m_dob = m_dob
        self.f_name = f_name
        self.f_dob = f_dob
        
    def identity(self):
        """Method to return unique identity of the person"""
        id = self.name + ", " + self.dob
        return id
        
    def identity_m(self):
        """Method to return unique identity of person's mother"""
        id_m = self.m_name + ", " + self.m_dob
        return id_m
        
    def identity_f(self):
        """Method to return unique identity of person's father"""
        id_f = self.f_name + ", " + self.f_dob
        return id_f

#Empty list of people
p = []
n = int(input("Number of people: "))
print("Enter details of people!")
for i in range(n):
    person = Family(input("Name: "), input("Date of birth: "),
                input("Mother's name: "), input("Mother's dob: "),
                input("Father's name: "), input("Father's dob: "))
    if i < n-1:
        print("Next person!")
    else:
        print("End of entry")
    p.append(person)

#Empty list of people without children
pwc = []
for i in range(n):
    c = 0
    for j in range(n):
        if j != i:
            if (p[i].identity() == p[j].identity_m() or
                    p[i].identity() == p[j].identity_f()):
                c = c + 1
            else:
                c = c + 0
    if c == 0:
        pwc.append(p[i].identity())

print("List of people without children: ", pwc)

print("Output is saved in output.txt file")
with open('family_output.txt', 'w', newline='') as f:
    w = csv.writer(f, delimiter='\n')
    w.writerow(pwc)

