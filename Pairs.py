"""Given an array of integers and a target value, determine the number of
pairs of array elements that have a difference equal to the target value.

Example:
k = 1
arr = [1,2,3,4]

There are three values that differ by k=1: 2-1=1, 3-2=1, and 4-3=1. Return
3."""

def pairs(k, arr):
    """Method to find number of pairs that have diff equal to target"""
    arr = set(arr)
    num_of_pairs = [1 for x in arr if x+k in arr]
    return len(num_of_pairs)

if __name__ == '__main__':
    k = int(input("Enter target value: "))
    arr = list(map(int, input("Enter array of integers: ")\
    .rstrip().split(" ")))
    result = pairs(k, arr)
    print(f"Number of pairs with difference {k} are {result}")
