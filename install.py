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
    os.system('cls')
    print(f"{colors.BOLD}{colors.OKGREEN}{bacon.NAME} Installer {bacon.VERSION} {colors.ENDC}")
    if progress == 0:
        print("BACON CLASS", "[----]")
    elif progress == 1:
        print("BACON CLASS", "[=---]")
    elif progress == 2:
        print("BACON CLASS", "[==--]")
    elif progress == 3:
        print("BACON CLASS", "[===-]")
    elif progress == 4:
        print("BACON CLASS", "[====]")
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
            bclass()
            nl()
            setup.write(f"   VERSION = '{bacon.NAME}'")
            progress = 2
            time.sleep(0.5)
            bclass()
            nl()
            setup.write(f"   UPDATE = {bacon.UPDATE}")
            progress = 3
            time.sleep(0.5)
            bclass()
            nl()
            setup.write(f"   NAME = '{bacon.VERSION}'")
            progress = 4
            time.sleep(0.5)
            bclass()
