"""Each time Sunny and Johnny take a trip to the Ice Cream Parlor,
they pool their money to buy ice cream. On any given day, the parlor
offers a line of flavors. Each flavor has a cost associated with it.

Given the value of money and the cost of each flavor for t trips to
the Ice Cream Parlor, help Sunny and Johnny choose two distinct
flavors such that they spend their entire pool of money during each
visit. ID numbers are the 1-based index number associated with a
cost. For each trip to the parlor, print the ID numbers for the two
types of ice cream that Sunny and Johnny purchase as two
space-separated integers on a new line. You must print the smaller
ID first and the larger ID second."""

def ice_cream(cost, money):
    """Method to determine flavors"""
    d = lambda i: cost[i-1]
    z = [f"{i} {j}" for i in range(1, len(cost)) for j in range(i+1, len(cost)+1) if d(i) + d(j) == money]
    z.sort()
    return ' '.join(map(str, z))
    
if __name__ == '__main__':
    with open('icecreamparlor_input.txt') as file:
        lines = file.readlines()
        x = [list(map(int, line.rstrip().split())) for line in lines]
    t = x[0][0]
    j = 0
    for i in range(t):
        money = x[1+j][0]
        n = x[2+j][0]
        cost = x[3+j]
        j = j + 3
        print(f"ID numbers of costs: {ice_cream(cost, money)}")


