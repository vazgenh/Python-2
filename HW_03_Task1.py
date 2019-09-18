import json
f = open("cities.json")
data = json.load(f)

# My best city will be with the most Irish bars and with no gas/oil companies.

""" 1. First of all, we should find a city with the most Irish bars (but here we just created a dict where all cities are there
either there are cities with the most Irish bars or not.) Afterward, we will find it with the help of maxvalue.
"""
d={}
for city in data:
    d[city["city"]]=0
    for bars in city["bars"]:
        if bars["chain"]=='Irish':
            d[city["city"]]+=1

# 2. Here we gonna delete cities with gas/oil companies.

for city in data:
    for company in city["company"]:
        if company["industry"]=="Gas/Oil":
            del d[city["city"]]
            break
# 3. In the first one we found cities where could be Irish bars or maybe couldn't, but we need to find cities with the most Irish bars (without gas/oil)

maxvalue=0
bestcity=""
for city in d.keys():
    if d[city]>maxvalue:
        maxvalue=d[city]
        bestcity=city
    elif d[city]==maxvalue:
        bestcity+= ' '+city
        
print(bestcity)

# So the output will be TUSKAHOMA CATHERINE which are the best cities in the concept of not having oil/gas companies and having the most Irish bars.
