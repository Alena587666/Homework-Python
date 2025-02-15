import pytest
from string_utils import StringUtils

string_utils = StringUtils()

def test_capitalize_positive():
    assert string_utils.capitalize("skypro") == ["Skypro"]
