# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 20:56:15 2021

@author: balavenkat
"""

base  = 3
s  = base*base

def pattern(r,c): return (base*(r%base)+r//base+c)%s

from random import sample
def shuffle(s): return sample(s,len(s)) 
rBase = range(base) 
r  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
c  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
n  = shuffle(range(1,base*base+1))

b = [ [n[pattern(r,c)] for c in c] for r in r ]

for line in b: 
    print(line)
    
squares = s*s
empties = squares * 3//4
for p in sample(range(squares),empties):
    b[p//s][p%s] = 0

nize = len(str(s))
for line in b: 
    print("["+"  ".join(f"{n or '.':{nize}}" for n in line)+"]")