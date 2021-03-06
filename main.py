"""
Created on Thu Sep 27 20:11:16 2018
Multiband cross check
@author: owen
"""
from functools import reduce
import check_member as check
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

output = [] #collects audit returned from check_member.py

#Request file name from user and opens file
fn = input('Enter file name(hbinput or lbinput): ')
fn1 = fn+'.txt'
with open(fn1) as f:
    next(f)


#Group SpectrumLandscape and cell site, by band, for comparison     
    for i in f:
        i = i.replace('\n','')
        i = i.split('\t')
        count = 4
        holding = []
        holding.append(i[1]),holding.append(i[6]),holding.append(i[7]),\
        holding.append(i[8])        
        f1900 = [i[9],i[2]]
        f850 = [i[11],i[3]]
        f700 = [i[10],i[4]]
        faws = [i[12],i[5]]
        combine = [f1900,f850,f700,faws]

#Loop through each combine list, one band at a time, and appends holding with results       
        while count > 0:
            for val in combine:
                checkup = check.checks(val[0],val[1])
                outs = '-'.join(checkup)
                holding.append(outs)
                count = count - 1
            output.append(holding)
fn = fn+'output.csv'        
with open(fn, 'w') as fs:
    fs.write('FIPS,''FA,''Lat,' 'Long,' '1900_Offender,' '850_Offender,' '700_Offender,' 'AWSOffeder')
    fs.write('\n')
    for i in output:
        i = str(reduce(lambda x,y:x+","+y,i))
        i = i.replace('"', '')
        fs.write("{}\n".format(i))
fs.close()

#Open output file and then geocode it with Point data for plotting
data=pd.read_csv(fn)
data['coordinates']=[Point(xy) for xy in zip(data['Long'], data['Lat'])]
gdata = gpd.GeoDataFrame(data, geometry='coordinates')
gdata.crs={'init':'epsg:4326'}
