"""A staircase of size (say n = 5) is combination of white spaces and #:

    #
    ##
    ###
    ####
    #####
    
where number of #'s at bottom is equal to n. Whrite a method to print
a staircase for a given integer n as input."""

def stair_case(stair_case_size: int) -> str:
    stair_case: str = ""
    for i in range(1, stair_case_size + 1, 1):
        for j in range(stair_case_size - i):
            stair_case += " "
        for k in range(i):
            stair_case += "#"
        stair_case += "\n"
    return stair_case

def main() -> None:
    stair_case_size: int = int(input("Size of staircase: "))
    result: str = stair_case(stair_case_size)
    print(result)
    
if __name__ == '__main__':
    main()
