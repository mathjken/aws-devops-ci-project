from app import add_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_add_negative_numbers():
    assert add_numbers(-2, -3) == -5
