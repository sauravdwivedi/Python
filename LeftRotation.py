"""A left rotation operation on an array shifts each of the array's
elements 1 unit to the left. For example, if 2 left rotations are
performed on array [1,2,3,4,5], then the array would become
[3,4,5,1,2]. Note that the lowest index item moves to the highest
index in a rotation. This is called a circular array.

Given an array a of n integers and a number, d, perform d left
rotations on the array. Return the updated array to be printed as a
single line of space-separated integers."""

def left_rot(a, d):
    """Method to make d left-rotations for array a"""
    if d <= len(a):
        x = [a[-len(a)+d+j] for j in range(len(a))]
    else:
        d = d % n
        x = [a[-len(a)+d+j] for j in range(len(a))]
    result = map(str, x)
    print(' '.join(result))
    return result

if __name__ == '__main__':
    n = int(input("Length of array: "))
    a = []
    for i in range(n):
        a.append(int(input(f"{i}th entry: ")))
    d = int(input("Enter no. of rotations: "))
    left_rot(a, d)
#    import timeit
#    print(timeit.timeit('left_rot(a, d)', globals=globals()))
