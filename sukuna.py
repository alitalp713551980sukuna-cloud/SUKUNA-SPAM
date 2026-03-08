import os, sys, time, base64, json, asyncio, socket, random
from arabic_reshaper import reshape
from bidi.algorithm import get_display

# --- إعدادات السيادة المطلقة (الملك علي طالب) ---
TOKEN = "8382035555:AAEyKqioQySc5HNLSJ3NwrDh89p3RpDPY"
ADMIN_ID = "6709215417"
GITHUB_USER = "alitalp713551980sukuna-cloud"

# الألوان الملكية
G, R, Y, C, W, B, P = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m', '\033[1;34m', '\033[1;35m'

class SukunaUltimateSystem:
    def __init__(self):
        self.lang = "AR"
        self.u = {"n": "Guest", "id": str(random.randint(100000, 999999)), "lv": 1, "p": 0, "d": 5}
        self.tools = {str(i): f"Tool_S{i}" for i in range(1, 101)}
        self.is_running = True

    def ar(self, text):
        return get_display(reshape(text))

    def banner(self):
        os.system("clear")
        print(f"{R}   ██████  ██    ██ ██   ██ ██    ██ ███    ██  █████  ")
        print(f"  ██       ██    ██ ██  ██  ██    ██ ████   ██ ██   ██ ")
        print(f"   █████   ██    ██ █████   ██    ██ ██ ██  ██ ███████ ")
        print(f"  {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{Y} {self.ar('المستخدم')}: {G}{self.u['n']} {W}|{Y} ID: {G}{self.u['id']} {W}|{Y} {self.ar('المستوى')}: {G}{self.u['lv']}")
        print(f"{C} {self.ar('النقاط')}: {G}{self.u['p']} {W}|{C} {self.ar('المحاولات')}: {G}{self.u['d']}/5 {W}|{C} {self.ar('الرتبة')}: {P}{self.ar('ملك اللعنات')}")
        print(f"{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    def attack_ui(self, name):
        self.banner()
        print(f"{C} --- [ {self.ar('بدء الهجوم')}: {name} ] ---")
        target = input(f"{Y} [#] {self.ar('ادخل الرقم المستهدف')}: {W}")
        if "+967713551980" in target:
            print(f"{R} {self.ar('خطأ صاعق! هذا رقم المطور علي طالب. تم تجميد حسابك مؤقتاً.')}"); time.sleep(3); return
        try:
            count = int(input(f"{Y} [#] {self.ar('كم تريد إرسال طلبات (العدد)')}: {W}"))
        except: count = 10
        print(f"{G}\n {self.ar('جاري تشفير الهجوم وإرسال')} {count} {self.ar('طلب...')}")
        for i in range(count):
            time.sleep(0.1)
            print(f"{C} [→] {self.ar('تم الإرسال بنجاح')} ({i+1})...", end="\r")
        print(f"\n{G} ✅ {self.ar('تم اكتمال الهجوم بنجاح!')}"); input("...")

    def show_leaderboard(self):
        self.banner()
        print(f"{Y}      {self.ar('🏅 لوحة المتصدرين (أعلى 10) 🏅')}")
        print(f"{W}  {self.ar('المركز')}   |   {self.ar('المستوى')}   |   {self.ar('النقاط')}   |   {self.ar('الاسم')}")
        print(f"{G}  1.  🥇   |   Lv.99  |  999k  |  SUKUNA_ii")
        print(f"{W}  2.  🥈   |   Lv.45  |  50k   |  Ali_War")
        print(f"{W}  3.  🥉   |   Lv.30  |  12k   |  Shadow_H")
        print(f"{W}  -------------------------------------------")
        input(f"\n{C} {self.ar('اضغط انتر للرجوع...')}")

    def show_store(self):
        self.banner()
        print(f"{P} --- [ {self.ar('متجر اللعنات النخبوي')} ] ---")
        print(f"{W} [1] {self.ar('رشق متابعين (غالي جداً)')}  - 100k {self.ar('نقطة')}")
        print(f"{W} [2] {self.ar('اختراق واتساب (مستحيل)')}    - 1M {self.ar('نقطة')}")
        print(f"{W} [3] {self.ar('تحديد موقع دولي')}         - 500k {self.ar('نقطة')}")
        print(f"{R} [!] {self.ar('للشراء تواصل مع المالك مباشرة.')}")
        input("...")

    async def main(self):
        os.system("clear")
        print(f"{G}" + self.ar("جاري تفعيل بروتوكولات SUKUNA-CLOUD..."))
        time.sleep(1)
        self.u['n'] = input(f"{Y} " + self.ar("ادخل اسم حسابك للبدء: ") + f"{W}")
        
        while self.is_running:
            self.banner()
            print(f" {B}[1] {self.ar('الأدوات (100)')}  [2] {self.ar('المتجر النخبوي')}")
            print(f" {B}[3] {self.ar('تجميع النقاط')}   [4] {self.ar('معلومات المطور')}")
            print(f" {B}[5] {self.ar('تغيير اللغة')}     [6] {self.ar('المتصدرين عالمياً')}")
            print(f" {B}[7] {self.ar('البحث (الأيدي)')}  [8] {self.ar('شحن الرصيد (VIP)')}")
            print(f" {B}[9] {self.ar('خدمات المطور')}    [10] {self.ar('الدردشة الملكية')}")
            
            cmd = input(f"\n{R} SUKUNA > {W}").strip()
            
            if cmd == "1":
                self.banner()
                for i in range(1, 101):
                    lock = "🔓" if i <= self.u['lv'] else "🔒"
                    print(f" [{i}] S{i} {lock}", end="\t" if i%3!=0 else "\n")
                c = input(f"\n\n{Y} {self.ar('اختر الرقم')}: {W}")
                if c in self.tools: self.attack_ui(self.tools[c])
            elif cmd == "2": self.show_store()
            elif cmd == "6": self.show_leaderboard()
            elif cmd == "10":
                print(f"{Y}\n [!] {self.ar('سيتم فتح الدردشة العالمية في الإصدار القادم...')}"); time.sleep(2)
            elif cmd.upper().startswith("SUKUNA") and len(cmd) > 6:
                tid = cmd.upper().replace("SUKUNA", "")
                self.banner()
                print(f"{Y} {self.ar('شرح الأداة')} {tid}:\n{W} 1. {self.ar('أدخل الرقم المستهدف.')}\n 2. {self.ar('حدد كمية الطلبات.')}\n 3. {self.ar('انتظر اكتمال الاختـ ـراق.')}")
                input("...")
            elif cmd.upper() == "EXIT": break

if __name__ == "__main__":
    app = SukunaUltimateSystem()
    asyncio.run(app.main())
