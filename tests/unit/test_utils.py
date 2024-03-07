import pytest

from stringutils.utils import (
    add_list_elements,
    capitalize_string,
    reverse_string,
)


@pytest.fixture
def input_lists():
    _list1 = ["Big", "Good", "Light"]
    _list2 = ["Small", "Bad", "Heavy"]
    return (_list1, _list2)


@pytest.mark.unit
def test_reverse_string(input_strings):
    assert reverse_string(input_strings[0]) == "olleh"
    assert reverse_string(input_strings[1]) == "soidA"
    assert reverse_string(input_strings[2]) == "eYB"


@pytest.mark.unit
def test_capitalize_string(input_strings):
    assert capitalize_string(input_strings[0]) == "HELLO"
    assert capitalize_string(input_strings[1]) == "ADIOS"
    assert capitalize_string(input_strings[2]) == "BYE"


# @pytest.mark.unit
def test_add_list_elements(input_lists):
    assert add_list_elements(input_lists[0], input_lists[1]) == [
        "BigSmall",
        "GoodBad",
        "LightHeavy",
    ]
