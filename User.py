"""This program models users, and provides their details"""

class User:
    """A class that defines a user"""
    
    def __init__(u, name, surname, age, tel):
        """u.n takes parameter name and makes it a variable n"""
        u.n = name
        u.s = surname
        u.a = age
        u.t = tel
        
    def desc(u):
        print(f"Details of user: {u.n} {u.s} ({u.a}), Number: {u.t}")
   
    def greet(u):
        print(f"{u.n} is welcome!")

u1 = User("Saurav", "Dwivedi", 30, "+461234567")
u2 = User("Albert", "Einstein", 45, "+445245453")

print(f"{u1.n} is {u1.a} years old!")
print(f"{u1.desc()}")
print(f"{u2.desc()}")
print(f"\n{u1.greet()}")
print(f"{u2.greet()}")


