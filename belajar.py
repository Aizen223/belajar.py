#modul
import os
import sys
import time


print ("jawab dengan benar")
print ("lalu tekan enter")
input("nama :")
input("alamat :")
input("umur :")
time.sleep(1)
print ("biasakan wajah anda")
time.sleep(2)
os.system("clear")
os.system("figlet BIOTAS")

def menu():
     print ("+==================+")
     print ("username :aizen")
     print ("facebook :aizen")
     print ("+==================+")
     print ("1.update & upgrade")
     print ("2.install git")
     print ("3.exit")
     time.sleep(1)
     pil = (input("pilih no :"))
     if pil == "1":
         os.system("pkg update && pkg upgrade")
     elif pil == "2":
         os.system("pkg install git")
     elif pil == "3":
         print ("exit")
     else:
         print ("input salah")
menu()