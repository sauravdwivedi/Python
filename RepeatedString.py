"""There is a string, s, of lowercase English letters that is repeated
infinitely many times. Given an integer, n, find and print the number of
letter a's in the first n letters of the infinite string.

Example:

s = 'abcac'
n = 10

The substring we consider is abcacabcac, the first 10 characters of the
infinite string. There are 4 occurrences of a in the substring."""

def repeated_string(s, n):
    """Method to return number of occurences of 'a' in first n characters"""
    remainder = n % len(s)
    ratio = int(n / len(s))
    result = s[:remainder].count('a') + ratio * s.count('a')
    return result

if __name__ == '__main__':
    s = input("Enter string: ")
    n = int(input("Enter integer: "))
    result = repeated_string(s, n)
    print(result)
