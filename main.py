from utils import *
import queue
from hashlib import sha256

def BFS(code: bytes, methods: list):
    
    decoded = [code]
    bfs = queue.Queue()
    bfs.put((code, []))
    result = []
    while not bfs.empty():
        this_code, chain = bfs.get()
        # print(this_code)
        # input()
        for method in methods:      
            decoded_code = method(this_code)
            if decoded_code is None:
                continue
            hashcode = sha256(decoded_code).digest()
            if hashcode in decoded:
                continue
            decoded.append(hashcode)
            bfs.put((decoded_code, chain + [method]))
            
        
        if matchTarget(this_code):
            result.append((this_code, chain))
    
    return result

def codeChain(code: bytes, methods: list):
    result = code
    for method in methods:
        result = method(result)
    
    return result

if __name__ == "__main__":
    
    import sys
    file = sys.argv[1]
    with open(file, 'rb') as f:
        code = f.read()
    
    decode_methods = [unhex, unbase16, unbase32, unbase58, unbase64, unbase85, unurlsafe_base64]
    res = BFS(code, decode_methods)
    
    for result, chains in res:
        print("result:", result)
        print(str(chains[0])[10:-23], end='')
        for chain in chains[1:]:
            print(" ->", str(chain)[10:-23], end='')
        
        print('\n' + '= ' * 20)