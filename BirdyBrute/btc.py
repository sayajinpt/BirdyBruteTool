from time import sleep
import os   
import bitcoin, base58, ecdsa, requests, smtplib, multiprocessing, blockchain
from multiprocessing import Pool
import binascii, hashlib
from bitcoin import *
import subprocess


cores = 4

def btc():
    
    global num_threads
    for n in range(10000):
        start = time.time()
        private_key = random_key()               
        public_key = privtopub(private_key)
        address = pubtoaddr(public_key)
        
        #print(address+ ' ' +private_key)
        f = open("BTC/OUT/addr.txt","a")
        f.write(address+ ' ' +"\n")
        f.close()
        f = open("BTC/OUT/PrvKeys.txt","a")
        f.write(private_key+ ' ' +"\n")
        f.close()
        end = time.time()
        print('time/s', (end - start))
        

                
    

if __name__ == '__main__':
    jobs = []    
    for r in range(cores):
        p = multiprocessing.Process(target=btc)
        jobs.append(p)
        p.start()
        
        
        

         



