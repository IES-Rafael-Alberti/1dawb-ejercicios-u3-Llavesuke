import pytest
from src.listas_10 import higher_lower

@pytest.mark.parametrize(
    'numbers_tuple, tuple_expected',
    [
        ((50, 75, 46, 22, 80, 65, 8), (80,8))
    ]
)
def test_higher_lower_params(numbers_tuple,tuple_expected):
    assert higher_lower(numbers_tuple) == tuple_expected