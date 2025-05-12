// QD-RSA Core Placeholder in C
#include <math.h>
#include <stdint.h>

uint64_t phi_s(uint64_t x, double eps_s, uint64_t n) {
    double kappa_s = M_PI + eps_s;
    return (uint64_t)(x * sin(kappa_s * x)) % n;
}
