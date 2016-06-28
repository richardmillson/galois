# given a finite field, will generate each possible polynomial over this field
# will then evaluate each polynomial at each possible value in the field,
# rejecting polynomials that contain a root in the field

import numpy
import itertools


def has_roots(poly, p):
    """
    evaluates the polynomial poly at all possible residues of F_p
    returns true if the polynomial has a root
    :param poly: numpy.polynomial.polynomial
    :param p: int
    :return: bool
    """
    return any((numpy.polyval(poly, x) % p == 0 for x in range(p)))


def irred_polys(p, d):
    """
    returns a tuple of polynomials of degree d
    that do not have any roots over the field of p elements
    :param p: int
    :param d: int
    :return: tuple(numpy.polynomial.polynomial)
    """
    return (poly for poly in cand_polys(p, d) if not has_roots(poly, p))


def cand_polys(p, d):
    """
    returns all candidate polynomials of degree d over the field of p elements
    as a generator of tuples of polynomial coefficients in order of increasing degree
    polynomials with a zero constant term are excluded
    because they are guaranteed to have a root at x = 0
    :param p: int
    :param d: int
    :return: generator of numpy.polynomial.polynomial
    """
    polys = itertools.product(range(p), repeat=d)
    return (poly + (1,) for poly in polys if not poly[0] == 0)
