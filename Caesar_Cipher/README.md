# caesar_cipher
A lightweight Python module that encrypts and decrypts text messages using a Caesar cipher substitution mapping with customizable shifts.

## Features

- **Custom Shift Range:** Supports rotation keys from 1 to 25.
- **Case Preservation:** Encrypts both uppercase and lowercase letters while keeping original casing intact.
- **Input Validation:** Rejects invalid non-integer shifts and out-of-bounds keys with clear error messaging.
- **Convenience Functions:** Modular `encrypt()` and `decrypt()` helper functions built on top of `str.maketrans()`.

## Usage

```python
from caesar import decrypt, encrypt

# Encrypt a plaintext message
ciphertext = encrypt("Hello World", 3)
print(ciphertext)  # Output: Khoor Zruog

# Decrypt a ciphertext message
plaintext = decrypt(ciphertext, 3)
print(plaintext)  # Output: Hello World
