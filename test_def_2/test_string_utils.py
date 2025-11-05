from srs.string_utils import palindrome
import pytest

@pytest.mark.parametrize("s", ["stats", "deified"])
def test_palindrome_true(s):
    assert palindrome(s)
    

@pytest.mark.parametrize("s", ["hello", "world"])
def test_string_utils_false(s):
    assert not palindrome(s)
    