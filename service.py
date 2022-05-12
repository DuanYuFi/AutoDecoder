from main import BFS as detector
from scapy.all import *

import decode

decode_methods = []
methods = decode.__dict__
for each in methods:
    if each.startswith('un'):
        decode_methods.append(methods[each])

def capture(x):
    payload = x[TCP].payload
    if isinstance(payload, NoPayload):
        return
    
    data = payload.load.strip()
    # print(data)
    res = detector(data, decode_methods, [], 5)
    if len(res) != 0:
        print('\n' + '= ' * 20)
        print("Threat Found, from", x[IP].src, " to", x[IP].dst)
        for result, chains in res:
            print("result:", result)
            if len(chains) == 0:
                print("No encode")
                continue
            if isinstance(chains[0], tuple):
                print(str(chains[0][0])[10:-23] + '(%d)' % chains[0][1], end='')
            else:
                print(str(chains[0])[10:-23], end='')
            for chain in chains[1:]:
                if isinstance(chain, tuple):
                    print(" ->", str(chain[0])[10:-23] + "(%d)" % chain[1], end='')
                else:
                    print(" ->", str(chain)[10:-23], end='')
        
        print("")
            

def main():

    print(ifaces)
    idx = input("Input interface index: ").strip()
    iface = ifaces.dev_from_index(int(idx))
    print("Service running...")
    sniff(filter='tcp', iface=iface, prn=capture)

if __name__ == "__main__":
    main()