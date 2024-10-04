
class power():
    def __init__(self):
        self.exponent = 1
        self.base = 0

    def get_base(self):
        get_base = int(input("Enter the base: "))
        self.base = get_base

    def get_exponent(self):
        get_exponent = int(input("Enter the exponent: "))
        self.exponent = get_exponent

    def evaluate(self, base=None, exponent=None):
        if base is None and exponent is None:
            base = self.base
            exponent = self.exponent

        if exponent == 0:
            return 1
        else:
            return base * self.evaluate(base, exponent - 1)


p = power()
p.get_base()
p.get_exponent()
result = p.evaluate()
print(f"{p.base} raised to the power of {p.exponent} is: {result}")

