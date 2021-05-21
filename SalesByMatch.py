"""There is a large pile of socks that must be paired by color.
Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.

Example:

n = 7
ar = [1,2,1,2,1,3,2]

There is one pair of color 1 and one of color 2. There are three odd
socks left, one of each color. The number of pairs is 2."""

def sock_merchant(ar):
    """Method to return number of pairs"""
    count = 0
    y = set(ar)
    for x in y:
        c = ar.count(x)
        if c % 2 == 0:
            count = count + int(c/2)
        else:
            count = count + int((c-1)/2)
    return count

if __name__ == '__main__':
    file = open('SalesByMatch_output.txt', 'w')
    ar = list(map(int, input("List: ").rstrip().split()))
    result = sock_merchant(ar)
    file.write(str(result) + '\n')
    print("Output written in SalesByMatch_output.txt")
    file.close()
