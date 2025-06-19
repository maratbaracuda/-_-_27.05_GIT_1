import pytest
from calc_homework import Calculator

class TestCalculator:
    def setup_method(self) -> None:
        self.calc = Calculator()
    def test_divide_by_zero(self):
        result = self.calc.divide(6,0)
        assert result == "Делить на ноль нельзя"