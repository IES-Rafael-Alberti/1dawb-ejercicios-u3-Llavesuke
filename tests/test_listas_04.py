import pytest 
from src.listas_04 import order_list

@pytest.mark.parametrize(
    'list, ordered_list',
    [
        ([10,32,43,15,33,27], [10,15,27,32,33,43])
    ]
)
def test_order_list_params(list,ordered_list):
    assert order_list(list) == ordered_list