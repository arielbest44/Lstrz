from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print('\033[1;36;40m<───────────────[ ARIEL SANDY PERMANA ] ───────────────>')
           print('')
           os.system('date | lolcat')
           print("\033[1;93m")
           print(" \033[1;92m   SUBCRIBE DULU CHANNEL GUA')")
           print("\033[1;93m")
           print("<───────────────[ ARIEL SANDY PERMANA ] ───────────────>")
           print("")
           try:
                x = str(input('\033[1;92mUsername \033[1;93m: '))
                print("")
                e = getpass('\033[1;92mPassword \033[1;93m: ')
                print ("")
                if x=="Ariel" and e=="Ganteng":
                   print('Login Sukses Mohon Tunggu Sebentar...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   os.system('figlet ' + x + ' | lolcat')
                   print('\033[1;92m ────────────────────────────────────── ')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Password/Usr Name Salah")
                      time.sleep(2)
                      print("")
           except Exception:

                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Password/Usr Name Salah")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Password/Usr Name Salah")
                      time.sleep(2)
menu()