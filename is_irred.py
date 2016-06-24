# tests to determine whether a polynomial is irreducible over a finite field

import numpy


def eisenstein(poly, p):
    """
    returns true if poly is irreducible by Eisenstein's sufficient condition:
    p is prime
    p does not divide the leading coefficient
    p divides every other coefficient
    p squared does not divide the constant term
    note that if Eisenstein's condition is not met, ie returns false,
    this does not necessarily imply that poly is reducible
    :param poly: numpy.polynomial.polynomial
    :param p: int
    :return: Bool
    """
    return all(poly[0] % p != 0,
               poly[0] % p**2 != 0,
               all(poly[x] % p == 0 for x in range(1, len(poly))))
