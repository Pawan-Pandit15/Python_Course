import pytest
import requests

def test_getrequest_validation():

    header = {
        "content-type": "application/json"
    }

    url = "https://reqres.in/api/users/2"

    response = requests.get(url,headers=header)
    assert response.status_code == 200
    print(response.text)