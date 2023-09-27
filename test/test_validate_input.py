import unittest
from unittest.mock import Mock
from DrawingTriangle.input_validation import validate_input

class TestValidateInput(unittest.TestCase):
    def setUp(self):
        self.error_label = Mock()

    def test_validate_input_positive_integer(self):
        input_num = "50"
        result = validate_input(input_num, self.error_label)
        self.assertTrue(result)
        self.error_label.config.assert_called_once_with(text="")

    def test_validate_input_non_positive_integer(self):
        input_num = "-1337"
        result = validate_input(input_num, self.error_label)
        self.assertFalse(result)
        self.error_label.config.assert_called_once_with(text="Введите целое положительное число больше 0")

    def test_validate_input_non_integer2(self):
        input_num = "abcdef"
        result = validate_input(input_num, self.error_label)
        self.assertFalse(result)
        self.error_label.config.assert_called_once_with(text="Введите числовое значение")

    def test_validate_input_non_integer3(self):
        input_num = "*#@"
        result = validate_input(input_num, self.error_label)
        self.assertFalse(result)
        self.error_label.config.assert_called_once_with(text="Введите числовое значение")

    def test_validate_input_zero(self):
        input_num = "0"
        result = validate_input(input_num, self.error_label)
        self.assertFalse(result)
        self.error_label.config.assert_called_once_with(text="Введите целое положительное число больше 0")

if __name__ == "__main__":
    unittest.main()
