from Crypto.Util.number import inverse, long_to_bytes

# Given values
e = 2
p = 8946541176074654913817717054410771331419218032593785296134838490312525894218240553305396599307555077734655624876704161811830296918000348456470769765921767
q = 8932929811422923151480388874853984777290071075825590049173830382535883452482114410463430296988680318519251836647527145507992221700683938654669731212502879
n = p * q
c = 17349894155329354363328734000800652637346887108866919240446747423455120556394923514564284438906649577094462846372316919957176356395706169922421515974398971844608693078173465906525109301576180786133798467234128571459625488335621909834995712400917418963473920470534646258784866422718709370743346105151573384808

def tonelli_shanks(n, p):
    assert pow(n, (p-1) // 2, p) == 1, "n is not a square (mod p)"
    if p % 4 == 3:
        x = pow(n, (p + 1) // 4, p)
        return [x, (p - x) % p]
    # Tonelli-Shanks for p %4 == 1
    Q = p - 1
    S = 0
    while Q % 2 == 0:
        Q //= 2
        S += 1
    z = 2
    while pow(z, (p-1) // 2, p) == 1:
        z += 1
    c = pow(z, Q, p)
    x = pow(n, (Q + 1) // 2, p)
    t = pow(n, Q, p)
    m = S
    while t != 1:
        i, temp = 0, t
        for i in range(1, m):
            temp = pow(temp, 2, p)
            if temp == 1:
                break
        b = pow(c, 1 << (m - i - 1), p)
        x = (x * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        m = i
    return [x, (p - x) % p]

# Compute square roots modulo p and q
c_p = c % p
sqrt_p = [pow(c_p, (p + 1) // 4, p), (-pow(c_p, (p + 1) // 4, p)) % p]

c_q = c % q
sqrt_q = tonelli_shanks(c_q, q)

# Generate all combinations of roots
from itertools import product

for r_p, r_q in product(sqrt_p, sqrt_q):
    # Apply CRT
    m_p = r_p
    m_q = r_q
    # x ≡ m_p mod p, x ≡ m_q mod q
    # Using Garner's formula
    h = (inverse(p, q) * (m_q - m_p)) % q
    m = m_p + h * p
    m %= n
    # Check padding
    try:
        pt = long_to_bytes(m)
        padding_length = pt[-1]
        if padding_length < 1 or padding_length > 100:
            continue
        if all(b == padding_length for b in pt[-padding_length:]):
            print("Flag:", pt[:-padding_length].decode())
            exit()
    except:
        continue