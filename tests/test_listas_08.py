import pytest
from src.listas_08 import palindrome

@pytest.mark.parametrize(
    'word,expected',
    [
        (['a','n','a'], True),
        (['p','e','r','r','i','t','o'],False)
    ]
)
def test_palindrome_params(word,expected):
    assert palindrome(word) == expected