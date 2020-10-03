class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        module = (other.real ** 2 + other.imaginary ** 2)
        other_real_reciproc = other.real / module
        other_imaginary_reciproc = - other.imaginary / module
        recyproc = ComplexNumber(other_real_reciproc, other_imaginary_reciproc)
        return self * recyproc

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        from math import e, sin, cos

        return ComplexNumber(e ** self.real, 0) * ComplexNumber(cos(self.imaginary), sin(self.imaginary))
