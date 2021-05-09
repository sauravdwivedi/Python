"""This program models a restaurant, and prints details about
restaurants"""

class Res:
    """Class to mode a restaurant"""
    
    def __init__(r, name, cuisine):
        r.n = name
        r.c = cuisine
        def isopen(r):
        print(f"{r.n} is open!")
        
    def has(r):
        print(f"{r.n} has {r.c}")

r1 = Res("MacDonalds","Burger")
r2 = Res("Indiska","Paneer")

print(f"Name of first restaurant: {r1.n}")
print(f"Cuisine in second restaurant: {r2.c}")
print(f"{r1.isopen()}")
print(f"{r2.has()}")
