import pytest


def test_sub():
    assert 2 - 2 == 0

def test_add():
    assert 2 + 2 == 4

def test_mul():
    assert 2 * 3 == 5

def test_div():
    assert 2 / 2 != 0




# @pytest.mark.smoke
# def test_sub2():
#     assert 2 - 2 == 0
#
#
# @pytest.mark.reg
# def test_sub3():
#
#
# @pytest.mark.reg
# def test_sub4():
#     assert 2 - 2 == 0
#
#
# @pytest.mark.skip(reason="Not implemented yet")
# def test_subtraction():
#     assert 2 - 1 == 1
