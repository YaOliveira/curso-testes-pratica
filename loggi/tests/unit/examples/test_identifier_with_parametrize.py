from examples.identifier import Identifier
import pytest

@pytest.mark.parametrize(
    'indentif',
    [
        pytest.param('a', id='uma_letra'),
        pytest.param('ab', id='duas_letras'),
        pytest.param('abcde', id = "quatro_letras"),
        pytest.param('abcdef', id='seis_letras'),
        pytest.param('a1', id='letra_e_numero'),
           
    ]
)
def test_all_cases_true(indentif):
    identifier = Identifier()

    is_valid = identifier.validate_identifier(indentif)

    assert is_valid is True





@pytest.mark.parametrize(
    'indentiff',
    [
        pytest.param('', id ='vazio'),
        pytest.param('abcdefg', id = 'excedeu_limite'),
        pytest.param('1a', id='inicia_com_numero'),
        pytest.param('açai', id='caracter_invalido'),

    ]
)
def test_all_cases_false(indentiff):
    identifier = Identifier()

    is_valid = identifier.validate_identifier(indentiff)

    assert is_valid is False
