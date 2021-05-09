"""Given a list of strings, write a method that returns a list of
all strings that start with the letter 'a' (lower case) and have
exactly 3 letters."""

def fil_string(n):
    """Method to filter strings with first element 'a'
    and length 3"""
    y = []
    x = []
    for i in range(0, n):
        print("\t Enter string: ")
        x.append(input())
    for i in range(0, n):
        if len(x[i]) == 3 and x[i][0] == 'a':
            y.append(x[i])
     print("List of strings with first eliment 'a' and length 3")
     print(y)
     return

if __name__ == '__main__':
    print("\t Enter number of Strings: ")
    n = int(input())
    fil_string(n)
