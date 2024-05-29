import requests

header = {
    "Accept" : "text/plain",
    "Content-Type" : "application/json"
}
body_json = {
  "id": 201,
  "title": "Pawan id updated",
  "dueDate": "2024-04-03T10:24:00.222Z",
  "completed": True
}

response = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/15",headers=header,json=body_json)
print(response.status_code)
print(response.json())
print(body_json["title"])

assert response.status_code == 200
