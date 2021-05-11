"""The absolute difference is the positive difference between two
values a and b, is written |a-b| or |b-a| and they are equal. If a =
3 and b = 2, |3-2| = |2-3| = 1. Given an array of integers, find the
minimum absolute difference between any two elements in the array."""

def min_abs_diff(a):
    """Method to find minimum absolute difference"""
    abs_diff = []
    for i in range(len(a)-1):
        abs_diff.append(min([abs(a[i]-a[j]) for j in range(i+1, len(a))]))
    return min(abs_diff)

if __name__ == '__main__':
    a = input("Enter array (space separated): ").rstrip().split()
    a = list(map(int, a))
    print("Minimum absolute difference btw two values: ", min_abs_diff(a))

