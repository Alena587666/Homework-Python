import pytest
from string_utils import StringUtils

string_utils = StringUtils()
#1
def test_capitalize_positive():
    assert string_utils.capitalize("skypro") == "Skypro"
    assert string_utils.capitalize("python") == "Python"
    assert string_utils.capitalize("hello") =="Hello"

def test_capitalize_negative():
    assert string_utils.capitalize(" ") == "Skypro"
#2
def test_trim_positive():
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("   hello") == "hello"
    assert string_utils.trim("   abc") == "abc"
#3
def test_contains_positive():
    assert string_utils.contains("Skypro","S") == True
    assert string_utils.contains("Skypro", "U") == False

def test_contains_negative():
    assert string_utils.contains("Skypro", "U") == True
    assert string_utils.contains("Skypro", "S") == False
#4
def test_delete_symbol_positive():
    assert string_utils.delete_symbol("Skypro", "K") == "Sypro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"

