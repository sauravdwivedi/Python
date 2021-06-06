"""A queue is an abstract data type that maintains the order in which
elements were added to it, allowing the oldest elements to be removed from
the front and new elements to be added to the rear. This is called a
First-In-First-Out (FIFO) data structure because the first element added to
the queue (i.e., the one that has been waiting the longest) is always the
first one to be removed.

A basic queue has the following operations:

-> Enqueue: add a new element to the end of the queue.
-> Dequeue: remove the element from the front of the queue and return it.

In this challenge, you must first implement a queue using two stacks. Then
process q queries, where each query is one of the following 3 types:

Type 1) Enqueue element x into the end of the queue.
Type 2) Dequeue the element at the front of the queue.
Type 3) Print the element at the front of the queue.

Input Format: The first line contains a single integer, q, the number of
queries. Each of the next q lines contains a single query in the form
described in the problem statement above. All queries start with an integer
denoting the query types (e.g., 1, 2, 3), but only query type '1' is followed
by an additional space-separated value, x, denoting the value to be
enqueued."""

class MyQueue:
    def __init__(self, values):
        self.values = values
    def put(self, enqueue, y):
        y.append(enqueue)
    def pop(self, y):
        del y[0]
    def peek(self, y):
        if len(y) > 0:
            front_elem = y[0]
        else:
            front_elem = y
        return front_elem
    
if __name__ == '__main__':
    q = int(input("Enter number of querries: "))
    y = []
    for i in range(q):
        values = list(map(int, input("Enter queue: ").split()))
        queue = MyQueue(values)
        if values[0] == 1:
            queue.put(values[1], y)
        elif values[0] == 2:
            queue.pop(y)
        else:
            print(queue.peek(y))
