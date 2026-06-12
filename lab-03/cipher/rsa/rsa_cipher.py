import json
import os
import random
import hashlib


class RSACipher:
    def __init__(self, key_dir=None):
        self.key_dir = key_dir or os.path.dirname(os.path.abspath(__file__))
        self.private_key_path = os.path.join(self.key_dir, 'private_key.json')
        self.public_key_path = os.path.join(self.key_dir, 'public_key.json')

    def generate_keys(self):
        p = self._generate_prime(512)
        q = self._generate_prime(512)
        while q == p:
            q = self._generate_prime(512)

        n = p * q
        phi = (p - 1) * (q - 1)
        e = 65537
        d = self._modinv(e, phi)

        private_key = {'n': n, 'e': e, 'd': d, 'p': p, 'q': q}
        public_key = {'n': n, 'e': e}

        with open(self.private_key_path, 'w', encoding='utf-8') as f:
            json.dump(private_key, f)
        with open(self.public_key_path, 'w', encoding='utf-8') as f:
            json.dump(public_key, f)

    def load_keys(self):
        if not os.path.exists(self.private_key_path) or not os.path.exists(self.public_key_path):
            self.generate_keys()

        with open(self.private_key_path, 'r', encoding='utf-8') as f:
            private_key = json.load(f)
        with open(self.public_key_path, 'r', encoding='utf-8') as f:
            public_key = json.load(f)

        return private_key, public_key

    def encrypt(self, message, key):
        if isinstance(message, str):
            message = message.encode('utf-8')
        m_int = int.from_bytes(message, 'big')
        if m_int >= key['n']:
            raise ValueError('Message too large for key size')
        c_int = pow(m_int, key['e'], key['n'])
        size = (key['n'].bit_length() + 7) // 8
        return c_int.to_bytes(size, 'big')

    def decrypt(self, ciphertext, key):
        if isinstance(ciphertext, str):
            ciphertext = bytes.fromhex(ciphertext)
        c_int = int.from_bytes(ciphertext, 'big')
        m_int = pow(c_int, key['d'], key['n'])
        message = m_int.to_bytes((m_int.bit_length() + 7) // 8, 'big')
        return message.decode('utf-8', errors='replace')

    def sign(self, message, private_key):
        if isinstance(message, str):
            message = message.encode('utf-8')
        digest = hashlib.sha256(message).digest()
        h_int = int.from_bytes(digest, 'big')
        s_int = pow(h_int, private_key['d'], private_key['n'])
        size = (private_key['n'].bit_length() + 7) // 8
        return s_int.to_bytes(size, 'big')

    def verify(self, message, signature, public_key):
        if isinstance(message, str):
            message = message.encode('utf-8')
        if isinstance(signature, str):
            signature = bytes.fromhex(signature)
        h_int = int.from_bytes(hashlib.sha256(message).digest(), 'big')
        s_int = int.from_bytes(signature, 'big')
        verified = pow(s_int, public_key['e'], public_key['n'])
        return verified == h_int

    def _generate_prime(self, bits):
        while True:
            candidate = random.getrandbits(bits) | 1 | (1 << bits - 1)
            if self._is_prime(candidate):
                return candidate

    def _is_prime(self, n, witnesses=None):
        if n < 2:
            return False
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for p in small_primes:
            if n == p:
                return True
            if n % p == 0:
                return False
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        if witnesses is None:
            witnesses = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
        for a in witnesses:
            if a % n == 0:
                continue
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def _egcd(self, a, b):
        if b == 0:
            return (a, 1, 0)
        g, x1, y1 = self._egcd(b, a % b)
        return (g, y1, x1 - (a // b) * y1)

    def _modinv(self, a, m):
        g, x, _ = self._egcd(a, m)
        if g != 1:
            raise ValueError('Modular inverse does not exist')
        return x % m
