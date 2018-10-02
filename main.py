# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 20:11:16 2018
Multiband cross check
@author: owen
"""
import check_member as check

l = [["1051","1002","b,c","a","b1,b2,b3,b4","j1,j2,l1","b,c","b","b1,b2,b3,b4,f1","j3,l1"],
     ["1052","1002","b,c","a","b1,b2,b3,b4","j1,j2,l1","b,c","b","b1,b2,b3,b4","j3,l1"]]
output = [] #collects audit returned from check_member.py
with open('shortlist2.txt') as f:
    next(f)
x = 6
y = 2 
for i in l:
    line = l
    count = 4
    holding = []
    holding.append(i[1])
    while count > 0:
        for val in line:
            missing = check.checks(val[x],val[y])
            holding.append(missing)
            x = x+1
            y = y+1
            count = count - 1
            output.append(holding)
