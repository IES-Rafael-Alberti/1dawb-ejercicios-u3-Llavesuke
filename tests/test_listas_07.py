import pytest
from src.listas_07 import check_3

@pytest.mark.parametrize(
    'list, filtered_list',
    [
        (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
         ['b', 'c', 'e', 'f', 'h', 'i', 'k', 'l', 'n', 'o', 'q', 'r', 't', 'u', 'w', 'x', 'z'])
    ]
)
def test_check_3_params(list,filtered_list):
    assert check_3(list) == filtered_list
    