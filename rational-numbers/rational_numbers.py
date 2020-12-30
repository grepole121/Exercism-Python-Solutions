from __future__ import division
from fractions import gcd

class Rational:
    def __init__(self, numer, denom):
        rat_gcd = gcd(numer, denom)
        self.numer = int(numer/rat_gcd)
        self.denom = int(denom/rat_gcd)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational( ((self.numer * other.denom) + (self.denom * other.numer)), (self.denom * other.denom))

    def __sub__(self, other):
        return Rational( ((self.numer * other.denom) - (self.denom * other.numer)), (self.denom * other.denom))

    def __mul__(self, other):
        return Rational( self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational( self.numer * other.denom, other.numer * self.denom)

    def __abs__(self):
        return Rational( abs(self.numer), abs(self.denom) )

    def __pow__(self, power):
        return Rational( self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return base ** (self.numer/self.denom)
