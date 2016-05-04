from irreducible_polys import *


def test_cand_polys():
    assert list(cand_polys(3, 3)) == [(1, 0, 0, 1), (1, 0, 0, 2), (1, 0, 1, 1), (1, 0, 1, 2), (1, 0, 2, 1), (1, 0, 2, 2), (1, 1, 0, 1), (1, 1, 0, 2), (1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 2, 1), (1, 1, 2, 2), (1, 2, 0, 1), (1, 2, 0, 2), (1, 2, 1, 1), (1, 2, 1, 2), (1, 2, 2, 1), (1, 2, 2, 2)]


def test_irred_polys():
    assert list(irred_polys(3, 3)) == [(1, 0, 2, 1), (1, 0, 2, 2), (1, 1, 0, 2), (1, 1, 1, 2), (1, 1, 2, 1), (1, 2, 0, 1), (1, 2, 1, 1), (1, 2, 2, 2)]


test_cand_polys()
test_irred_polys()