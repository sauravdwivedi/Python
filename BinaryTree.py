"""A binary tree is strict when all nodes have either two or zero
child nodes. Write a method that checks if a binary tree is
strict."""

def bin_tree(z):
    """Method to check if tree is strict binary"""
    x = 0
    if len(z) == 2 or len(z) == 0:
        x = x + 0
    else:
        x = x + 1
    for i in range(len(z)):
        if len(z[i]) == 2 or len(z[i]) == 0:
            x = x + 0
        else:
            x = x + 1
    print(f"The tree: {z}")
    if x == 0:
        print("Tree is strict binary!")
    else:
        print("Tree is NOT strict binary!")
    return

if __name__ == '__main__':
    z = {}
    m = int(input("Number of branches in first level node: "))
    for i in range(m):
        z[i] = {}
        p = int(input("Number of branches in second level nodes: "))
        for j in range(p):
            z[i][j] = {}
    bin_tree(z)
