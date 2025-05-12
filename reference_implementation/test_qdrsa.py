# Basic tests for QD-RSA core
from qdrsa_core import phi_s, xi_s, i_star

def test_phi():
    assert isinstance(phi_s(5, 0.00031415, 997), int)

def test_xi():
    assert isinstance(xi_s(7, 1.3, 0.8, 2, 997), int)

def test_hash():
    h = i_star(9)
    assert len(h) == 64 and all(c in '0123456789abcdef' for c in h)

if __name__ == "__main__":
    test_phi()
    test_xi()
    test_hash()
    print("All QD-RSA core tests passed.")
