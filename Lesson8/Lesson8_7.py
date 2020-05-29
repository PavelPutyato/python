class ComplexNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return complex(self.a, self.b) + complex(other.a, other.b)

    def __mul__(self, other):
        return complex(self.a, self.b) * complex(other.a, other.b)


cn1 = ComplexNumbers(30, 0.03)
cn2 = ComplexNumbers(20, 0.6)
print(cn1 + cn2)
print(cn1 * cn2)