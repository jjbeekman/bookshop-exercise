from cin import is_valid_cin, get_checksum
import pytest


class TestIsValidCin:
    def test_is_valid_cin(self):
        """Valid CIN test"""
        input = "17000372214424"

        result = is_valid_cin(input)

        assert result is True

    def test_is_valid_cin_wrong_checksum(self):
        """Same CIN as previous test but with wrong checksum"""
        input = "17000372214428"

        result = is_valid_cin(input)

        assert result is False

    def test_is_valid_cin_input_digits(self):
        """CIN value contains string characters"""
        input = "hello_world123"

        result = is_valid_cin(input)

        assert result is False

    def test_is_valid_cin_input_length(self):
        """CIN value has the wrong length"""
        input = "17000374"

        result = is_valid_cin(input)

        assert result is False


class TestChecksum:
    def test_checksum(self):
        """Correct checksum"""
        input = "170003722144"

        result = get_checksum(input)

        assert result == "24"

    def test_checksum_leading_zero(self):
        """Checksum needs to get a leading zero appended"""
        input = "170049382730"

        result = get_checksum(input)

        assert result == "04"

    def test_checksum_input_digit(self):
        """CIN input contains non digits"""
        input = "abcdefghijkl"

        with pytest.raises(AssertionError):
            get_checksum(input)

    def test_checksum_input_length(self):
        """CIN input incorrect length"""
        input = "123456"

        with pytest.raises(AssertionError):
            get_checksum(input)
