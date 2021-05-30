"""You are given a string containing characters A and B only. Your
task is to change it into a string such that there are no matching
adjacent characters. To do this, you are allowed to delete zero or
more characters in the string.

Your task is to find the minimum number of required deletions.

Example:
s = AABAAB

Remove an A at positions 0 and 3 to make s = ABAB in 2 deletions."""

def alt_char(s):
    """Method to find min no. of deletions"""
    x = s[0]
    for i in range(len(s)-1):
        if s[i+1] != s[i]:
            x = x + s[i+1]
    deletions = len(s) - len(x)
    return deletions

if __name__ == '__main__':
    s = input("Enter string: ")
    print(alt_char(s))
