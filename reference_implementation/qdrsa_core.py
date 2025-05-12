# QD-RSA Core Functions (Python)
import math
import hashlib
import hmac

def phi_s(x, eps_s, n):
    kappa_s = math.pi + eps_s
    return int(x * math.sin(kappa_s * x)) % n

def xi_s(x, gamma, delta, r, n):
    x_r = x + r
    return int((x_r**2) * math.cosh(gamma * x_r) * math.atan(delta * x_r)) % n

def i_star(x, N_s=20, b=10):
    acc = sum((x**k) / (b**k) for k in range(1, N_s + 1))
    return hashlib.sha3_256(str(acc).encode()).hexdigest()
