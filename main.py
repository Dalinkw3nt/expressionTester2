class ExpressionEvaluator:

    def __init__(self, expression):
        self.expression = expression.replace(' ', '')
        self.index = 0

    def evaluate(self):
        try:
            result = self._evaluate_expression()
            if self.index != len(self.expression):
                return "Invalid Expression"
            return str(result)
        except (ValueError, ZeroDivisionError, IndexError):
            return "Invalid Expression"
#define the evaluate_expression method

    def _evaluate_expression(self):
        term = self._evaluate_term()
        while self.index < len(
                self.expression) and self.expression[self.index] in ('+', '-'):
            operator = self.expression[self.index]
            self.index += 1
            next_term = self._evaluate_term()
            if operator == '+':
                term += next_term
            else:
                term -= next_term
        return term
#define the evaluate_term method

    def _evaluate_term(self):
        factor = self._evaluate_factor()
        while self.index < len(
                self.expression) and self.expression[self.index] in ('*', '/'):
            operator = self.expression[self.index]
            self.index += 1
            next_factor = self._evaluate_factor()
            if operator == '*':
                factor *= next_factor
            else:
                if next_factor == 0:
                    raise ZeroDivisionError
                factor /= next_factor
        return factor
#define the evaluate_factor method

    def _evaluate_factor(self):
        if self.expression[self.index] == '(':
            self.index += 1
            result = self._evaluate_expression()
            if self.expression[self.index] != ')':
                raise ValueError
            self.index += 1
            return result
        return self._get_number()


#define the get_number method

    def _get_number(self):
        start = self.index
        while self.index < len(
                self.expression) and (self.expression[self.index].isdigit()
                                      or self.expression[self.index] == '.'):
            self.index += 1
        return float(self.expression[start:self.index])


def evaluate_algebraic_expression(expression):
    evaluator = ExpressionEvaluator(expression)
    return evaluator.evaluate()


# Test cases
#expressions = [
#    "3 + 12 * 3 / 12",
#    "(3 + 3) * 42 / (6 + 12)",
#    "4 (12E)",
#    "4 (41)",
#    "42+43**271"
#]

expressions = input("Please enter an Expression to Evaluate"
                    " (e.g. 2 + 3 * 4 / (5 - 6) - 7): ")

#for expr in expressions:
result = evaluate_algebraic_expression(expressions)
print("Result", result)

#
