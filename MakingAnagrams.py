"""A student is taking a cryptography class and has found anagrams
to be very useful. Two strings are anagrams of each other if the
first string's letters can be rearranged to form the second string.
In other words, both strings must contain the same exact letters in
the same exact frequency. For example, bacdc and dcbac are anagrams,
but bacdc and dcbad are not.

The student decides on an encryption scheme that involves two large
strings. The encryption is dependent on the minimum number of
character deletions required to make the two strings anagrams.
Determine this number.

Given two strings, a and a, that may or may not be of the same
length, determine the minimum number of character deletions required
to make a and b anagrams. Any characters can be deleted from either
of the strings."""

def make_anagram(a, b):
    """Method to make anagrams"""
    c = 0
    s = ""
    n = len(a) + len(b)
    for x in a:
        if x in b:
            c = c + 1
            s = s + x
            b = b.replace(x," ",1)
    print(c, b)
    return n-2*c
    
if __name__ == '__main__':
    a = [input("Enter String a: ")]
    b = input("Enter String b: ")
    print(make_anagram(a, b))
