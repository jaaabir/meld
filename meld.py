#!/bin/python3

import random as r
import sys
import os
import time
import threading as t


arg = sys.argv

def gen():
    print()
    print("[*] Generating .." , end = '')
    for i in range(6):
        print("." * 5 , end = '')
        time.sleep(0.4)
        
def banner():

    banners = [
        '''
                 ███╗░░░███╗███████╗██╗░░░░░██████╗░
                 ████╗░████║██╔════╝██║░░░░░██╔══██╗
                 ██╔████╔██║█████╗░░██║░░░░░██║░░██║
                 ██║╚██╔╝██║██╔══╝░░██║░░░░░██║░░██║
                 ██║░╚═╝░██║███████╗███████╗██████╔╝
                 ╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═════╝░''' ,

        '''
               
       █████████████████████████████████████████████████████████████████████
       █░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░░░░░░░███
       █░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀░░░░█
       █░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░░░▄▀▄▀░░█
       █░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█
       █░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█
       █░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█
       █░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█
       █░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█
       █░░▄▀░░██████████░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░▄▀▄▀░░█
       █░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█
       █░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░███
       █████████████████████████████████████████████████████████████████████ '''
        ,

      '''
                           ▛▚▞▜ █☰ ▙▄ ◗ ''']

    banner = r.choice(banners)
    print(banner)

def save_file(procs , name):
    with open(name+'_wordlist.txt' , 'a' ) as file:
        file.write(str(procs))
        file.write("\n")

def dup(numb):

    new_numb = []
    dup = []
    for i in numb:
        if i not in new_numb:
            new_numb.append(i)
            
        else:
            dup.append(i)

    return new_numb

def proc_single(name , num):

    num_len = int(len(num))
    sq_num_len = int(num_len) ** int(num_len)
    sp_num = list(num)
    print()
    for n in sp_num:

        nm_n = name + n
        print(nm_n)
        save_file(nm_n , name)

    for n in sp_num:

        n_nm = n + name
        print(n_nm)
        save_file(n_nm , name)

def proc_fully(name , num):

    num_len = int(len(num))
    sq_num_len = int(num_len) ** int(num_len)
    sp_num = list(num)

    #for n in sp_num:
    #    print(name+n)
    #for n in sp_num:
    #    print(n+name)

    stored_nums = []
    
    for _ in range(1,sq_num_len * 2):

        joined_nums = ''
        r.shuffle(sp_num)
        for i in sp_num:
            joined_nums += i    
        stored_nums.append(joined_nums)    
    

    no_dup = dup(stored_nums)   
    
    for i in no_dup:

        nm_i = name + i
        print(nm_i)
        save_file(nm_i , name)
        
    for i in no_dup:

        i_nm = i + name
        print(i_nm)
        save_file(nm_i , name)     


if len(arg) != 3 :

    print()
    print('[-] Error : please provide 2 argument')
    print('[-] Syntax : python <name or char> <char or number>')
    #print(len(arg))

else :
    try :
        name = arg[1]
        num = arg[2]

        banner()

        print()

        gen = t.Thread( target = gen )
        gen.start()
        gen.join()
        
        print()

        #proc( name , num )

        thread1 = t.Thread(target = proc_single , args = (name,num ))
        thread3 = t.Thread(target = proc_fully , args = (name , num))

        thread1.start()

        thread3.start()

        
        thread1.join()
        thread3.join()

        pwd = os.getcwd()
        print("\n",f"[+] Saved the worldlist in {pwd}")

    except :
        
        print("\n[-] ERROR .....................")
        print("[-] Check the syntax ")
        print("[+] [-] Syntax : python <name or char> <char or number>")
