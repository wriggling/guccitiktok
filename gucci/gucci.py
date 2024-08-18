import hashlib
import json
from time import time
from random import randint, choice
import requests
import random
import string
from copy import deepcopy
from urllib.parse import quote
import os
from os import system
from colorama import Fore, init
import pystyle
from pystyle import Colors, Write, Box, Colorate, Center
from time import sleep

v = Colors.blue_to_purple
rr = Colors.red_to_yellow
er = Colors.red_to_black
wr = Colors.green_to_white
ff = Colors.yellow_to_red
ii = Colors.blue_to_cyan
tt = Colors.red_to_white
cc = Colors.green_to_white
gg = Colors.yellow_to_green

def clear(): return os.system('cls') if os.name == 'nt' else os.system('clear')
os.system("mode con cols=155 lines=40")
system(f"title " + "GUCCI TOOL [@cxcvc on DC]")

def hex_string(num):
    tmp_string = hex(num)[2:]
    if len(tmp_string) < 2:
        tmp_string = '0' + tmp_string
    return tmp_string

def RBIT(num):
    result = ''
    tmp_string = bin(num)[2:]
    while len(tmp_string) < 8:
        tmp_string = '0' + tmp_string
    for i in range(0, 8):
        result = result + tmp_string[7 - i]
    return int(result, 2)

def file_data(path):
    with open(path, 'rb') as f:
        result = f.read()
    return result

def reverse(num):
    tmp_string = hex(num)[2:]
    if len(tmp_string) < 2:
        tmp_string = '0' + tmp_string
    return int(tmp_string[1:] + tmp_string[:1], 16)

class XG:
    def __init__(self, debug):
        self.length = 0x14
        self.debug = debug
        self.hex_CE0 = [0x05, 0x00, 0x50, choice(range(0, 0xFF)), 0x47, 0x1e, 0x00, choice(range(0, 0xFF)) & 0xf0]

    def addr_BA8(self):
        tmp = ''
        hex_BA8 = []
        for i in range(0x0, 0x100):
            hex_BA8.append(i)
        for i in range(0, 0x100):
            if i == 0:
                A = 0
            elif tmp:
                A = tmp
            else:
                A = hex_BA8[i - 1]
            B = self.hex_CE0[i % 0x8]
            if A == 0x05:
                if i != 1:
                    if tmp != 0x05:
                        A = 0
            C = A + i + B
            while C >= 0x100:
                C = C - 0x100
            if C < i:
                tmp = C
            else:
                tmp = ''
            D = hex_BA8[C]
            hex_BA8[i] = D
        return hex_BA8

    def initial(self, debug, hex_BA8):
        tmp_add = []
        tmp_hex = deepcopy(hex_BA8)
        for i in range(self.length):
            A = debug[i]
            if not tmp_add:
                B = 0
            else:
                B = tmp_add[-1]
            C = hex_BA8[i + 1] + B
            while C >= 0x100:
                C = C - 0x100
            tmp_add.append(C)
            D = tmp_hex[C]
            tmp_hex[i + 1] = D
            E = D + D
            while E >= 0x100:
                E = E - 0x100
            F = tmp_hex[E]
            G = A ^ F
            debug[i] = G
        return debug

    def calculate(self, debug):
        for i in range(self.length):
            A = debug[i]
            B = reverse(A)
            C = debug[(i + 1) % self.length]
            D = B ^ C
            E = RBIT(D)
            F = E ^ self.length
            G = ~F
            while G < 0:
                G += 0x100000000
            H = int(hex(G)[-2:], 16)
            debug[i] = H
        return debug

    def main(self):
        result = ''
        for item in self.calculate(self.initial(self.debug, self.addr_BA8())):
            result = result + hex_string(item)

        return '8404{}{}{}{}{}'.format(hex_string(self.hex_CE0[7]), hex_string(self.hex_CE0[3]),
                                       hex_string(self.hex_CE0[1]), hex_string(self.hex_CE0[6]), result)

def X_Gorgon(param, data, cookie):
    gorgon = []
    ttime = time()
    Khronos = hex(int(ttime))[2:]
    url_md5 = hashlib.md5(bytearray(param, 'utf-8')).hexdigest()
    for i in range(0, 4):
        gorgon.append(int(url_md5[2 * i: 2 * i + 2], 16))
    if data:
        if isinstance(data, str):
            data = data.encode(encoding='utf-8')
        data_md5 = hashlib.md5(data).hexdigest()
        for i in range(0, 4):
            gorgon.append(int(data_md5[2 * i: 2 * i + 2], 16))
    else:
        for i in range(0, 4):
            gorgon.append(0x0)
    if cookie:
        cookie_md5 = hashlib.md5(bytearray(cookie, 'utf-8')).hexdigest()
        for i in range(0, 4):
            gorgon.append(int(cookie_md5[2 * i: 2 * i + 2], 16))
    else:
        for i in range(0, 4):
            gorgon.append(0x0)
    gorgon = gorgon + [0x1, 0x1, 0x2, 0x4]
    for i in range(0, 4):
        gorgon.append(int(Khronos[2 * i: 2 * i + 2], 16))
    return {'X-Gorgon': XG(gorgon).main(), 'X-Khronos': str(int(ttime))}

def get_stub(data):
    if isinstance(data, dict):
        data = json.dumps(data)

    if isinstance(data, str):
        data = data.encode(encoding='utf-8')
    if data is None or data == "" or len(data) == 0:
        return "00000000000000000000000000000000"

    m = hashlib.md5()
    m.update(data)
    res = m.hexdigest()
    res = res.upper()
    return res

def get_profile(session_id, device_id, iid):
    try:
        data = None
        parm = (
            f"device_id={device_id}&iid={iid}&id=kaa&version_code=34.0.0&language=en"
            "&app_name=lite&app_version=34.0.0&carrier_region=SA&tz_offset=10800&mcc_mnc=42001"
            "&locale=en&sys_region=SA&aid=473824&screen_width=1284&os_api=18&ac=WIFI&os_version=17.3"
            "&app_language=en&tz_name=Asia/Riyadh&carrier_region1=SA&build_number=340002&device_platform=iphone"
            "&device_type=iPhone13,4"
        )
        url = f"https://api16.tiktokv.com/aweme/v1/user/profile/self/?{parm}"
        headers = {
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": f"sessionid={session_id}",
            "sdk-version": "2",
            "user-agent": "com.zhiliaoapp.musically/432424234 (Linux; U; Android 5; en; fewfwdw; Build/PI;tt-ok/3.12.13.1)",
        }
        response = requests.get(url, headers=headers, cookies={"sessionid": session_id})
        profile_data = response.json()
        print(f"Profile response: {profile_data}")
        return profile_data.get("user", {}).get("unique_id", "None")
    except Exception as e:
        print(f"Exception in get_profile: {e}")
        return "None"

def check_is_changed(last_username, session_id, device_id, iid):
    try:
        current_username = get_profile(session_id, device_id, iid)
        print(f"Current username: {current_username}")
        return not (current_username == last_username)
    except Exception as e:
        print(f"Exception in check_is_changed: {e}")
        return False

def change_username(session_id, device_id, iid, last_username, nusr, max_retries=5):
    attempt = 0
    while attempt < max_retries:
        attempt += 1
        try:
            data = f"aid=364225&unique_id={quote(nusr)}"
            parm = f"aid=364225&residence=&device_id={device_id}&version_name=1.1.0&os_version=17.4.1&iid={iid}&app_name=tiktok_snail&locale=en&ac=4G&sys_region=SA&version_code=1.1.0&channel=App%20Store&op_region=SA&os_api=18&device_brand=iPad&idfv=16045E07-1ED5-4350-9318-77A1469C0B89&device_platform=iPad&device_type=iPad13,4&carrier_region1=&tz_name=Asia/Riyadh&account_region=&tz_offset=10800"
            headers = {
                "Host": "api.tiktokv.com",
                "Connection": "keep-alive",
                "sdk-version": "2",
                "x-tt-token": "00000000000000000000000000000000",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": "com.zhiliaoapp.musically/202100 (Linux; U; Android 8; en_US; samsung; SM-G930T; samsung; sm; en_US; tt-ok/1.1.0.0)",
                "Cookie": f"sessionid={session_id}",
                "Accept-Encoding": "gzip, deflate",
            }
            url = f"https://api.tiktokv.com/aweme/v1/commit/user/?{parm}"
            X_Gon = X_Gorgon(parm, data, f'sessionid={session_id}')
            response = requests.post(url, data=data, headers={**headers, **X_Gon})
            result = response.json()

            print(f"Attempt {attempt}: Response: {result}")

            if check_is_changed(last_username, session_id, device_id, iid):
                return "[ ! ] Username has been changed!"
            
            if 'redirect' in result or 'error' in result:
                print(f"[ {Fore.RED}- {Fore.RESET}] {Fore.RED}Redirect or error encountered, retrying...{Fore.RESET}")
            if 'Slow' in result:
                print(f"Being rate limited\n\n[ {Fore.RED}- {Fore.RESET}] {Fore.RED}MAKE SURE YOUR ACCOUNT WAS MADE IN JAPAN, discord.gg/guccimane USE THE GUIDE IN #links\n{result}{Fore.RESET}")
            else:
                print(f"[ {Fore.RED}- {Fore.RESET}] {Fore.RED}Error has occurred. Details: {result}{Fore.RESET}")

        except Exception as e:
            print(f"Exception in change_username (Attempt {attempt}): {e}")

        import time
        time.sleep(1)

    return f"[ {Fore.RED}- {Fore.RESET}] {Fore.RED}Failed to change username after multiple attempts!{Fore.RESET}"

def main():
    while True:
        clear()

        font = """

                  ██████████            
                  ██      ██            
                  ██      ██            
                  ██      ██            
                  ██      ██            
      ██████████████      ██████████████                          ┏━━━━━━━━━━━━━━━━━━━━━━━┓
      ██                              ██                          ┃WELCOME TO GUCCI'S TOOL┃
      ██                              ██                          ┃                       ┃
      ██                              ██                          ┃    SECTION = FONT     ┃
      ██████████████      ██████████████                          ┃                       ┃
                  ██      ██                                      ┃ discord.gg/guccimane  ┃
                  ██      ██                                      ┗━━━━━━━━━━━━━━━━━━━━━━━┛
                  ██      ██            
                  ██      ██            
                  ██      ██            
                  ██      ██            
                  ██      ██            
                  ██      ██            
                  ██      ██            
                  ██      ██            
                  ██      ██            
                  ██      ██            
                  ██████████            

"""
        font.center(40)

        redirect = """                                                                       
                 ████                              ████                        
              ████████        ██      ██        ████████                          ┏━━━━━━━━━━━━━━━━━━━━━━━┓
            ████████████      ██████████      ████████████                        ┃WELCOME TO GUCCI'S TOOL┃
          ████████████████    ██████████    ████████████████                      ┃                       ┃
        ████████    ████████████  ██  ████████████    ████████                    ┃  SECTION = REDIRECT   ┃
        ██████        ██████████████████████████        ██████                    ┃                       ┃
      ████              ██████████████████████              ████                  ┃ discord.gg/guccimane  ┃
      ██                    ██████████████                    ██                  ┗━━━━━━━━━━━━━━━━━━━━━━━┛
                              ██████████                                      
                              ██████████                                      
                                ██  ██                                        

"""
        redirect.center(40)

        menu = """
                                                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                                      ┃            /:.   ,:\            ┃
                                                      ┃      .~=-./::: u  ::\,-~=.      ┃
                                                      ┃   ___|::  \    |    /  ::|___   ┃
                                                      ┃  \::  `.   \   |   /   .' :::/  ┃
                                                      ┃   \:    `.  \  |  /  .'    :/   ┃
                                                      ┃ .-: `-._  `.;;;;;;.'   _.-' :-. ┃
                                                      ┃ \::     `-;;;;;;;;;;;-'     ::/ ┃
                                                      ┃  >~------~;;;;;;;;;;;~------~<  ┃
                                                      ┃ /::    _.-;;;;;;;;;;;-._    ::\ ┃
                                                      ┃ `-:_.-'   .`;;;;;;;'.   `-._:-' ┃
                                                      ┃    /    .'  /  |  \  `.   :\    ┃
                                                      ┃   /::_.'   /   |   \   `._::\   ┃
                                                      ┃       |:: /    |    \  ::|      ┃
                                                      ┃       `=-'\:::.n.:::/`-=-'      ┃
                                                      ┃            \:'   `:/            ┃
                                                      ┃                                 ┃
                                                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        
                                              ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                              ┃                                                    ┃
                                              ┃    {____   {__     {__    {__       {__   {__      ┃
                                              ┃  {_    {__ {__     {__ {__   {__ {__   {__{__      ┃
                                              ┃ {__        {__     {__{__       {__       {__      ┃
                                              ┃ {__        {__     {__{__       {__       {__      ┃
                                              ┃  {__    {_ {__     {__ {__   {__ {__   {__{__      ┃
                                              ┃   {_____     {_____      {____     {____  {__      ┃
                                              ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                                              ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ 
                                              ┃               [R] Redirect                         ┃
                                              ┃               [F] Regular Font                     ┃
                                              ┃               [T] Tutorials                        ┃
                                              ┃               [C] Credits                          ┃   
                                              ┃               [Q] FAQ                              ┃
                                              ┃                                                    ┃      
                                              ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

                                              →→→ """
        menu.center(40)

        session = """
                                                ████                                      
                                              ██▓▓▓▓██                                    
                                            ██▓▓▓▓██                                      
                                            ██▓▓██                                        
                                  ████████  ██▓▓██  ████████                              
                              ████░░░░░░░░████▓▓████░░░░░░░░████                          
                          ████░░░░░░░░░░██░░░░██░░░░██░░░░░░░░░░████                                
                        ██░░░░██░░░░░░██░░░░░░░░░░░░░░██░░░░░░██░░░░██                             
                      ██░░░░██░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░██░░░░██                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓      
                      ██░░██░░░░░░░░██░░░░░░░░██░░░░░░░░██░░░░░░░░██░░██                      ┃Welcome to Gucci Tool, Thank you for using this tool.┃      
                    ██░░██░░░░░░░░██████░░░░░░██░░░░░░██████░░░░░░░░██░░██                    ┃                                                     ┃      
                    ██░░██░░░░░░██████████░░░░░░░░░░██████████░░░░░░██░░██                    ┃                  Made by: Gucci                     ┃      
                    ██░░██░░░░░░██████████░░░░░░░░░░██████████░░░░░░██░░██                    ┃           Server: discord.gg/guccimane              ┃      
                    ██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██                    ┃            Paste your Session ID Below.             ┃      
                    ██░░██░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░██░░██                    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛      
                    ██░░██░░░░░░░░░░░░░░░░██████████░░░░░░░░░░░░░░░░██░░██                
                    ██░░██░░░░░░░░░░░░░░░░██████████░░░░░░░░░░░░░░░░██░░██                
                    ██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██                
                      ██░░██░░░░░░░░░░██████████████████░░░░░░░░░░██░░██                  
                      ██░░░░██░░░░░░░░░░░░██████████░░░░░░░░░░░░██░░░░██                  
                        ██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██                    
                          ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████                      
                              ████░░░░░░░░░░░░██░░░░░░░░░░░░████                          
                                  ████████████  ████████████                              


                                                                                      →→→ """
        session.center(40)

        tutorial = """


\n\n\n
       dBBBBBBBBBBBBBBBBBBBBBBBBb
      BP YBBBBBBBBBBBBBBBBBBBBBBBb
     dB   YBb                 YBBBb                                   
     dB    YBBBBBBBBBBBBBBBBBBBBBBBb                                 
      Yb    YBBBBBBBBBBBBBBBBBBBBBBBb                                 
       Yb    YBBBBBBBBBBBBBBBBBBBBBBBb                                
        Yb    YBBBBBBBBBBBBBBBBBBBBBBBb                               
	 Yb    YBBBBBBBBBBBBBBBBBBBBBBBb                                  
          Yb    YBBBBBBBBBBBBBBBBBBBBBBBb                             
	   Yb   dBBBBBBBBBBBBBBBBBBBBBBBBb
            Yb dP=======================/
             YbB=======================(
	      Ybb=======================|
	       Y888888888888888888DSI8888b\n\n\n
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃Step 1: Download OVPNSpider on Mobile                                                            ┃
┃Step 2: Download Python Editor on Mobile                                                         ┃
┃Step 3: Add "EditThisCookie" to your browser as an Extension                                     ┃
┃Step 4: Go back on Mobile, Make sure TikTok is closed and turn on Japan or Korea on OVPNSpider.  ┃
┃Step 5: Open TikTok with the vpn on and Sign Up:                                                 ┃
┃Step 6: Once you've made the account, go on your computer and log into the account you just made.┃
┃Step 7: Once you've logged in, go to EditThisCookie extension, and look for "session_id".        ┃
┃Step 8: Copy the session id and open up the Gucci Tool and choose what you want.                 ┃
┃                    THIS IS THE 50/50 METHOD, ADDING MOBILE METHOD LATER.                        ┃
┃                                  - Love from Gucci                                              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

"""
        tutorial.center(40)

        credits = """

                                                                       ┏━━━━━━━━━━━━━━━━━━━━┓
                                                                       ┃          _.-/)     ┃
                                                                       ┃         // / / )   ┃
                                                                       ┃      .=// / / / )  ┃
                                                                       ┃     /// / / / /    ┃
                                                                       ┃    // /      /     ┃
                                                                       ┃   ||         /     ┃
                                                                       ┃    ||       /      ┃
                                                                       ┃     ))    .'       ┃
                                                                       ┃    //    /         ┃
                                                                       ┃         /          ┃
                                                                       ┗━━━━━━━━━━━━━━━━━━━━┛\n\n\n
                                     ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                     ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
                                     ┃                                  Thank these people:                                            ┃
                                     ┃                                                                                                 ┃
                                     ┃ Harbi - Made the first tool, idea, & api.                                                       ┃
                                     ┃ "s"/pssionate - Found out the Redirect Method.                                                  ┃
                                     ┃ Fire - Helped me out with the new api & debug system.                                           ┃
                                     ┃ Matthew - gave me the correct recognition in conetic's server.                                  ┃
                                     ┃ Carbonia - Help and made it a bit more efficient.                                               ┃
                                     ┃                                                                                                 ┃
                                     ┃ I personally Thank the rest of you guys for supporting this tool and believing in me, Thank you.┃
                                     ┃                                 - From, Gucci.                                                  ┃
                                     ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

"""
        credits.center(40)

        faq = """
                  ???????                    .----------------.  .----------------.  .----------------. 
             ??:::::::::::?                  | .--------------. || .--------------. || .--------------. |
            ?:::::????:::::?                 | |  _________   | || |      __      | || |    ___       | |
            ?::::?    ?::::?                 | | |_   ___  |  | || |     /  \     | || |  .'   '.     | |
            ?::::?     ?::::?                | |   | |_  \_|  | || |    / /\ \    | || | /  .-.  \    | |
            ??????     ?::::?                | |   |  _|      | || |   / ____ \   | || | | |   | |    | |
                      ?::::?                 | |  _| |_       | || | _/ /    \ \_ | || | \  -'  \_    | |
                     ?::::?                  | | |_____|      | || ||____|  |____|| || |  .___.\__|   | |
                    ?::::?                   | |              | || |              | || |              | |
                   ?::::?                    | '--------------' || '--------------' || '--------------' |
                  ?::::?                     '----------------'  '----------------'  '----------------' 
                  ?::::?                         
                  ??::??     
                   ????      
                  
                    ???       
                   ??:??      
                    ???    

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃What VPN should i use ?                                                                          ┃
┃                                                                                                 ┃
┃ VPNS:                                                                                           ┃
┃-ovpnspider                                                                                      ┃
┃-mysterium vpn                                                                                   ┃ 
┃-tunnelbear                                                                                      ┃
┃-windscribe                                                                                      ┃
┃Working on both IOS and Android                                                                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃You're editing too fast, slow down error                                                         ┃
┃                                                                                                 ┃
┃Make a new account ON TIKTOK APP NOT THE BROWSER, THE APP WITH THE JAPAN VPN.                    ┃
┃                                                                                                 ┃
┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
┃Why this happens:                                                                                ┃ 
┃You either created the account on browser, made the account on pc, or you’re genuinely           ┃
┃just ratelimited so just wait.                                                                   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

"""
        faq.center(40)

        session_id = Write.Input(f"""\n\n\n\n\n\n{session}""",  ii, interval=0)

        clear()

        device_id = str(randint(777777788, 999999999999))
        iid = str(randint(777777788, 999999999999))

        sel = input(Colorate.Vertical(v, f"""\n\n\n\n\n\n{menu}""")).strip().lower()

        user = get_profile(session_id, device_id, iid)

        if user != "None":
            print(Colorate.Vertical(v, f"Guccimane @cxcvc"))
        else:
            print(Colorate.Vertical(er, f"\n[ - ] Incorrect session ID or something else is wrong, discord.gg/guccimane for help."))
            continue

        clear()
        if sel == "r":
            Write.Print(f"""\n\n\n\n\n\n{redirect}""",  rr, interval=0.001)
            sleep(0.2)  
            print(Colorate.Vertical(rr, f"[ ! ] Your Username: {user}".strip().lower()))
            nusr = input(Colorate.Vertical(rr, f"\n[ ! ] Enter your new Username: ".strip().lower()))
            nusr = nusr.ljust(78) + random.choice(string.ascii_lowercase)
            rrr = change_username(session_id, device_id, iid, user, nusr)
            clear()
            Write.Print(rrr, er, interval=0)
            print(Colorate.Vertical(wr, f"\n[ + ] IT WORKED! YOUR USER IS NOW\n\n GOING BACK TO SESSION ID PAGE IN 3 SECONDS: {nusr}"))
            sleep(3)  
        elif sel == "f":
            Write.Print(f"""\n\n\n\n\n\n{font}""",  ff, interval=0.001)
            sleep(0.2)  
            print(Colorate.Vertical(ff, f"\n[ ! ] Your Username: {user}".strip().lower()))
            nusr = input(Colorate.Vertical(ff, f"\n[ ! ] Enter your new Username: ".strip().lower()))
            rrr = change_username(session_id, device_id, iid, user, nusr)
            clear()
            Write.Print(rrr, er, interval=0)
            print(Colorate.Vertical(wr, f"\n[ + ] IT WORKED! YOUR USER IS NOW\n\n GOING BACK TO SESSION ID PAGE IN 3 SECONDS: {nusr}"))
            sleep(3)  
        elif sel == "t":
            Write.Print(f"""{tutorial}""", tt, interval=0.001)
            sleep(0.2) 
            gucci = input(f"\n{Fore.LIGHTRED_EX}Type 'gucci' to go back when you're done: ".lower())
            if gucci == "gucci":
                continue
        elif sel == "c":
            Write.Print(f"""{credits}""", cc, interval=0.001)
            sleep(0.2) 
            gucci = input(f"\n{Fore.LIGHTGREEN_EX}Type 'gucci' to close when you're done: ".lower())
            if gucci == "gucci":
                continue
            print("\n")
        elif sel == "q":
            Write.Print(f"""{faq}""", gg, interval=0.001)
            sleep(0.2) 
            gucci = input(f"\n{Fore.LIGHTYELLOW_EX}Type 'gucci' to close when you're done: ".lower())
            if gucci == "gucci":
                continue
            print("\n")
        else:
            print(Colorate.Vertical(er, f"\n[ - ] This isn't Redirect, Regular Font, Tutorials, Credits, or FAQ. Go back and choose the correct one. Try typing the letters lowercased."))
            continue  

if __name__ == "__main__":
    main()
