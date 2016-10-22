# ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # !
# !                       Zip Cracker                       # !
# !                                                         # !
# !     Written in Python v2.7.11                           # !
# !                                                         # !
# !     Author: jokyjoe (a.k.a. GERIKO7!, JustIce)          # !
# !                                                         # !
# !     Purpose: Showcase , test                            # !
# !                                                         # !
# !     Written within 5 hours.                             # !
# !     Stability (1-10): 6                                 # !
# !                                                         # !
# !     Done? No.                                           # !
# !     Licensed: No.                                       # !
# !     Feel free to edit, publish and use the code.        # !
# !                                                         # !
# !     By reading, viewing, using or/and editing the code, # !
# !     You accept the Terms of Use describe below.         # !
# !                                                         # !
# !                      Terms of Use                       # !
# !                                                         # !
# !     I (the Author, jokyjoe) am not responsible for any  # !
# !     damage, harm, loss and/or trouble You, the user,    # !
# !     cause, inflict. After downloading, viewing, editing # !
# !     or/and using the following code, software, You take # !
# !     responsibility for Your actions using It.           # !
# !                                                         # !
# !     By reading, viewing, using or/and editing the code, # !
# !     You accept the Terms of Use described above.        # !
# ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! 
import itertools
import os.path
import sys
import zipfile
import time
import subprocess
from datetime import datetime
def clear():
    os.system('cls')
alphabet = ""
# SETTINGS
clear()
print "Enable lowercase letters?"
print "(Y/N)"
menuc = raw_input(">> ")
if menuc.lower() == "y":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
clear()
print "Enable uppercase letters?"
print "(Y/N)"
menuc = raw_input(">> ")
if menuc.lower() == "y":
    alphabet = alphabet + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
clear()
print "Enable numbers?"
print "(Y/N)"
menuc = raw_input(">> ")
if menuc.lower() == "y":
    alphabet = alphabet + "0123456789"
clear()
print "Enable symbols? ('.,!?$@%^', etc...)"
print "(Y/N)"
menuc = raw_input(">> ")
if menuc.lower() == "y":
    alphabet = alphabet + "'!?$%^@*()_-+={[}]:;@'~#|\<,>.?/" + '"'
clear()
print "Show current password and length? (= UI = slower performance)"
print "(Y/N)"
menuc = raw_input(">> ")
if menuc.lower() == "y":
    enableGUI = True
else:
    enableGUI = False
clear()
try:
    print sys.argv[2]
    try:
        n = int(sys.argv[2])
    except:
        print "Set the password estimated length."
        print "If you don't know it, type '1'."
        print "Default : 1"
        try:
            n = int(raw_input(">> "))
        except:
            n = 1
except:
    print "Set the password estimated length."
    print "If you don't know it, type '1'."
    print "Default : 1"
    try:
        n = int(raw_input(">> "))
    except:
        n = 1
# SETTINGS ABOVE
FNULL = open(os.devnull, 'w')
clear()
print "Starting..."

data = ''
sat = 0
bad = 0
"""
if os.path.isfile('wordlist.txt'):
    passfile = open('wordlist.txt','w')
    passfile.truncate(0)
else:
    passfile = open('wordlist.txt','w')
"""
now = datetime.now().strftime('%H:%M:%S')
while True:
    for xs in itertools.product(alphabet, repeat=n):
        if enableGUI == True:
            clear()
            print "Passwd : %s" % ''.join(xs)
            print "Length : %d" % n
        """
        passfile.write(''.join(xs))
        """
        data = zipfile.ZipFile(sys.argv[1], 'r')
        try:
            data.extractall('crackedzip', data.namelist(), ''.join(xs))
            end = datetime.now().strftime('%H:%M:%S')
            end = end.split(':')
            hrs = end[0]
            min = end[1]
            sec = end[2]
            now = now.split(':')
            nhrs = now[0]
            nmin = now[1]
            nsec = now[2]
            hrs = int(hrs) - int(nhrs)
            min = int(min) - int(nmin)
            sec = int(sec) - int(nsec)
            if sec < 0:
                min-=1
                sec+=60
            if min < 0:
                hrs-=1
                min+=60
            clear()
            print "It took %d hours, %d minutes and %d seconds" % (hrs,min,sec)
            print "CRACKED!"
            print "Password is: %s" % ''.join(xs)
            raw_input()
            break
        except RuntimeError:
            # BAD PASSWORD
            continue
        except:
            test = ''.join(xs)
            try:
                data.extractall('crackedzip', data.namelist(), test)
                end = datetime.now().strftime('%H:%M:%S')
                end = end.split(':')
                hrs = end[0]
                min = end[1]
                sec = end[2]
                now = now.split(':')
                nhrs = now[0]
                nmin = now[1]
                nsec = now[2]
                hrs = int(hrs) - int(nhrs)
                min = int(min) - int(nmin)
                sec = int(sec) - int(nsec)
                if sec < 0:
                    min-=1
                    sec+=60
                if min < 0:
                    hrs-=1
                    min+=60
                clear()
                print "It took %d hours, %d minutes and %d seconds" % (hrs,min,sec)
                print "CRACKED!"
                print "Password is: %s" % ''.join(xs)
                raw_input()
                break
            except RuntimeError:
                continue
            except:
                continue
        """
        except:
            print "Error"
            e = sys.exc_info()[0]
            print e
            raw_input()
            continue
        """
    n+=1
passfile.close()
# ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # !
# !                       Zip Cracker                       # !
# !                                                         # !
# !     Written in Python v2.7.11                           # !
# !                                                         # !
# !     Author: jokyjoe (a.k.a. GERIKO7!, JustIce)          # !
# !                                                         # !
# !     Purpose: Showcase , test                            # !
# !                                                         # !
# !     Written within 5 hours.                             # !
# !     Stability (1-10): 6                                 # !
# !                                                         # !
# !     Done? No.                                           # !
# !     Licensed: No.                                       # !
# !     Feel free to edit, publish and use the code.        # !
# !                                                         # !
# !     By reading, viewing, using or/and editing the code, # !
# !     You accept the Terms of Use describe below.         # !
# !                                                         # !
# !                      Terms of Use                       # !
# !                                                         # !
# !     I (the Author, jokyjoe) am not responsible for any  # !
# !     damage, harm, loss and/or trouble You, the user,    # !
# !     cause, inflict. After downloading, viewing, editing # !
# !     or/and using the following code, software, You take # !
# !     responsibility for Your actions using It.           # !
# !                                                         # !
# !     By reading, viewing, using or/and editing the code, # !
# !     You accept the Terms of Use described above.        # !
# ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! # ! 