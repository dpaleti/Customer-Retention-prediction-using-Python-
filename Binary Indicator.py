import sys
import json
from datetime import datetime

tot_cntr = 0
ret_cntr = 0

with open('data.json') as data_file:    
    data = json.load(data_file)

for i in range(len(data)):
   tot_cntr += 1
   d2 = data[i]["last_trip_date"]
   d1 = '2014-07-01'
   d1 = datetime.strptime(d1, "%Y-%m-%d")
   d2 = datetime.strptime(d2, "%Y-%m-%d")

   if ((d1 - d2).days) <= 30:
       ret_cntr += 1
       data[i]['Active'] = '1'
   else:
       data[i]['Active'] = '0' 
   		
ret_per =(ret_cntr/tot_cntr)*100 

with open('data-uber.txt', 'w') as outfile:
    json.dump(data, outfile)

