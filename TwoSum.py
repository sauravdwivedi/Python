"""Write a method that checks if there is at least one pair of
numbers in a list of numbers, which has sum equal to target. 
Given arr = [1, 3, 4] and target = 5, result is true because 
the pair (1,4) sums to 4."""

def two_sum(list_of_nums, target_num):
    """Method to check if sum of a pair is equal to target"""
    result = False
    for p in list_of_nums:
    	for q in list_of_nums:
     	    if (p != q) and (p + q == target_num):
    	        result = True
    if result:
    	return "At least one pair has sum equal to target!"
    else:
    	return "No pair has sum equal to target"

if __name__ == "__main__":    
    list_of_nums = list(map(int, input("Enter space separated list of numbers: ")
        .strip().split(" ")))
    target_num = int(input("Enter target integer: "))
    print(two_sum(list_of_nums, target_num))
