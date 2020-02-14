from examples.identifier import Identifier

def test_case_01:
    identifier = Identifier()

    is_valid = identifier.validate_identifier('ab')

    assert is_valid is True
