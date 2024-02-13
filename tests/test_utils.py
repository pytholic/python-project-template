import pytest

from stringutils import capitalize_string, reverse_string


@pytest.fixture
def input_strings():
    return ["hello", "Adios", "BYe"]


def test_reverse_string(input_strings):
    for input_str in input_strings:
        expected_output = input_str[::-1]
        assert reverse_string(input_str) == expected_output


def test_capitalize_string(input_strings):
    for input_str in input_strings:
        expected_output = input_str.capitalize()
        assert capitalize_string(input_str) == expected_output
