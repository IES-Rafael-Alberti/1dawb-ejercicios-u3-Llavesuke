import pytest
from src.listas_11 import scalar_product

@pytest.mark.parametrize(
    'u_vector,v_vector,expected',
    [
        ([120,40,56], [48,79,25], (5760, 3160, 1400))
    ]
)
def test_scalar_product_params(u_vector,v_vector,expected):
    assert scalar_product(u_vector,v_vector) == expected