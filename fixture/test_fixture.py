import pytest


# @pytest.fixture()
# def setup():                  # this file comment because fixture call for conftest file
#     print("I will execute first")
#     yield      # here yield word hold execution
#     print("I will execute last")


# def test_fixture(setup):
#     print("I will execute second")

#-----------------------------------------------------------------------------------
# If I have multiple testcase then we can wrap the fixture in one class


# @pytest.mark.usefixtures("setup")
# class Testdemo:           # here class name shpuld be start from ( Test ) word
#
#     def test_fixture1(self):
#         print("fixture method 1")
#
#     def test_fixture2(self):
#         print("fixture method 2")
#
#     def test_fixture3(self):
#         print("fixture method 3")


# -----------------------------------------------------------------------------------

@pytest.mark.usefixtures("setup")
class Testdemo:

    def test_fixture1(self):
        print("fixture method 1")

    def test_fixture2(self):
        print("fixture method 2")

    def test_fixture3(self):
        print("fixture method 3")








