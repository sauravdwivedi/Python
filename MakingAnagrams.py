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
    count = 0
    len_bothstring = len(a) + len(b)
    for x in a:
        if x in b:
            count = count + 1
            b = b.replace(x," ",1)
    print(f"Minimum number of character deletions required \
    \n to make a and b anagrams: {len_bothstring - 2*count}")
    return
    
if __name__ == '__main__':
    a = [input("Enter String a: ")]
    b = input("Enter String b: ")
    make_anagram(a, b)
