class bacon:
    VERSION = "0.0.1"
    UPDATE = False
    NAME = "BaconShell"
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

import time
print(f"{colors.BOLD}{colors.OKGREEN}baconShell Installer {bacon.VERSION} {colors.ENDC}")
print("This app installs baconShell on your computer")
print("[A] Upgrade Installation")
print("[B] Clean Installation")
stg1 = True
while stg1 == True:
    a = ["a", "A", "[A]"]
    option = input()
    if option in a:
        if bacon.UPDATE == False:
            print(f"{colors.WARNING}⚠️INSUFFICIENT VERSION⚠️{colors.ENDC} {colors.BOLD}{colors.FAIL}Requires Clean Install.{colors.ENDC}")
