import pytest
from src.listas_06 import check_approved

@pytest.mark.parametrize(
    'subjects,marks,expected',
    [
        (['Matemáticas','Lengua','Ingles'], [6,3,7], ['Matemáticas','Ingles'])
    ]
)
def test_check_approved(subjects,marks,expected):
    assert check_approved(subjects,marks) == expected