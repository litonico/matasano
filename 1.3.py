import binascii
import pwnlib.util.fiddling as fiddling

def _out(bytestring):
    print("bytestring: ", bytestring)
    print("hex: ", binascii.hexlify(bytestring))

cipher = binascii.unhexlify(b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

def letter_frequency(s, letter):
    return s.count(letter) / len(s)

def squared_error(s, letter, expected):
    return (letter_frequency(s, letter) - expected)**2

def error_vs_english(s):
    return squared_error(s, b'e', 0.120) + \
           squared_error(s, b't', 0.091) + \
           squared_error(s, b'a', 0.081) + \
           squared_error(s, b'o', 0.076) + \
           squared_error(s, b'i', 0.073) + \
           squared_error(s, b'n', 0.069) + \
           squared_error(s, b's', 0.062) + \
           squared_error(s, b'r', 0.060) + \
           squared_error(s, b'h', 0.059) + \
           squared_error(s, b'd', 0.043) + \
           squared_error(s, b'l', 0.040) + \
           squared_error(s, b'u', 0.028) + \
           squared_error(s, b'c', 0.027) + \
           squared_error(s, b'm', 0.026) + \
           squared_error(s, b'f', 0.023) + \
           squared_error(s, b'y', 0.021) + \
           squared_error(s, b'w', 0.021) + \
           squared_error(s, b'g', 0.020) + \
           squared_error(s, b'p', 0.018) + \
           squared_error(s, b'b', 0.015) + \
           squared_error(s, b'v', 0.011) + \
           squared_error(s, b'k', 0.006) + \
           squared_error(s, b'x', 0.001) + \
           squared_error(s, b'q', 0.001) + \
           squared_error(s, b'j', 0.001) + \
           squared_error(s, b'z', 0.001) + \
           squared_error(s, b'*', 0.000)

def score(cipher, key):
    plain = fiddling.xor(cipher, key)
    error = error_vs_english(plain)
    return [error, key, plain]

key_scores = [score(bytes([k]), cipher) for k in range(255)]
_out(
    min(key_scores, key=lambda x: x[0])[2]
)
