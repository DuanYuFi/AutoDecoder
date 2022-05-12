import string
charset = string.printable.encode()

def avaliable(s: bytes):
    for each in s:
        if each not in charset:
            return False
    return True