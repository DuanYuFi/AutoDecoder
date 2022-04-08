from base64 import b64decode, b85decode, b16decode, b32decode, urlsafe_b64decode
import re
import string

from base58 import b58decode

from patterns import *

def matchTarget(code: bytes):
    return re.match(TARGET, code) is not None

def unhex(code: bytes):
    if re.match(HEX, code) is None:
        return None
    return bytes.fromhex(code.decode())

def unbase64(code: bytes):
    if re.match(BASE64, code) is None:
        return None
    return b64decode(code)

def unbase58(code: bytes):
    if re.match(BASE58, code) is None:
        return None
    return b58decode(code)

def unbase32(code: bytes):
    if re.match(BASE32, code) is None:
        return None
    return b32decode(code)

def unbase16(code: bytes):
    if re.match(BASE16, code) is None:
        return None
    return b16decode(code)

def unbase85(code: bytes):
    if re.match(BASE85, code) is None:
        return None
    return b85decode(code)

def unurlsafe_base64(code: bytes):
    if re.match(URLSAFE_BASE64, code) is None:
        return None
    return urlsafe_b64decode(code)