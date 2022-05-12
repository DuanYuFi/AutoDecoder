
def xor_decrypt(s: bytes, key: int):
    ret = [each ^ key for each in s]
    return bytes(ret)

'''
def shift_decrypt(s: bytes, key: int):
    ret = [(each + key) % 256 for each in s]
    return bytes(ret)
'''