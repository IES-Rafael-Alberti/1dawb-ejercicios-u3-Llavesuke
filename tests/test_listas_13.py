import pytest
from src.listas_13 import calculate_average, calculate_typical_deviation

@pytest.mark.parametrize(
    'numeric_list,average',
    [
        ([15,43,120,40], 54.5)
    ]
)
def test_calculate_average_params(numeric_list,average):
    assert calculate_average(numeric_list) == average

@pytest.mark.parametrize(
    'numeric_list,typical_deviation',
    [
        ([15,43,120,40],39.35)
    ]
)
def test_calculate_typical_deviation(numeric_list,typical_deviation):
    assert calculate_typical_deviation(numeric_list) == typical_deviation