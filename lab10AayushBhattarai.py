class IDEA:
    MOD_ADD = 0x10000   # 2^16
    MOD_MUL = 0x10001   # 2^16 + 1

    def __init__(self, key: int):
        if not (0 <= key < (1 << 128)):
            raise ValueError("Key must be a 128-bit integer")

        self.enc_keys = self._generate_encrypt_keys(key)
        self.dec_keys = self._generate_decrypt_keys(self.enc_keys)

    # ---------- Basic Operations ----------

    def _add(self, a, b):
        return (a + b) & 0xFFFF

    def _mul(self, a, b):
        if a == 0:
            a = self.MOD_MUL - 1
        if b == 0:
            b = self.MOD_MUL - 1
        r = (a * b) % self.MOD_MUL
        return 0 if r == self.MOD_MUL - 1 else r

    def _mul_inv(self, x):
        return 0 if x == 0 else pow(x, -1, self.MOD_MUL)

    # ---------- Key Schedule ----------

    def _generate_encrypt_keys(self, key):
        keys = []
        for _ in range(6 * 8 + 4):  # 52 keys
            keys.append((key >> 112) & 0xFFFF)
            key = ((key << 16) | (key >> 112)) & ((1 << 128) - 1)
        return keys

    def _generate_decrypt_keys(self, ek):
        dk = [0] * 52
        dk[48] = self._mul_inv(ek[0])
        dk[49] = (-ek[1]) & 0xFFFF
        dk[50] = (-ek[2]) & 0xFFFF
        dk[51] = self._mul_inv(ek[3])

        j = 4
        for i in range(42, -1, -6):
            dk[i + 4] = ek[j + 4]
            dk[i + 5] = ek[j + 5]
            dk[i] = self._mul_inv(ek[j])
            dk[i + 1] = (-ek[j + 2]) & 0xFFFF
            dk[i + 2] = (-ek[j + 1]) & 0xFFFF
            dk[i + 3] = self._mul_inv(ek[j + 3])
            j += 6

        return dk

    # ---------- Core Algorithm ----------

    def _process_block(self, block, keys):
        x1, x2, x3, x4 = block
        k = 0

        for _ in range(8):
            y1 = self._mul(x1, keys[k]); k += 1
            y2 = self._add(x2, keys[k]); k += 1
            y3 = self._add(x3, keys[k]); k += 1
            y4 = self._mul(x4, keys[k]); k += 1

            t1 = self._mul(y1 ^ y3, keys[k]); k += 1
            t2 = self._mul(self._add(y2 ^ y4, t1), keys[k]); k += 1
            t1 = self._add(t1, t2)

            x1 = y1 ^ t2
            x2 = y3 ^ t2
            x3 = y2 ^ t1
            x4 = y4 ^ t1

        # Final transformation
        z1 = self._mul(x1, keys[k])
        z2 = self._add(x3, keys[k + 1])
        z3 = self._add(x2, keys[k + 2])
        z4 = self._mul(x4, keys[k + 3])

        return z1, z2, z3, z4

    # ---------- Public API ----------

    def encrypt(self, block):
        return self._process_block(block, self.enc_keys)

    def decrypt(self, block):
        return self._process_block(block, self.dec_keys)


# ---------- Demo ----------
if __name__ == "__main__":
    plaintext = (0x1234, 0x5678, 0x9ABC, 0xDEF0)
    key = 0x2BD6459F82C5B300952C49104881FF48

    idea = IDEA(key)
    ciphertext = idea.encrypt(plaintext)
    recovered = idea.decrypt(ciphertext)

    print("Plaintext :", plaintext)
    print("Encrypted :", ciphertext)
    print("Decrypted :", recovered)