class bacon:
    VERSION = "0.0.1"
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
