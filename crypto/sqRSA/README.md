# sqRSA

> Im having trouble with this RSA stuff. I think I'm doing it right but it keeps giving me an error! Can you get my program to work?

Basically, using `e = 2` is an illegal RSA move in this case. The key insight is that `e = 2` implies the use of a cryptosystem similar to Rabin's, which requires computing square roots modulo primes and using the Chinese Remainder Theorem (CRT) to reconstruct the message.

To solve this, we write a python script that does:

- Square Roots Modulo Primes: Compute the square roots of the ciphertext c modulo primes p and q. Since p ≡ 3 (mod 4), we can directly compute the roots. For q ≡ 1 (mod 4), use the Tonelli-Shanks algorithm.
- Chinese Remainder Theorem: Combine the square roots from both primes to find possible plaintexts.
- Padding Check: Validate each possible plaintext by checking PKCS#7 padding to identify the correct flag.