"""This program calculates MC in wood for given weight and oven dry
weight"""

def moisture_content(x, y):
    """Method to calculate MC in wood"""
    z = 100 * (y - x) / x
    m = f"MC is {z} %"
    print(m)
    return
 
if __name__ == '__main__':
    moisture_content(
        float(input('Oven dry weight: ')),
        float(input('Given weight: '))
        )

