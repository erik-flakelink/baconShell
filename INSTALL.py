class bacon:
    VERSION = "0.0.2"
    UPDATE = False
    NAME = "baconShell"
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def nl():
    setup.write("\n")
def bclass():
    print(f"{colors.BOLD}{colors.OKGREEN}{bacon.NAME} Installer {bacon.VERSION} {colors.ENDC}")
    if progress == 0:
        print("BACON CLASS", "[----] 0%")
    elif progress == 1:
        print("BACON CLASS", "[=---] 25%")
    elif progress == 2:
        print("BACON CLASS", "[==--] 50%")
    elif progress == 3:
        print("BACON CLASS", "[===-] 75%")
    elif progress == 4:
        print("BACON CLASS", "[====] 100%")
def cclass():
    if progress2 == 0:
        print("COLORS CLASS", "[----------] 0%")
    elif progress2 == 1:
        print("COLORS CLASS", "[=---------] 10%")
    elif progress2 == 2:
        print("COLORS CLASS", "[==--------] 20%")
    elif progress2 == 3:
        print("COLORS CLASS", "[===-------] 30%")
    elif progress2 == 4:
        print("COLORS CLASS", "[====------] 40%")
    elif progress2 == 5:
        print("COLORS CLASS", "[=====-----] 50%")
    elif progress2 == 6:
        print("COLORS CLASS", "[======----] 60%")
    elif progress2 == 7:
        print("COLORS CLASS", "[=======---] 70%")
    elif progress2 == 8:
        print("COLORS CLASS", "[========--] 80%")
    elif progress2 == 9:
        print("COLORS CLASS", "[=========-] 90%")
    elif progress2 == 10:
        print("COLORS CLASS", "[==========] 100%")
def iclass():
    if progress3 == 0:
        print("IMPORTS", "[----] 0%")
    elif progress3 == 1:
        print("IMPORTS", "[=---] 25%")
    elif progress3 == 2:
        print("IMPORTS", "[==--] 50%")
    elif progress3 == 3:
        print("IMPORTS", "[===-] 75%")
    elif progress3 == 4:
        print("IMPORTS", "[====] 100%")
def session():
    if prog == 0:
        print("SESSION", "[-----] 0%")
    elif prog == 1:
        print("SESSION", "[=----] 20%")
    elif prog == 2:
        print("SESSION", "[==---] 40%")
    elif prog == 3:
        print("SESSION", "[===--] 60%")
    elif prog == 4:
        print("SESSION", "[====-] 80%")
    elif prog == 5:
        print("SESSION", "[=====] 100%")
def com():
    if progress4 == 0:
        print("COMMANDS", "[------] 0%")
    elif progress4 == 1:
        print("COMMANDS", "[=-----] 17%")
    elif progress4 == 2:
        print("COMMANDS", "[==----] 33%")
    elif progress4 == 3:
        print("COMMANDS", "[===---] 50%")
    elif progress4 == 4:
        print("COMMANDS", "[====--] 66%")
    elif progress4 == 5:
        print("COMMANDS", "[=====-] 83%")
    elif progress4 == 6:
        print("COMMANDS", "[======] 100%")
import os
import time
print(f"{colors.BOLD}{colors.OKGREEN}{bacon.NAME} Installer {bacon.VERSION} {colors.ENDC}")
print("This app installs baconShell on your computer")
print("[A] Upgrade Installation")
print("[B] Clean Installation")
stg1 = True
progress = 0
while stg1 == True:
    a = ["a", "A", "[A]"]
    b = ["b", "B", "[B]"]
    option = input()
    if option in a:
        if bacon.UPDATE == False:
            print(f"{colors.WARNING}⚠️INSUFFICIENT VERSION⚠️{colors.ENDC} {colors.BOLD}{colors.FAIL}Requires Clean Install.{colors.ENDC}")
    if option in b:
        with open("SYSTEM.py", 'w') as setup:
            setup.write(f"class bacon:")
            progress = 1
            time.sleep(0.5)
            os.system('cls')
            bclass()
            nl()
            setup.write(f"   VERSION = '{bacon.NAME}'")
            progress = 2
            time.sleep(0.5)
            os.system('cls')
            bclass()
            nl()
            setup.write(f"   UPDATE = {bacon.UPDATE}")
            progress = 3
            time.sleep(0.5)
            os.system('cls')
            bclass()
            nl()
            setup.write(f"   NAME = '{bacon.VERSION}'")
            progress = 4
            time.sleep(0.5)
            os.system('cls')
            bclass()
            nl()
            setup.write(f"class colors:")
            progress2 = 1
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            nl()
            setup.write(f"  HEADER = '\033[95m'")
            progress2 = 2
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            nl()
            setup.write(f"  OKBLUE = '\033[94m'")
            progress2 = 3
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            nl()
            setup.write(f"  OKCYAN = '\033[96m'")
            progress2 = 4
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            nl()
            setup.write(f"  OKGREEN = '\033[92m'")
            progress2 = 5
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            nl()
            setup.write(f"  WARNING = '\033[93m'")
            progress2 = 6
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            nl()
            setup.write(f"  FAIL = '\033[91m'")
            progress2 = 7
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            nl()
            setup.write(f"  ENDC = '\033[0m'")
            progress2 = 8
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            nl()
            setup.write(f"  BOLD = '\033[1m'")
            progress2 = 9
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            nl()
            setup.write(f"  UNDERLINE = '\033[4m'")
            progress2 = 10
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            nl()
            setup.write(f"import os")
            progress3 = 1
            time.sleep(0.5)
            os.system('cls')
            bclass()
            cclass()
            iclass()
            nl()
            setup.write(f"import shutil;import platform")
            progress3 = 2
            time.sleep(0.5)
            os.system('cls')
            bclass()
            cclass()
            iclass()
            nl()
            setup.write(f"import time;import sys")
            progress3 = 3
            time.sleep(0.5)
            os.system('cls')
            bclass()
            cclass()
            iclass()
            nl()
            setup.write(f"import subprocess\nfrom sys import version_info")
            progress3 = 4
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            iclass()
            nl()
            setup.write(f"print(f'{colors.BOLD}{colors.OKGREEN}{bacon.NAME}{colors.ENDC}')\nsession = True")
            prog = 1
            time.sleep(0.5)
            os.system('cls')
            bclass()
            cclass()
            iclass()
            session()
            nl()
            setup.write(f"def nl():")
            nl()
            setup.write(f"  w.write('\\n')")
            nl()
            setup.write(f"while session == True:")
            prog = 3
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            iclass()
            session()
            nl()
            setup.write(f"  command = input()")
            prog = 5
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            iclass()
            session()
            nl()
            setup.write(f"  if command == 'HOST.os':")
            nl()
            setup.write(f"      print('>', str(platform.system()))")
            nl()
            setup.write(f"  elif command == 'HOST':")
            nl()
            setup.write(f"      print('>', str(platform.system()) + ' ' + str(platform.release()))")
            progress4 = 1
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            iclass()
            session()
            com()
            nl()
            setup.write(f"  elif command == 'HOST.ver':\n")
            setup.write(f"      print('>', str(platform.release()))")
            progress4 = 2
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            iclass()
            session()
            com()
            nl()
            setup.write(f"  elif command == 'HOST.rel':\n")
            setup.write(f"      print('>', str(platform.release()))")
            progress4 = 3
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            iclass()
            session()
            com()
            nl()
            setup.write(f"  elif command == 'BACON':\n")
            setup.write(f"      print('>', '{bacon.NAME}')")
            nl()
            setup.write(f"      print('>', '{bacon.VERSION}')")
            nl()
            setup.write(f"      print('>', 'Update Status: ','{bacon.UPDATE}')")
            nl()
            setup.write(f"  elif command == 'BACON.id':\n")
            setup.write(f"      print('>', '{bacon.NAME}')")
            progress4 = 4
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            iclass()
            session()
            com()
            nl()
            setup.write(f"  elif command == 'BACON.ver':\n")
            setup.write(f"      print('>', '{bacon.VERSION}')")
            progress4 = 5
            time.sleep(1)
            os.system('cls')
            bclass()
            cclass()
            iclass()
            session()
            com()
            nl()
            setup.write(f"  elif command == 'BACON.dump':\n")
            setup.write(f"      with open('UNINSTALL.py', 'w') as w:")
            nl()
            setup.write(f"          w.write('import time')")
            nl()
            setup.write(f"          nl()")
            nl()
            setup.write(f"          w.write('import os')")
            nl()
            setup.write(f"          nl()")
            nl()
            setup.write(f"          w.write('print(\"bacon Uninstaller\")')")
            nl()
            setup.write(f"          nl()")
            nl()
            setup.write(f"          w.write('time.sleep(1)')")
            nl()
            setup.write(f"          nl()")
            nl()
            setup.write(f"          w.write('os.remove(\"SYSTEM.py\")')")
            nl()
            setup.write(f"          nl()")
            nl()
            setup.write(f"          w.write('os.remove(\"INSTALL.py\")')")
            nl()
            setup.write(f"          nl()")
            nl()
            setup.write(f"          w.write('print(\"Uninstall has completed. You may now delete this file.\")')")
            nl()
            setup.write(f"          nl()")
            nl()
            setup.write(f"          w.write('time.sleep(10)')")
            progress4 = 6
            time.sleep(3)
            os.system('cls')
            bclass()
            cclass()
            iclass()
            session()
            com()
            nl()
