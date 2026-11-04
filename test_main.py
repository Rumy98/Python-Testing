# from main import get_weather
# def test_get_weather():
#     assert get_weather(21)=="hot"
#     assert get_weather(1)=="cold"
#     assert get_weather(11)=="hot"

from main import add,divide
import pytest

def test_add():
    assert add(2,3)==5,"2+3 should be 5"
    assert add(-1,1)==5, "-1+1 should be 0"
    assert add(5,1)==6, "5+1 should be 6"

def test_divide():
    with pytest.raises(ValueError,match="Can be divided by 0"):
        divide(10,0)
