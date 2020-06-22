import binascii
import pwnlib.util.fiddling as fiddling

def _in(hexstring):
    return binascii.unhexlify(hexstring)

def _out(bytestring):
    print("bytestring: ", bytestring)
    print("hex: ", binascii.hexlify(bytestring))

plain = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = "ICE"

_out(fiddling.xor(plain, key))

