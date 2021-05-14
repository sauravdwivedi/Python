"""A bracket is considered to be any one of the following
characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening
bracket (i.e., (, [, or {) occurs to the left of a closing bracket
(i.e., ), ], or }) of the exact same type. There are three types of
matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets
it encloses are not matched. For example, {[(])} is not balanced
because the contents in between { and } are not balanced. The pair
of square brackets encloses a single, unbalanced opening bracket, (,
and the pair of parentheses encloses a single, unbalanced closing
square bracket, ].

By this logic, we say a sequence of brackets is balanced if the
following conditions are met:

1) It contains no unmatched brackets.
2) The subset of brackets enclosed within the confines of a matched
pair of brackets is also a matched pair of brackets.

Given n strings of brackets, determine whether each sequence of
brackets is balanced. If a string is balanced, return YES.
Otherwise, return NO."""

def bal_bracket(s):
    """Method to identify if a string of brackets is balanced"""
    # list of indexes of balanced subbrackets in string
    list_of_bsb = [i for i in range(len(s)) if (
        (s[i] == "(" and s[i+1] == ")")
        or (s[i] == "[" and s[i+1] == "]")
        or (s[i] == "{" and s[i+1] == "}"))]
    
    y = 0
    for x in list_of_bsb:
            s = s[:x-y] + s[x+2-y:]
            y = y + 2
            
    while len(s) >= 1:
        if ((s[0] == "(" and s[len(s)-1] == ")")
            or (s[0] == "[" and s[len(s)-1] == "]")
            or (s[0] == "{" and s[len(s)-1] == "}")):
            s = s[1:len(s)-1]
        else:
            break
            
    if len(s) == 0:
        result = "YES"
    else:
        result = "NO"
    return result

if __name__ == '__main__':
    n = int(input("No. of Strings: "))
    for i in range(n):
        s = input("String of brackets: ")
        print(bal_bracket(s))
