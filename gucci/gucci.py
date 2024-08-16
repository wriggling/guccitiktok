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
from colorama import Fore, init  # Import colorama for coloring text
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

def clear(): return os.system('cls') if os.name == 'nt' else os.system('clear')
os.system("mode con cols=200 lines=40")
system(f"title " + "GUCCI TOOL [@cxcvc on DC]")

# Helper functions (no changes needed here)
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

# XG class (no changes needed here)
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

# X-Gorgon function (no changes needed here)
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

# Function to get the stub (no changes needed here)
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

# Function to retrieve TikTok profile (no changes needed here)
def get_profile(session_id, device_id, iid):
    """Retrieve the current TikTok username for a given session, device, and iid."""
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
        print(f"Profile response: {profile_data}")  # Debug print
        return profile_data.get("user", {}).get("unique_id", "None")
    except Exception as e:
        print(f"Exception in get_profile: {e}")  # Debug print
        return "None"

# Function to check if username has been changed (no changes needed here)
def check_is_changed(last_username, session_id, device_id, iid):
    """Check if the username has been successfully changed."""
    try:
        current_username = get_profile(session_id, device_id, iid)
        print(f"Current username: {current_username}")  # Debug print
        return not (current_username == last_username)
    except Exception as e:
        print(f"Exception in check_is_changed: {e}")  # Debug print
        return False

# Function to change TikTok username (updated with detailed error handling and retry logic)
def change_username(session_id, device_id, iid, last_username, nusr, max_retries=5):
    """Attempt to change a TikTok username with retry logic."""
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

            # Log attempt details
            print(f"Attempt {attempt}: Response: {result}")

            if check_is_changed(last_username, session_id, device_id, iid):
                return "[ ! ] Username has been changed!"
            
            if 'redirect' in result or 'error' in result:  # Assuming API might include such fields
                print("[ :( ] Redirect or error encountered, retrying...")
            if 'Slow' in result:
                print(f"Being rate limited\n\n{Fore.RED}[ :( ] MAKE SURE YOUR ACCOUNT WAS MADE IN JAPAN, discord.gg/guccimane USE THE GUIDE IN #links\n{Fore.WHITE}{result}")
            else:
                print(f"[ :( ] Error has occurred. Details: {result}")

        except Exception as e:
            print(f"Exception in change_username (Attempt {attempt}): {e}")  # Debug print

        # Optional sleep before retrying (e.g., 1 second)
        import time
        time.sleep(1)

    return f"{Fore.RED}[ :( ] Failed to change username after multiple attempts!"

# Updated main function to handle user interaction and username change
def main():
      """Main function to handle user interaction and username change."""
      clear()

      # All of the Section's ASCII
      font = """

            ██████████            
            ██      ██            
            ██      ██            
            ██      ██            
            ██      ██            
██████████████      ██████████████                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓         
██                              ██                    ┃ _ _ _     _                      _          _____         _      _____     _   _         _ ┃
██                              ██                    ┃| | | |___| |___ ___ _____ ___   | |_ ___   |   __|___ ___| |_   |     |___| |_| |_ ___ _| |┃
██                              ██                    ┃| | | | -_| |  _| . |     | -_|  |  _| . |  |   __| . |   |  _|  | | | | -_|  _|   | . | . |┃
██████████████      ██████████████                    ┃|_____|___|_|___|___|_|_|_|___|  |_| |___|  |__|  |___|_|_|_|    |_|_|_|___|_| |_|_|___|___|┃
            ██      ██                                ┃                                                                                            ┃
            ██      ██                                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
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
            ████████        ██      ██        ████████                        ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
          ████████████      ██████████      ████████████                      ║ __      __   _                    _         ___        _ _            _     __  __     _   _            _   ║
        ████████████████    ██████████    ████████████████                    ║ \ \    / /__| |__ ___ _ __  ___  | |_ ___  | _ \___ __| (_)_ _ ___ __| |_  |  \/  |___| |_| |_  ___  __| |  ║
      ████████    ████████████  ██  ████████████    ████████                  ║  \ \/\/ / -_) / _/ _ \ '  \/ -_) |  _/ _ \ |   / -_) _` | | '_/ -_) _|  _| | |\/| / -_)  _| ' \/ _ \/ _` |_ ║
      ██████        ██████████████████████████        ██████                  ║   \_/\_/\___|_\__\___/_|_|_\___|  \__\___/ |_|_\___\__,_|_|_| \___\__|\__| |_|  |_\___|\__|_||_\___/\__,_(_)║
    ████              ██████████████████████              ████                ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    ██                    ██████████████                    ██              
                            ██████████                                      
                            ██████████                                      
                              ██  ██                                        
"""
      redirect.center(40)

      menu = """
  ░░░░░░                                                                                              ▒▒  
      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░    ░░                                                      ░░    ░░▒▒▒▒▒▒▓▓▒▒▒▒    
  ▓▓▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░                                          ▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓
      ░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒                                ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░    
    ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒░░                          ░░▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓                                 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ░░▒▒▓▓▓▓▓▓▓▓██▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒                      ▒▒▒▒▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░                                 ┃                                                    ┃
    ░░▓▓▓▓▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓██▒▒▓▓██▒▒▒▒▓▓▒▒▒▒                  ░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▒▒▓▓▓▓                                   ┃    {____   {__     {__    {__       {__   {__      ┃
          ▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒                  ▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓                                       ┃  {_    {__ {__     {__ {__   {__ {__   {__{__      ┃
          ▒▒▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▒▒▒▒▒▒              ▒▒▒▒▓▓▒▒▓▓████▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▒▒                                       ┃ {__        {__     {__{__       {__       {__      ┃
              ▓▓▒▒▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██▒▒▓▓▓▓▒▒░░            ▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▒▒▒▒                                         ┃ {__        {__     {__{__       {__       {__      ┃
                  ▓▓▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓████▓▓▒▒▒▒▒▒          ▒▒▒▒▒▒▓▓██▓▓▓▓▓▓██▓▓▓▓██▓▓██▒▒▓▓                                             ┃  {__    {_ {__     {__ {__   {__ {__   {__{__      ┃
                      ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▒▒▒▒▒▒░░        ▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒                                                 ┃   {_____     {_____      {____     {____  {__      ┃
                              ▓▓▓▓▓▓██▓▓▓▓▒▒██▒▒▒▒▓▓░░    ▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                         ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                                ▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▒▒▓▓▓▓░░▒▒▓▓▒▒▓▓████▓▓▓▓▓▓▓▓▒▒                                                           ┃                                                    ┃ 
                                  ▓▓▓▓▓▓▓▓▓▓██████▓▓░░    ▓▓▒▒██▓▓██▓▓▓▓▓▓▒▒                                                             ┃               [R] Redirect                         ┃
                                  ░░▓▓▓▓▓▓▓▓██████▒▒        ▓▓██▓▓▓▓▓▓▓▓▓▓                                                               ┃               [F] Regular Font                     ┃
                                    ▓▓▓▓▓▓▓▓██████          ▓▓████▓▓████                                                                 ┃               [T] Tutorials                        ┃
                                      ██▓▓▓▓██████          ▒▒████▓▓▓▓▓▓                                                                 ┃               [C] Credits                          ┃         
                                      ▒▒▓▓▓▓██▓▓░░            ▓▓██▓▓▓▓                                                                   ┃                                                    ┃      
                                        ▒▒▓▓░░                  ░░▓▓░░                                                                   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                                          ▓▓                      ██                                      

                                                                                                                                                         →→→ """
      menu.center(40)

      session = """
                                              ████                                      
                                            ██▓▓▓▓██                                    
                                          ██▓▓▓▓██                                      
                                          ██▓▓██                                        
                                ████████  ██▓▓██  ████████                              
                            ████░░░░░░░░████▓▓████░░░░░░░░████                          
                        ████░░░░░░░░░░██░░░░██░░░░██░░░░░░░░░░████                                █████████████████████████████████████████████████████████████████████████████████████████████
                      ██░░░░██░░░░░░██░░░░░░░░░░░░░░██░░░░░░██░░░░██                              █ _____ _____ _____ _____ _____ _____ _   _   ___________  ______ _____ _     _____  _    _ █
                    ██░░░░██░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░██░░░░██                            █/  ___|  ___/  ___/  ___|_   _|  _  | \ | | |_   _|  _  \ | ___ \  ___| |   |  _  || |  | |█
                    ██░░██░░░░░░░░██░░░░░░░░██░░░░░░░░██░░░░░░░░██░░██                            █\ `--.| |__ \ `--.\ `--.  | | | | | |  \| |   | | | | | | | |_/ / |__ | |   | | | || |  | |█
                  ██░░██░░░░░░░░██████░░░░░░██░░░░░░██████░░░░░░░░██░░██                          █ `--. \  __| `--. \`--. \ | | | | | | . ` |   | | | | | | | ___ \  __|| |   | | | || |/\| |█
                  ██░░██░░░░░░██████████░░░░░░░░░░██████████░░░░░░██░░██                          █/\__/ / |___/\__/ /\__/ /_| |_\ \_/ / |\  |  _| |_| |/ /  | |_/ / |___| |___\ \_/ /\  /\  /█
                  ██░░██░░░░░░██████████░░░░░░░░░░██████████░░░░░░██░░██                          █\____/\____/\____/\____/ \___/ \___/\_| \_/  \___/|___/   \____/\____/\_____/\___/  \/  \/ █
                  ██░░██░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░██░░██                          █                                   discord.gg/guccimane                                    █
                  ██░░██░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░██░░██                          █████████████████████████████████████████████████████████████████████████████████████████████
                  ██░░██░░░░░░░░░░░░░░░░██████████░░░░░░░░░░░░░░░░██░░██                
                  ██░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░██                
                  ██░░░░░░░░░░░░░░████░░░░░░░░░░░░░░████░░░░░░░░░░░░░░██                
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
     dB   YBb                 YBBBb                                   ██████████████████████████████████████████████████████████████████████████████████
     dB    YBBBBBBBBBBBBBBBBBBBBBBBb                                  █ ______   __  __     ______   ______     ______     __     ______     __        █
      Yb    YBBBBBBBBBBBBBBBBBBBBBBBb                                 █/\__  _\ /\ \/\ \   /\__  _\ /\  __ \   /\  == \   /\ \   /\  __ \   /\ \       █
       Yb    YBBBBBBBBBBBBBBBBBBBBBBBb                                █\/_/\ \/ \ \ \_\ \  \/_/\ \/ \ \ \/\ \  \ \  __<   \ \ \  \ \  __ \  \ \ \____  █
        Yb    YBBBBBBBBBBBBBBBBBBBBBBBb                               █   \ \_\  \ \_____\    \ \_\  \ \_____\  \ \_\ \_\  \ \_\  \ \_\ \_\  \ \_____\ █
	 Yb    YBBBBBBBBBBBBBBBBBBBBBBBb                              █    \/_/   \/_____/     \/_/   \/_____/   \/_/ /_/   \/_/   \/_/\/_/   \/_____/ █
          Yb    YBBBBBBBBBBBBBBBBBBBBBBBb                             ██████████████████████████████████████████████████████████████████████████████████
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
┃                                       - Love from Gucci                                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

"""
      tutorial.center(40)

      credits = """

                                                                     ┏━━━━━━━━━━━━━━━━━━━━┓
                                                                     ┃          _.-/`)    ┃
                                                                     ┃         // / / )   ┃
                                                                     ┃      .=// / / / )  ┃
                                                                     ┃     //`/ / / / /   ┃
                                                                     ┃    // /     ` /    ┃
                                                                     ┃   ||         /     ┃
                                                                     ┃    ||       /      ┃
                                                                     ┃     ))    .'       ┃
                                                                     ┃    //    /         ┃
                                                                     ┃         /          ┃
                                                                     ┗━━━━━━━━━━━━━━━━━━━━┛\n\n\n
                                     ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                     ┃            _____ _                 _                           ___  _ _ _                       ┃
                                     ┃           |_   _| |               | |                         / _ \| | | |                      ┃
                                     ┃             | | | |__   __ _ _ __ | | __  _   _  ___  _   _  / /_\ \ | | |                      ┃
                                     ┃             | | | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | | |  _  | | | |                      ┃
                                     ┃             | | | | | | (_| | | | |   <  | |_| | (_) | |_| | | | | | | |_|                      ┃
                                     ┃             \_/ |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_| \_| |_/_|_(_)                      ┃
                                     ┃                                            __/ |                                                ┃
                                     ┃                                           |___/                                                 ┃
                                     ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
                                     ┃                              Thank these people:                                                ┃
                                     ┃                                                                                                 ┃
                                     ┃                      Harbi - Made the first tool, idea, & api.                                  ┃
                                     ┃                      "s"/pssionate - Found out the Redirect Method.                             ┃
                                     ┃                      Fire - Helped me out with the new api & debug system.                      ┃
                                     ┃                      Matthew - gave me the correct recognition in conetic's server.             ┃
                                     ┃                                                                                                 ┃
                                     ┃ I personally Thank the rest of you guys for supporting this tool and believing in me, Thank you.┃
                                     ┃                                 - From, Gucci.                                                  ┃
                                     ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
\n
"""
      credits.center(40)

      # startup of Gucci Tool
      session_id = Write.Input(f"""\n\n\n\n\n\n{session}""",  ii, interval=0.0)

      device_id = str(randint(777777788, 999999999999))
      iid = str(randint(777777788, 999999999999))
    
      
      # Ask the user for "Redirect" or "User"
      clear()
      sel = input(Colorate.Vertical(v, f"""\n\n\n\n\n\n{menu}""")).strip().lower()

      user = get_profile(session_id, device_id, iid)

      if user != "None":
        print(Colorate.Vertical(v, f"Guccimane @cxcvc"))
      else:
        print(Colorate.Vertical(er, f"\nIncorrect session ID or something else is wrong, discord.gg/guccimane for help."))
        return
      clear()
      if sel == "r":
        Write.Print(f"""\n\n\n\n\n\n{redirect}""",  rr, interval=0.0)
        print(Colorate.Vertical(rr, f"Your Username: {user}".strip().lower()))
        nusr = input(Colorate.Vertical(rr, f"\n Enter your new Username: ".strip().lower()))
        nusr = nusr.ljust(78) + random.choice(string.ascii_lowercase)
      elif sel == "f":
        Write.Print(f"""\n\n\n\n\n\n{font}""",  ff, interval=0.0)
        print(Colorate.Vertical(ff, f"\nYour Username: {user}".strip().lower()))
        nusr = input(Colorate.Vertical(ff, f"\n Enter your new Username: ".strip().lower()))
      elif sel == "t":
        Write.Print(f"""{tutorial}""", tt, interval=0.001)
        input(f"{Fore.LIGHTRED_EX}Type anything to close when you're done: ".lower())
      elif sel == "c":
        Write.Print(f"""{credits}""", cc, interval=0.001)
        input(f"{Fore.LIGHTGREEN_EX}Type anything to close when you're done: ".lower())
        print("\n")
      else:
        print(Colorate.Vertical(er, f"\nThis isn't Redirect, or Reg Font. Go back and choose the correct one. Try typing the letters lowercased."))
        return

      rrr = change_username(session_id, device_id, iid, user, nusr)
      clear()
      Write.Print(rrr, er, interval=0)
      print(Colorate.Vertical(wr, f"\nIT WORKED! YOUR USER IS NOW: {nusr}"))

# Ensuring the main function runs
if __name__ == "__main__":
    main()
