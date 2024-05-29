# This is simple request in paython file

# import requests
#
# header = {
#     "content type" : "application-json"
# }
#
# json_payload = {
#     "name": "Pawan",
#     "job": "Software Testing"
# }
#
# url = "https://reqres.in/api/users"
#
# response = requests.post(url,headers=header,json=json_payload)
# print(response.status_code)
# print(response.json())

#--------------------------------------------------------------------------

# This request is passing payload in json file

import requests
import json

header = {
    "content type" : "application-json"
}

# Here json code in other json file ( user_json ) this is file name

json_file = open ("./user_json")
json_payload = json.load(json_file)

url = "https://reqres.in/api/users"


response = requests.post(url,headers=header,json=json_payload)
print(response.status_code)
print(response.text)