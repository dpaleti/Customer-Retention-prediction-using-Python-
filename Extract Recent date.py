import sys
import json
from datetime import datetime


tot_cntr = 0
ret_cntr = 0
lest = []
var = 0
with open('data.json') as data_file:    
    data = json.load(data_file)

for i in range(len(data)):
   tot_cntr += 1
   d2 = data[i]["last_trip_date"]
   #d1 = sys.argv[1]
   d1 = '2015-05-24' #some arbitary date in 2015
   d1 = datetime.strptime(d1, "%Y-%m-%d")
   d2 = datetime.strptime(d2, "%Y-%m-%d")
   lest.append((d1 - d2).days)

var = lest.index(min(lest))
print(data[var]["last_trip_date"])


