import binascii
import pwnlib.util.fiddling as fiddling

cipher = binascii.unhexlify(b'1c0111001f010100061a024b53535009181c')
key = binascii.unhexlify(b'686974207468652062756c6c277320657965')

print(
    binascii.hexlify(fiddling.xor(cipher, key))
)
