from time import sleep
import time
import os   
from multiprocessing import Pool
import subprocess
from timeit import default_timer as timer
from secrets import token_bytes
from coincurve import PublicKey
from hashlib import sha3_256
from web3 import Web3
import multiprocessing


cores = 4


def eth():
    
    global num_threads 
    for n in range(10000):
        start = time.time()
        private_key = sha3_256(token_bytes(32)).digest()
        public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
        addr = sha3_256(public_key).digest()[-20:]
        addr1 = addr.hex()
        address = Web3.toChecksumAddress(addr1)
        priv = private_key.hex()

        f1 = open("ETH/OUT/addr.txt","a")
        f1.write(address+ ' ' +"\n")
        f2 = open("ETH/OUT/PrvKeys.txt","a")
        f2.write(priv+ ' ' +"\n")
        f1.close()
        f1.close()
        end = time.time()
        print('time/s', (end - start))

  
    
    

if __name__ == '__main__':
    jobs = []    
    for r in range(cores):
        p = multiprocessing.Process(target=eth)
        jobs.append(p)
        p.start()


        



