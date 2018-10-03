# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 20:11:16 2018
Multiband cross check
@author: owen
"""
import check_member as check
output = [] #collects audit returned from check_member.py
with open('query5mile.txt') as f:
    next(f)
     
    for i in f:
        i = i.split('\t')
        count = 4
        holding = []
        holding.append(i[1]), holding.append(i[6])
        f1900 = [i[7],i[2]]
        f850 = [i[8],i[3]]
        f700 = [i[9],i[4]]
        faws = [i[10],i[5]]
        combine = [f1900,f850,f700,faws]
        
        while count > 0:
            for val in combine:
                checkup = check.checks(val[0],val[1])
                holding.append(checkup)
                count = count - 1
            output.append(holding)
