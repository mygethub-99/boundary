# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 20:11:16 2018
Multiband cross check
@author: owen
"""
import check_member as check

l = [["Mobile",1097,	"E2,E1,F2,F1","a"	,"B,C","I2,I1,J3,J4,J5,J6",13805304,"D2,D1,F2,F1,C6,C7","none","C","C2,C1,F3,F4,F5,F6,J3,J4,J5,J6"],
     ["East Carroll",22035,"D2,D1,E2,E1,C9,C10,C11","b","B,C","F3,F4,F5,F6,I2,I1,J3,J4,J5,J6",14511289,"B6,B7,B8,B9,B10,B11,E2,E1,C","none","B,C","J3,J4,J5,J6"]]
output = [] #collects audit returned from check_member.py
#with open('shortlist2.txt') as f:
    #next(f)
x = 6
y = 2 
for i in l:
    line = l
    count = 4
    holding = []
    holding.append(i[1])
    holding.append(i[5])
    while count > 0:
        for val in line:
            missing = check.checks(val[x],val[y])
            holding.append(missing)
            x = x+1
            y = y+1
            count = count - 1
output.append(holding)
