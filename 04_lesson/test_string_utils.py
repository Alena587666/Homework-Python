import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.parametrize("string",
  [ 
    ("москва", "Москва"),
    ("николай", "Николай"),
    ("skypro", "Skypro"),
  ],
)

def test_capitilize_positive(string: str) -> str:
  string = StringUtils()  
  assert string.capitilize(string)

@pytest.mark.parametrize("string",
  [ 
    ("  Mосква", "Москва"),
    (" Hиколай", "Николай"),
    ("  Skypro", "Skypro"),
  ],
)

def test_trim_positive(string: str) -> str:
  string = StringUtils()
  whitespace = " "
  while string.startswith(whitespace):
        string = string.removeprefix(whitespace)
  assert string