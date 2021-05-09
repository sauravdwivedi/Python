"""Comma Separated: Write a method that returns a comma-separated
string based on a given list of integers. Each element should be
preceded by the letter 'e' if the number is even, and preceded by
the letter 'o' if the number is odd. For example, if the input
list is (3,44), the output should be 'o3,e44'."""

def com_sep(x):
    """Method to separate integers with comma,
    preceded by 'o' if odd or by 'e' if integer is even"""
    
    y = ""
    for i in range(n-1):
        if x[i] % 2 == 0:
            y = y + "e" + str(x[i]) + ","
        else:
            y = y + "o" + str(x[i]) + ","
    if x[n-1] % 2 == 0:
        y = y + "e" + str(x[n-1])
    else:
        y = y + "o" + str(x[n-1])
    print(y)
    return

if __name__ == '__main__':
    n = int(input("Enter length: "))
    x = []
    for i in range(n):
        x.append(int(input("List entry: ")))
    com_sep(x)
