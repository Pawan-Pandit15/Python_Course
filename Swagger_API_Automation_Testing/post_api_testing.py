import requests



header = {
    "Accept" : "text/plain",
    "Content-Type" : "application/json"
}

body = {
  "id": 21,
  "title": "Pawan postman practice",
  "dueDate": "2024-04-03T06:32:48.614Z",
  "completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities",headers=header,json=body)
print(response.status_code)
print(response.json())

assert response.status_code == 200
assert response.json()
assert body["id"] ==21































