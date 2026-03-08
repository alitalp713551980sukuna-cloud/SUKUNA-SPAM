import os, sys, time, base64, json, asyncio, socket, random, webbrowser

# --- إعدادات السيادة (SUKUNA_ii) ---
TOKEN = "8382035555:AAEyKqioQySc5HNLSJ3NwrDh89p3RpDPY"
ADMIN_ID = "6709215417"

# ألوان الهيبة
G, R, Y, C, W, B, P = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m', '\033[1;34m', '\033[1;35m'

class SukunaEmpire:
    def __init__(self):
        self.lang = "EN"
        self.user_data = {
            "name": "Guest", "id": str(random.randint(100000, 999999)),
            "level": 1, "points": 0, "daily_use": 5, "rank": "Servant"
        }
        self.tools_count = 100

    def trans(self, en, ar): return ar if self.lang == "AR" else en

    def check_perms(self):
        while not os.path.exists("/sdcard"):
            os.system("clear")
            print(f"{R} [!] Permissions Required | يجب منح الصلاحيات للعمل")
            os.system("termux-setup-storage")
            time.sleep(5)

    def banner(self):
        os.system("clear")
        print(f"{R}   ██████  ██    ██ ██   ██ ██    ██ ███    ██  █████  ")
        print(f"  ██       ██    ██ ██  ██  ██    ██ ████   ██ ██   ██ ")
        print(f"   █████   ██    ██ █████   ██    ██ ██ ██  ██ ███████ ")
        print(f"       ██  ██    ██ ██  ██  ██    ██ ██  ██ ██ ██   ██ ")
        print(f"  ██████    ██████  ██   ██  ██████  ██   ████ ██   ██ ")
        print(f"{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{Y} User: {G}{self.user_data['name']} {W}|{Y} ID: {G}{self.user_data['id']} {W}|{Y} Lvl: {G}{self.user_data['level']}")
        print(f"{C} Rank: {P}{self.user_data['rank']} {W}|{C} Points: {G}{self.user_data['points']} {W}|{C} Daily: {G}{self.user_data['daily_use']}/5")
        print(f"{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    def tool_info(self, tid):
        self.banner()
        print(f"{Y} --- [ {self.trans('Tool Description', 'شرح الأداة')} ] ---")
        # مثال لشرح الأداة 100 (التحكم الكامل)
        if tid == "100":
            print(f"{G} 1. {self.trans('How to use: Start the listener and send the link.', 'كيفية الاستخدام: ابدأ المستمع وأرسل الرابط.')}")
            print(f"{G} 2. {self.trans('Purpose: Full access to camera and files.', 'الغرض: الوصول الكامل للكاميرا والملفات.')}")
            print(f"{G} 3. {self.trans('Trick: Tell them it is a system security update.', 'الخدعة: أخبرهم أنه تحديث أمني للنظام.')}")
        else:
            print(f"{G} [!] {self.trans('Detailed manual for this tool is being downloaded...', 'يتم الآن تحميل الدليل التفصيلي لهذه الأداة...')}")
        input(f"\n{W} {self.trans('Enter to go back', 'اضغط انتر للرجوع')}...")

    async def main_menu(self):
        while True:
            self.banner()
            print(f" {B}[1] {self.trans('Tools', 'الأدوات')}  [2] {self.trans('Store', 'المتجر')}  [3] {self.trans('Tasks', 'المهام')}")
            print(f" {B}[4] {self.trans('Dev', 'المطور')}    [5] {self.trans('Settings', 'الإعدادات')} [6] {self.trans('Top 10', 'المتصدرين')}")
            print(f" {B}[7] {self.trans('Search', 'بحث')}   [8] {self.trans('Top-up', 'الشحن')}   [9] {self.trans('Services', 'الخدمات')}")
            print(f" {B}[10] {self.trans('Chat', 'دردشة')}")
            
            cmd = input(f"\n{R} SUKUNA > {W}").strip()
            
            if cmd == "1":
                self.banner()
                for i in range(1, 101):
                    status = "🔓" if i <= self.user_data['level'] else "🔒"
                    print(f" [{i}] Tool_{i} {status}", end="\t" if i%3!=0 else "\n")
                input("\n Back...")
            elif "SUKUNA" in cmd.upper():
                tid = cmd.upper().replace("SUKUNA", "")
                if tid: self.tool_info(tid)
            elif cmd == "5":
                self.lang = "AR" if self.lang == "EN" else "EN"
            elif cmd == "8":
                print(f"{G} Contact @SUKUNA_i to buy points (YER/USD)")
                time.sleep(2)

if __name__ == "__main__":
    os.system("pkg install termux-api python-bidi arabic-reshaper -y")
    app = SukunaEmpire()
    app.check_perms()
    asyncio.run(app.main_menu())
