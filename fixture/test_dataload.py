import pytest

@pytest.mark.usefixtures("data_load")
class TestData():
    def test_edit_profile(self,data_load):  # here when return something and receiving data that's why use parameter
        # print(data_load)

        print(data_load[0])  # this is only use when want specific data
        print(data_load[2])