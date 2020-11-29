from time import sleep
import os   
import bitcoin, base58, ecdsa, requests, smtplib, multiprocessing, blockchain
from bitcoin import *
import subprocess
from multiprocessing import Pool
from timeit import default_timer as timer
from secrets import token_bytes
from coincurve import PublicKey
from hashlib import sha3_256
from web3 import Web3
from cmp import cmp1, cmp2


def menu():

    print ("__________.__           .___       __________                __           ___________           .__")   
    print ("\______   \__|______  __| _/__.__. \______   \_______ __ ___/  |_  ____  /___    ___/___   ____ |  |")  
    print (" |    |  _/  \_  __ \/ __ <   |  |  |    |  _/\_  __ \  |  \   __\/ __ \    |    | /  _ \ /  _ \|  |")  
    print (" |    |   \  ||  | \/ /_/ |\___  |  |    |   \ |  | \/  |  /|  | \  ___/    |    |(  <_> |  <_> )  |__")
    print (" |______  /__||__|  \____ |/ ____|  |______  / |__|  |____/ |__|  \___  >   |____| \____/ \____/|____/")
    print ("        \/               \/\/              \/                         \/")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("- - - - -###################################")
    print("- - - - -## BTC                       = 1"+" ##")                            
    print("- - - - -## ETH                       = 2"+" ##")       
    print("- - - - -###################################")   
    print(" ")   

   
    op1 = 1 
    op2 = 2
 
  
    option = int(input("- - - - - - - - - - - - - - - - - - - - ------> OPTION : "))
    
                 
    
    if option == op1:
        clear = lambda: os.system('cls')
        clear()
        print("BTC CRACKER WILL USE 4 CORES, CHANGE NUMBER IN FILE FOR DIFFERENT AMOUNT")
        sleep(2)
        for i in range(1000):
            os.system("python btc.py")
            cmp1()
            
        
        
    if option == op2:
        clear = lambda: os.system('cls')
        clear()
        
        print("ETH CRACKER WILL USE 4 CORES, CHANGE NUMBER IN FILE FOR DIFFERENT AMOUNT")
        sleep(2)
      
        for i in range(1000):
            os.system("python eth.py")
            cmp2()
        
   
    else:
        if option != 1 or 2:
            
            print("########______INVALID OPTION______########")
            sleep(2)
            clear = lambda: os.system('cls')
            clear()
            return menu()

if __name__=="__main__": 
    menu()
            
    
    

 


