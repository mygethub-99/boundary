# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 13:03:13 2018
Check if item in the list
@author: owen
"""
site = "b,e"
sl = "b,c"
def checks(site,sl):
    missing = []
    site = site.split(',')
    sl = sl.split(',')
    count = len(site)
    while count > 0:
        for i in site:
            if i not in sl:
                missing.append(i)
            count = count - 1
        if len(missing) < 1:
                missing.append('none')
            
    return(missing)
