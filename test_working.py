from working import convert
import pytest

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")


def test_wrong_minute():
    with pytest.raises(ValueError):
         convert("9:60 AM to 9:60 PM")


def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")