from irreducible_polys import *


def test_cand_polys():
    assert list(cand_polys(2, 3)) == [(1, 0, 0, 1), (1, 0, 1, 1),
                                      (1, 1, 0, 1), (1, 1, 1, 1)]


def test_irred_polys():
    assert list(irred_polys(2, 3)) == [(1, 0, 1, 1), (1, 1, 0, 1)]

test_cand_polys()
test_irred_polys()
