from stringutils import capitalize_string, reverse_string


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Adios") == "soidA"
    assert reverse_string("BYe") == "eYB"


def test_capitalize_string():
    assert capitalize_string("hello") == "HELLO"
    assert capitalize_string("Adios") == "ADIOS"
    assert capitalize_string("BYe") == "BYE"
