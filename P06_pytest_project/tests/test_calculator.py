from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
            a = 4321
            b = 1234
            cal = Calculator()

            # act
            result = cal.subtract(a, b)

            # assert
            expected = a - b
            assert result == expected
    
    def test_multiply(self):
        # arrange
            a = 4321
            b = 1234
            cal = Calculator()

            # act
            result = cal.multiply(a, b)

            # assert
            expected = a * b
            assert result == expected

    def test_divide(self):
        # arrange
            a = 4321
            b = 1234
            cal = Calculator()

            # act
            result = cal.divide(a, b)

            # assert
            expected = a / b
            assert result == expected
    
    def test_ZeroDivisionError(self):
        # arrange
            a = 4321
            b = 0
            cal = Calculator()

            # act
            with pytest.raises(ZeroDivisionError):
                result = cal.divide(a, b)
