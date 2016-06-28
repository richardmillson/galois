# tests to determine whether a polynomial is irreducible over Q[x]

from fractions import Fraction
import numpy


def is_prime(num):
    """
    return True if num is a prime
    :param num: int
    :return: Bool
    """
    return True


def rational_root(poly):
    """
    rational root test
    :param poly: numpy.polynomial.polynomial
    :return: Bool
    """
    return True


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
