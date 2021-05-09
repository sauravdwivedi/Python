"""Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }
}

Given an array of integers, sort the array in ascending order using
the Bubble Sort algorithm above. Once sorted, print the following
three lines:

Array is sorted in numSwaps swaps., where numSwaps is the number of
swaps that took place.

First Element: firstElement, where firstElement is the first element
in the sorted array.

Last Element: lastElement, where lastElement is the last element in
the sorted array.

Hint: To complete this challenge, you must add a variable that keeps
a running tally of all swaps that occur during execution."""

def count_swaps(a):
    """Function swaps items and counts number of swaps"""
    count = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]
                count = count + 1
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")
    return

if __name__ == '__main__':
    n = int(input("Number of elements: ").strip())
    a = list(map(int, input("Array (space separated): ").rstrip().split()))
    count_swaps(a)
