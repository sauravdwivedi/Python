"""A class to describe cars"""

class Car:
    """A class to model cars"""
    
    def __init__(c, brand, model, year):
        """Initialize attributes to describe a car."""
        c.b = brand
        c.m = model
        c.y = year
        c.r = 0
        
    def desc(d):
        """Return a neatly formatted descriptive name."""
        long_name = f"{d.y} {d.b} {d.m}"
        return long_name.title()
        
    def meter(m):
        print(f"This car has {m.r} miles on it.")
        
    def um(u, mileage):
        if mileage >= u.r:
            u.r = mileage
        else:
            print("You can't roll back an odometer!")
            
    def mi(i, inc):
        if inc >= 0:
            i.r = i.r + inc
        else:
            print("You can't roll back an odometer!")

if __name__ =='__main__':
    my_new_car = Car('audi', 'a4', 2019)
    my_new_car.meter()
    my_new_car.um(int(input("Enter mileage: ")))
    my_new_car.meter()
    my_new_car.mi(int(input("Increase mileage by: ")))
    my_new_car.meter()
    my_new_car.desc()

