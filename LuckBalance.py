"""Lena is preparing for an important coding competition that is preceded by
a number of sequential preliminary contests. Initially, her luck balance is
0. She believes in "saving luck", and wants to check her theory. Each contest
is described by two integers, L[i] and T[i]:

- L[i] is the amount of luck associated with a contest. If Lena wins the
contest, her luck balance will decrease by L[i]; if she loses it, her luck
balance will increase by L[i].
- T[i] denotes the contest's importance rating. It's equal to 1 if the
contest is important, and it's equal to 0 if it's unimportant.

If Lena loses no more than k important contests, what is the maximum amount
of luck she can have after competing in all the preliminary contests? This
value may be negative.

Example:

k = 2
L = [5, 1, 4]
T = [1, 2, 0]

Contest        L[i]    T[i]
    1           5       1
    2           1       1
    3           4       0

If Lena loses all of the contests, her will be 5 + 1 + 4 = 10. Since she is
allowed to lose 2 important contests, and there are only 2 important
contests, she can lose all three contests to maximize her luck at 10.

If k = 1, she has to win at least 1 of the 2 important contests. She would
choose to win the lowest value important contest worth 1. Her final luck will
be 5 + 4 - 1 = 8."""

def luck_balance(L, T, k):
    """Method to return maximum amount of luck"""
    count = 1
    max_luck = 0
    l_imp = [L[i] for i in range(len(L)) if T[i] == 1]
    l_imp.sort(reverse = True)
    l_unimp = [L[i] for i in range(len(L)) if T[i] == 0]
    for x in l_imp:
        if count <= k:
            max_luck = max_luck + x
            count = count + 1
        else:
            max_luck = max_luck - x
    for x in l_unimp:
        max_luck = max_luck + x
    return max_luck
    
if __name__ == '__main__':
    k = int(input("Enter k: "))
    L = list(map(int, input("Enter L: ").rstrip().split()))
    T = list(map(int, input("Enter T: ").rstrip().split()))
    print(luck_balance(L, T, k))
