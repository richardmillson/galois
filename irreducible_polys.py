# given a finite field, will generate each possible polynomial over this field
# will then evaluate each polynomial at each possible value in the field,
# rejecting polynomials that contain a root in the field

# from numpy import polynomial
import numpy
import itertools


def has_roots(poly, p):
    """
    :param poly: numpy.polynomial.polynomial
    :param p: int
    :return: bool
    evaluates the polynomial at all possible residues,
    returns true if the polynomial has a root
    """
    return any((numpy.polyval(poly, x) % p == 0 for x in range(p)))


def irred_polys(p, d):
    """
    :param p: int
    :param d: int
    :return: tuple(numpy.polynomial.polynomial)
    returns a tuple of polynomials that do not have roots
    """
    return (poly for poly in cand_polys(p, d) if not has_roots(poly, p))


def cand_polys(p, d):
    """
    :param p: int
    :param d: int
    :return: generator of numpy.polynomial.polynomial
    returns a generator for all polynomials in the given field
    stored as a tuple of coefficients from highest to lowest power
    note that polynomials with zero constant term are excluded
    because they are guaranteed to have a root at x = 0
    """
    cand_polys = itertools.product(range(p), repeat=d)
    return ((1,) + poly for poly in cand_polys if not poly[-1] == 0)
