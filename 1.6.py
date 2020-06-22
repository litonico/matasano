import binascii
import pwnlib.util.fiddling as fiddling
from collections import namedtuple

cipher = fiddling.b64d("""
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
""")

def _in(hexstring):
    return binascii.unhexlify(hexstring)

def _out(bytestring):
    print("bytestring: ", bytestring)
    print("hex: ", binascii.hexlify(bytestring))

def hamming(bytestring1, bytestring2):
    byte_pairs = zip(fiddling.bits(bytestring1), fiddling.bits(bytestring2))
    total = 0
    for (b1, b2) in byte_pairs:
        if b1 != b2:
            total += 1
    return total

assert hamming(b"this is a test", b"wokka wokka!!!") == 37

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
           squared_error(s, b'*', 0.000) + \
           squared_error(s, b'?', 0.000) + \
           squared_error(s, b'`', 0.000) + \
           squared_error(s, b'0', 0.000) + \
           squared_error(s, b'1', 0.000) + \
           squared_error(s, b'2', 0.000) + \
           squared_error(s, b'3', 0.000) + \
           squared_error(s, b'4', 0.000) + \
           squared_error(s, b'5', 0.000) + \
           squared_error(s, b'6', 0.000) + \
           squared_error(s, b'7', 0.000) + \
           squared_error(s, b'8', 0.000) + \
           squared_error(s, b'9', 0.000) + \
           squared_error(s, b':', 0.000) + \
           squared_error(s, b'=', 0.000) + \
           squared_error(s, b'[', 0.000) + \
           squared_error(s, b']', 0.000) + \
           squared_error(s, b'<', 0.000) + \
           squared_error(s, b'$', 0.000) + \
           squared_error(s, b'%', 0.000) + \
           squared_error(s, b'!', 0.000) + \
           squared_error(s, b'^', 0.000) + \
           squared_error(s, b'&', 0.000) + \
           squared_error(s, b'#', 0.000) + \
           squared_error(s, b'(', 0.000) + \
           squared_error(s, b')', 0.000) + \
           squared_error(s, b'?', 0.000) + \
           squared_error(s, b':', 0.000) + \
           squared_error(s, b';', 0.000)

KeyScore = namedtuple("KeyScore", "normalized_edit_distance key_size")
def key_size_score(key_size):
    first = cipher[key_size * 0:key_size * 1]
    second = cipher[key_size * 1:key_size * 2]
    third = cipher[key_size * 2:key_size * 3]
    fourth = cipher[key_size * 3:key_size * 4]
    avg_norm_edit_distance = (
            (hamming(first, second) / key_size) + \
            (hamming(first, third) / key_size) + \
            (hamming(first, fourth) / key_size) + \
            (hamming(second, third) / key_size) + \
            (hamming(second, fourth) / key_size) + \
            (hamming(third, fourth) / key_size)
    ) / 2
    return KeyScore(avg_norm_edit_distance, key_size)

key_scores = [key_size_score(key_size) for key_size in range(2,40)]
best_key_sizes_by_score = list(map(lambda x: x.key_size, sorted(key_scores, key=lambda x: x.normalized_edit_distance)))

def columns(bytestring, n):
    for i in range(n):
        yield bytestring[i::n]

MatchesEnglishScore = namedtuple("MatchesEnglishScore", "error key plain")
def best_english_score(cipher):
    def score(key):
        plain = fiddling.xor(cipher, key)
        error = error_vs_english(plain)
        return MatchesEnglishScore(error, key, plain)

    key_scores = [score(bytes([k])) for k in range(255)]
    return min(key_scores, key=lambda x: x.error)

def find_vigenere_key(key_size):
    return b"".join(map(lambda x: x.key, [best_english_score(column) for column in columns(cipher, key_size)]))

print(find_vigenere_key(best_key_sizes_by_score[0]))
