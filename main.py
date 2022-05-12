import decode
import decrypt
import queue
from utils import avaliable
from hashlib import sha256

def BFS(code: bytes, decode_methods: list, decrypt_methods: list, max_depth:int=10):
    
    decoded = [code]
    bfs = queue.Queue()
    bfs.put((code, [], 0))
    result = []
    while not bfs.empty():
        this_code, chain, depth = bfs.get()
        if depth > max_depth:
            continue
        # print(this_code)
        # input()
        for method in decode_methods:
            try:
                decoded_code = method(this_code)
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except Exception as e:
                # print("error:", e)
                continue

            if decoded_code is None:
                continue
            hashcode = sha256(decoded_code).digest()
            if hashcode in decoded:
                continue
            decoded.append(hashcode)
            # print(this_code, method)
            bfs.put((decoded_code, chain + [method], depth + 1))
        
        for method in decrypt_methods:
            for key in range(256):
                decrypt_code = method(this_code, key)
                if not avaliable(decrypt_code):
                    continue
                hashcode = sha256(decrypt_code).digest()
                if hashcode in decoded:
                    continue
                decoded.append(hashcode)
                bfs.put((decrypt_code, chain + [(method, key)], depth + 1))
        
        if decode.matchTarget(this_code):
            result.append((this_code, chain))
    
    return result

def codeChain(code: bytes, methods: list):
    result = code
    for method in methods:
        result = method(result)
    
    return result

if __name__ == "__main__":
    
    import sys
    if len(sys.argv) > 1:
        file = sys.argv[1]
    
    else:
        file = "code.bin"
    with open(file, 'rb') as f:
        code = f.read()
    
    print(code)
    decode_methods = []
    methods = decode.__dict__
    for each in methods:
        if each.startswith('un'):
            decode_methods.append(methods[each])
    
    decrypt_methods = []
    methods = decrypt.__dict__
    for each in methods:
        if each.endswith('_decrypt'):
            decrypt_methods.append(methods[each])

    res = BFS(code, decode_methods, decrypt_methods, 5)
    # print(res[0][1])
    for result, chains in res:
        print("result:", result)
        if isinstance(chains[0], tuple):
            print(str(chains[0][0])[10:-23] + '(%d)' % chains[0][1], end='')
        else:
            print(str(chains[0])[10:-23], end='')
        for chain in chains[1:]:
            if isinstance(chain, tuple):
                print(" ->", str(chain[0])[10:-23] + "(%d)" % chain[1], end='')
            else:
                print(" ->", str(chain)[10:-23], end='')
        
        print('\n' + '= ' * 20)