"""Given a 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in A is a subset of values with indices falling in this
pattern in A's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in A. An hourglass sum is the sum of an
hourglass' values. Calculate the hourglass sum for every hourglass
in A, then print the maximum hourglass sum. The array will always be
6 by 6."""

import csv

def hour_glass(a):
    """Method to sort hourglasses in array"""
    hourglasses = []
    s = []
    for i in range(0, 4):
        for j in range(0, 4):
            h = []
            h.append(a[i][j])
            h.append(a[i][j+1])
            h.append(a[i][j+2])
            h.append(a[i+1][j+1])
            h.append(a[i+2][j])
            h.append(a[i+2][j+1])
            h.append(a[i+2][j+2])
            hourglasses.append(h)
            s.append(sum(h))
    
    hh = {}
    for i in range(1, len(hourglasses)):
        if sum(hourglasses[i]) > sum(hourglasses[i-1]):
            hh[i] = sum(hourglasses[i])

    hh = max(hh, key=hh.get)

    print("\t The given array: \n")
    print(a)
    print("\t The 16 hourglass are: \n")
    for hg in hourglasses:
        print(hg)
    print(f"\n\t The 16 hourglass sums are: {s}")
    print(f"\n\t Hourglass with highest sum is {hourglasses[hh]} with sum {sum(hourglasses[hh])}")

    with open('hourglasses_output.txt', 'w', newline='') as f:
        w = csv.writer(f, delimiter='\n')
        z = csv.writer(f, delimiter=' ')
        w.writerow(hourglasses)
        z.writerow(hourglasses[hh])
    return

if __name__ == '__main__':
    with open('hourglasses_input.txt') as file:
        lines = file.readlines()
        a = [list(map(int, line.rstrip().split())) for line in lines]
    hour_glass(a)
