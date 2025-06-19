class Calculator():
    @staticmethod
    def divide(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            return "Делить на ноль нельзя"
        else:
            return result
