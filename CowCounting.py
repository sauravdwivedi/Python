"""
Cows are sitting in field blocks described by their x and y coordinates:

Cows = [[1, 0], [3, 0], [0, 3], [1, 4], [2, 4], [3, 3], [4, 3], [4, 4]]:

 ---x-->
|
y
!
 __ __ __ __ __
|__|_#|__|_#|__|
|__|__|__|__|__|
|__|__|__|__|__|
|_#|__|__|_#|__|
|__|_#|_#|_#|_#|

A cow has a nearest neighbor if it has another cow sitting next left, right, 
up, or down to it, not sittng diagonally: cows [0, 1] and [0, 0] are nearest
neighbors, while cows [0, 1] and [1, 0] are not!

Return number of cows with at least one nearest neighbor.
"""

def cow_counting(cows, num_cows):
    """Method that returns number of cows with at least one nearest neighbor"""
    cow_x = {}
    cow_y = {}
    neighbor = 0
    for i in range(num_cows):
        cow_x[i] = cows[i][0]
        cow_y[i] = cows[i][1]
    for i in range(num_cows):
        count = 0
        for j in range(num_cows):
            if (
                (((cow_x[j] == cow_x[i] + 1) 
                    or (cow_x[j] == cow_x[i] - 1))
                    and (cow_y[j] == cow_y[i]))
                or 
                ((((cow_y[j] == cow_y[i] + 1) 
                    or (cow_y[j] == cow_y[i] - 1))
                    and (cow_x[j] == cow_x[i]))
                )
                ):
                count += 1  
        if count != 0:
            neighbor += 1      
    return neighbor
     
if __name__ == "__main__":
    input_file = "CowCounting_input.txt"
    try:
        with open(input_file) as file:
            lines = file.readlines()
            cows = [list(map(int, line.rstrip().split())) for line in lines]
        num_cows = len(cows)
    except FileNotFoundError:
        print(f"File {input_file} not found!")
    else:
        result = cow_counting(cows, num_cows)
        print(f"Number of cows with at least one nearest neighbor is {result}!")
