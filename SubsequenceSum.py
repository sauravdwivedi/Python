"""Write a program that can decide whether a sequence of numbers
contains a continuous subsequence having a zero sum."""

import pandas as pd
import re

df = pd.read_csv("subsequenceSum_input.txt", header=None)
m = len(df.index)
z = []
T = int(df.iloc[0,0])
for i in range(2, m, 2):
    x = df.iloc[i,0]
    y = []
    r = 0
    for n in x.split(' '):
        y.append(int(n))
    for k in range(0, len(y)+1):
        for j in range(0, len(y)+1):
            if j > k:
                if sum(y[k:j]) == 0:
                    r = r + 1
    if r != 0:
        z.append("Yes")
    else:
        z.append("No")
with open("subsequenceSum_output.txt", "w") as outfile:
    outfile.write("\n".join(z))
    
print("Output saved in subsequenceSum_output.txt file")
            

    
