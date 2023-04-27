import unittest
from vigenere_cipher import VigenereCipher

class TestVigenereCipher(unittest.TestCase):
    def test_encrypt(self):
        cipher = VigenereCipher("MYSECRETKEY")
        plaintext = "Hello, World!"
        expected_ciphertext = "T,!PQN?JYVDPV"
        self.assertEqual(cipher.encrypt(plaintext), expected_ciphertext)

    def test_decrypt(self):
        cipher = VigenereCipher("MYSECRETKEY")
        ciphertext = "T,!PQN?JYVDPV"
        expected_plaintext = "HELLO, WORLD!"
        self.assertEqual(cipher.decrypt(ciphertext), expected_plaintext)

    def test_encrypt_decrypt(self):
        cipher = VigenereCipher("MYSECRETKEY")
        plaintext = "Hello, World!"
        ciphertext = cipher.encrypt(plaintext)
        decrypted_text = cipher.decrypt(ciphertext)
        self.assertEqual(decrypted_text, plaintext.upper())

if __name__ == "__main__":
    unittest.main()
