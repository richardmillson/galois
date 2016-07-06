# tests to determine whether a polynomial is irreducible over Q[x]
# let poly = a_0 + a_1 x + ... + a_n x^n

from fractions import Fraction
import numpy


def is_prime(num):
    """
    return True if num is a prime
    :param num: int
    :return: Bool
    """
    return True


def divisors(num):
    """
    returns a list of all divisors of num
    including the trivial divisors 1 and num itslef
    :param num: int
    :return: list(int)
    """
    pass


def gcd(a, b):
    """
    given two integers, returns their greatest common divisor
    :param a: int
    :param b: int
    :return: int
    """
    while b:
        a, b = b, a % b
    return a


def rational_root(poly):
    """
    rational root test
    :param poly: numpy.polynomial.polynomial
    :return: Bool
    """
    a_0 = poly[0]
    a_n = poly[-1]
    cand_numerators = divisors(a_0)
    cand_denominators = divisors(a_n)
    cand_roots = (Fraction(r, s) for r in cand_numerators for s in cand_denominators if gcd(r, s) == 1)
    return any((numpy.polyval(poly, cand_root) == 0 for cand_root in cand_roots))


def eisenstein(poly, p):
    """
    returns True if poly is irreducible by Eisenstein's sufficient condition:
    p is prime
    p does not divide the leading coefficient
    p divides every other coefficient
    p squared does not divide the constant term
    note that if Eisenstein's condition is not met, ie returns False,
    this does not necessarily imply that poly is reducible
    :param poly: numpy.polynomial.polynomial
    :param p: int
    :return: Bool
    """
    return all(is_prime(p),
               poly[0] % p != 0,
               poly[0] % p**2 != 0,
               all(poly[x] % p == 0 for x in range(1, len(poly))))
