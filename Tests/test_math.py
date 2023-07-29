import math


def test_fun_ceil():
    resp  = math.ceil(10.7)
    assert 11 == resp

def test_fun_floor():
    resp  = math.floor(10.7)
    assert 10 == resp

def test_fun_pow():
    expected = int(8)
    resp  = math.pow(2, 4)
    assert expected == resp