import pytest
from src.listas_12 import matrix_products

@pytest.mark.parametrize(
    'A,B,C',
    [
        ([[1,2,3],[4,5,6]], [[-1,0],[0,1],[1,1]], [[2, 5],[2, 11]])
    ]
)
def test_matrix_products_params(A,B,C):
    assert matrix_products(A,B) == C