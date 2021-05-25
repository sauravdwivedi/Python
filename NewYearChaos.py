"""It is New Year's Day and people are in line for the Wonderland
rollercoaster ride. Each person wears a sticker indicating their
initial position in the queue from 1 to n. Any person can bribe the
person directly in front of them to swap positions, but they still
wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a
given queue order. Print the number of bribes, or, if anyone has
bribed more than two people, print Too chaotic.

Example

-: q = [1,2,3,4,5,6,7,8]

If person 5 bribes person 4, the queue will look like this:
1,2,3,5,4,6,7,8. Only 1 bribe is required. Print 1.

-: q = [4,1,2,3]

Person 4 had to bribe 3 people to get to the current position. Print
Too chaotic."""

def new_year_chaos(q):
    """Method to calculate number of bribes"""
    order = [i for i in range(1, len(q)+1)]
    count = 0
    chaos = 0
    for x in order:
        if order.index(x) - q.index(x) > 2:
            chaos = chaos + 1
    while q != order:
        for i in range(len(q)-1):
            if q[i] > q[i+1]:
                q[i+1], q[i] = q[i], q[i+1]
                count = count + 1
    if chaos != 0:
        print("Too chaotic")
    else:
        print(count)
    
if __name__ == '__main__':
    t = int(input("Number of test cases: "))
    for i in range(t):
        q = list(map(int, input("Queue: ").rstrip().split()))
        print(new_year_chaos(q))
        
