import requests

header = {
    "Content-Type" : "application/json",
    "Authorization" : "Bearer 1e5d878a972810c62c8495c875ecdf227a272bdc03d4bd47e3d0816ecbb9ceba"
}

json_body = {
    "name":"Pawan Pandit",
    "email":"shrishti_vermaf@bggsfskfslksins-ruggnoflffsdottir.test",
    "gender":"Male",
    "status":"active"
}

url = "https://gorest.co.in/public/v2/users"
response = requests.post(url,headers=header,json=json_body)

print(response.json())
assert response.status_code == 201

#   Check Authorization work or not from get method

get_response = requests.get(url+'/'+str(response.json()["id"]), headers=header)
print(get_response.json())
