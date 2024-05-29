import pytest


# @pytest.fixture()
# def setup():
#     print("I will execute first")
#     yield      # here yield word hold execution
#     print("I will execute last")


@pytest.fixture(scope="class")   # this is only use when use class particular one function to fixture see ( test_fixture.py ) file
def setup():
    print("I will execute first")
    yield      # here yield word hold execution
    print("I will execute last")


@pytest.fixture()  # this is only use for when data load and receiving data from fixture
def data_load():
    print("user profile data created")
    return ["Pawan","Pandit","pawan123@gmail.com"]



# this is use when ren multiple time and collect data each time one data
@pytest.fixture(params=["chrome","firefox","internet Manager"])
def cross_browser(request):
    return request.param




# this is only use when I have multiple data and every time we run to pass is and password
# so we can group data from list and pass index to fetch particular data
@pytest.fixture(params=[("chrome","pawan_chrome","pandit_chrome"),("firefox","kajal_chrome"),("internet Manager","annu")])
def cross_browser1(request):
    return request.param