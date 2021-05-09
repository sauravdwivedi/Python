"""Write an algorithm that process a given set of ip ranges by
removing their intersections and returning a set of mutually
exclusive ip ranges."""

from netaddr import *
import re
import pandas as pd
import numpy as np
import csv

def IP_address(x):
    """Method to sort mutually exclusive IP addresses"""
    print("\n\t Mutually exclusive IP ranges: ")
    y = []
    j = 0
    n = int(len(x)/4)
    for i in range (0,n):
        r1 = IPRange(x[i+j], x[i+j+1])
        r2 = IPRange(x[i+j+2], x[i+j+3])
        j = j+3
        s1 = IPSet()
        s2 = IPSet()
        s1.add(r1)
        s2.add(r2)
        c1 = s1 - (s1 & s2)
        c2 = s2 - (s1 & s2)
        #print(list(c1.iter_ipranges()))
        #print(list(c2.iter_ipranges()))
        y.append(list(c1.iter_ipranges()))
        y.append(list(c2.iter_ipranges()))
    print(y)
    with open("ip_output.txt", 'w', newline='') as f:
        w = csv.writer(f, delimiter='\n')
        z = csv.writer(f, delimiter=' ')
        w.writerow(y)
    return
    
if __name__ == '__main__':
    with open('ip_input.txt') as fh:
        fstring = fh.readlines()
        pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    x = []
    for line in fstring:
        x.append(pattern.search(line)[0])
    print("\n\t Given IP ranges: ")
    print(x)
    IP_address(x)
