import json

f = open("cities.json")

data = json.load(f)

d1 = {}
for city in data:
    for company in city["company"]:
        company_name = company["name"]
        if d1.get(company_name) != None:
            if city["city"] != d1[company_name][-1]:
                d1[company_name].append(city["city"])
            else:
                 continue
        else:
            d1[company_name] = [city["city"]]

d1           
