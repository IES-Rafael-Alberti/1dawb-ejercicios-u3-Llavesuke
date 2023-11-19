import pytest
from src.listas_09 import count_vowels

@pytest.mark.parametrize(
    'word,counted_list',
    [
        ('Raptor',[1,0,0,1,0]),
        ('Megaciclon',[1,1,1,1,0]),
        ('Destroza taladros',[3,1,0,2,0])
    ]
)
def test_count_vowels_params(word,counted_list):
    assert count_vowels(word) == counted_list