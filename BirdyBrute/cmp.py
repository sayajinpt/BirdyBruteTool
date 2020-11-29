from time import sleep
import time
import os   


def cmp1():
    print("COMPARING....")
    sleep(0.2)
    with open('BTC/IN/DB.txt', 'r') as file1:
        with open('BTC/OUT/addr.txt', 'r') as file2:
            same = set(file1).intersection(file2)

    same.discard('\n')

    with open('BTC/OUT/found.txt', 'w') as file_out:
        for line in same:
            file_out.write(line)
            print("FOUND", line)
            sleep(9999999999)
                    
    file1 = 'BTC/OUT/found.txt'
    if os.stat(file1).st_size == 0:
        f = open("BTC/OUT/addr.txt", "r+")
        f.seek(0)
        f.truncate()
        print("- - - -"+"...")
        sleep(0.2)
        print("- - - - - - - - - "+"FILE addr.txt CLEAN")
        sleep(0.2)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - -"+"OK")
        
        sleep(1)
        
        f = open("BTC/OUT/PrvKeys.txt", "r+")
        f.seek(0)
        f.truncate()
        print("- - - -"+"...")
        sleep(0.2)
        print("- - - - - - - - - "+"FILE PrvKeys.txt CLEAN")
        sleep(0.2)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - -"+"OK")
        clear = lambda: os.system('cls')
        clear()
        
    if os.stat(file1).st_size != 0:
        print("====FILE NOT EMPTY====")
        sleep(99999999)
        
def cmp2():
    print("COMPARING....")
    sleep(0.2)
    with open('ETH/IN/DB.txt', 'r') as file1:
        with open('ETH/OUT/addr.txt', 'r') as file2:
            same = set(file1).intersection(file2)

    same.discard('\n')

    with open('ETH/OUT/found.txt', 'w') as file_out:
        for line in same:
            file_out.write(line)
            print("FOUND", line)
            sleep(9999999999)
                    
    file1 = 'ETH/OUT/found.txt'
    if os.stat(file1).st_size == 0:
        f = open("ETH/OUT/addr.txt", "r+")
        f.seek(0)
        f.truncate()
        print("- - - -"+"...")
        sleep(0.2)
        print("- - - - - - - - - "+"FILE addr.txt CLEAN")
        sleep(0.2)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - -"+"OK")
        
        sleep(1)
        
        f = open("ETH/OUT/PrvKeys.txt", "r+")
        f.seek(0)
        f.truncate()
        print("- - - -"+"...")
        sleep(0.2)
        print("- - - - - - - - - "+"FILE PrvKeys.txt CLEAN")
        sleep(0.2)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - -"+"OK")
        clear = lambda: os.system('cls')
        clear()
        
    if os.stat(file1).st_size != 0:
        print("====FILE NOT EMPTY====")
        sleep(99999999)


        



