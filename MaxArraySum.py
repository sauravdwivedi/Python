"""Given an array of integers, find the subset of non-adjacent
elements with the maximum sum. Calculate the sum of that subset. It
is possible that the maximum sum is 0, the case when all elements
are negative."""

def max_sum_array(a):
    """Method to calculate maximum sum in sub arrays"""
    id_one = lambda i: [a[i+2*j] for j in range(len(a)) if i + 2*j < len(a)]
    y = [id_one(i) for i in range(len(a)) if len(id_one(i)) >= 2]
        
    for i in range(len(a)):
        for j in range(len(a)):
            if i+j+2 < len(a):
                z = [a[i]]
                z.append(a[i+j+2])
                y.append(z)
    total = [sum(x) for x in y]
    return max(total)

if __name__ == '__main__':
    a = list(map(int, input("Enter array (space separated): ").split()))
    print(max_sum_array(a))
