import pytest
from src.listas_05 import reverse_list

@pytest.mark.parametrize(
    'list,reversed_list',
    [
        ([1,2,3,4,5,6,7,8,9,10],[10,9,8,7,6,5,4,3,2,1])
    ]
)
def test_reverse_list_params(list,reversed_list):
    assert reverse_list(list) == reversed_list