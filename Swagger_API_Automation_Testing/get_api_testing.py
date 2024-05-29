# Simple GET API Calling
import requests

#
# response=requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities")
# print(response.status_code)
# print(response.json())
#
# assert response.status_code == 200


# # Parameter GET API Calling
#
# response=requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/5")
# print(response.status_code)
# print(response.json())
#
# assert response.status_code == 200




# Pass Header in get

head={
    "Accept":"text/plain"    # this is a header
}

response=requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/5",headers=head)
print(response.status_code)
print(response.json())

assert response.status_code == 200













