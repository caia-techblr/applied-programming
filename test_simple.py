import pytest

def is_even(num):
    return num % 2 == 0

def is_leap(yy):
    return yy % 4 == 0  # fix the logic

def test_dummy():
    assert 2 + 3 == 5

def test_even():
    assert is_even(44)

def test_leap_centuries():
    assert is_leap(2400)

def test_non_leap_centuries():
    assert not is_leap(1900) 
    assert not is_leap(00) 

def test_leap_years():
    assert is_leap(1996)

def test_non_leap_years():
    assert not is_leap(2015)
