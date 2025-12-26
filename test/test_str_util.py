from utils.str_rev import reverse_digits

def test_reverse_digits():
    result = reverse_digits("a1b2c3d4")
    assert result == "a4b3c2d1"
