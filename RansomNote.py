""" Harold is a kidnapper who wrote a ransom note, but now he is
worried it will be traced back to him through his handwriting. He
found a magazine and wants to know if he can cut out whole words
from it and use them to create an untraceable replica of his ransom
note. The words in his note are case-sensitive and he must use only
whole words available in the magazine. He cannot use substrings or
concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note,
print Yes if he can replicate his ransom note exactly using whole
words from the magazine; otherwise, print No."""

def check_magazine(magazine, note):
    """Method to check if note can be made from magazine words"""
    p = 0
    for i in range(len(note)):
        if note[i] in magazine:
            p = p + 0
            magazine.remove(note[i])
        else:
            p = p + 1
    if p == 0:
        print("Yes")
    else:
        print("No")
    return
    
if __name__ == '__main__':
    lines = []
    with open('ransomnote_input.txt') as file:
        contents = file.readlines()
        for line in contents:
            lines.append(line.rstrip().split())
        
    m = int(lines[0][0])
    n = int(lines[0][1])
    
    magazine = lines[1]
    note = lines[2]
    
    check_magazine(magazine, note)
