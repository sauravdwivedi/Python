"""Write a method that checks if there is at least on pair of
numbers which sum equals target. arr=[1, 3, 4] and target=5 result
is true because the pair (1,4) sums to five."""

def two_sum(x, t):
    """Method to check if sum of a pair is equal to target"""
    p = 0
    for i in range(len(x)):
        y = []
        for k in range(len(x)):
            if k != i:
                y.append(x[i])
                y.append(x[k])
                if sum(y) == t:
                    p = p + 1
                else:
                    p = p + 0
                y = []

    if p != 0:
            print("At least one pair has sum equal to target!")
    else:
        print("No pair has sum equal to target")
    return
    
if __name__ == '__main__':
    n = int(input("List length: "))
    print("\t Enter list")
    x = [int(input("Entry: ")) for i in range(n)]
    t = int(input("Enter target: "))
    two_sum(x, t)
