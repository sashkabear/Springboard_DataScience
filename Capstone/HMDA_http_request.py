# Script to retrieve HMDA (Home Mortgage Disclosure Act) data 

import requests
import json

#Example Request
#Loan Application Records (state = MI,  year 2010, limit to a 100 results, json format)

data = requests.get("https://api.consumerfinance.gov:443/data/hmda/slice/hmda_lar.json?$where=state_abbr+%3D+'MI'+AND+as_of_year+%3D+2010&$limit=100&$offset=0")

#print data
print(data.json())

#Save data
with open('DataSample.txt', 'w') as outfile:
    json.dump(data.json(), outfile)

