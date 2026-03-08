import os, sys, time, base64, json, asyncio, socket, random
from arabic_reshaper import reshape
from bidi.algorithm import get_display

# --- إعدادات الملك SUKUNA_ii (إمبراطورية علي طالب) ---
TOKEN = "8382035555:AAEyKqioQySc5HNLSJ3NwrDh89p3RpDPY"
ADMIN_ID = "6709215417"
GITHUB_USER = "alitalp713551980sukuna-cloud"

# الألوان الملكية (هيبة سكونا)
G, R, Y, C, W, B, P = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m', '\033[1;34m', '\033[1;35m'

class SukunaEmpireV20:
    def __init__(self):
        self.lang = "AR"
        self.u = {"n": "Guest", "id": str(random.randint(100000, 999999)), "lv": 1, "p": 0, "d": 5}
        self.tools = {str(i): f"Tool_S{i}" for i in range(1, 101)}

    def ar(self, text):
        # معالجة النصوص العربية لتظهر بشكل صحيح في ترمكس
        reshaped = reshape(text)
        return get_display(reshaped)

    def banner(self):
        os.system("clear")
        print(f"{R}   ██████  ██    ██ ██   ██ ██    ██ ███    ██  █████  ")
        print(f"  ██       ██    ██ ██  ██  ██    ██ ████   ██ ██   ██ ")
        print(f"   █████   ██    ██ █████   ██    ██ ██ ██  ██ ███████ ")
        print(f"  {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{Y} {self.ar('المستخدم')}: {G}{self.u['n']} {W}|{Y} ID: {G}{self.u['id']} {W}|{Y} {self.ar('المستوى')}: {G}{self.u['lv']}")
        print(f"{C} {self.ar('النقاط')}: {G}{self.u['p']} {W}|{C} {self.ar('يومي')}: {G}{self.u['d']}/5 {W}|{C} {self.ar('الرتبة')}: {P}{self.ar('ملك اللعنات')}")
        print(f"{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    def show_info(self, tid):
        self.banner()
        print(f"{Y} --- [ {self.ar('شرح الأداة')} {tid} ] ---")
        print(f"{W} 1. {self.ar('الاستخدام: ادخل الرقم وحدد عدد الهجمات المطلوبة.')}")
        print(f"{W} 2. {self.ar('الغرض: تعطيل الخدمة وسحب الجلسات النشطة.')}")
        print(f"{W} 3. {self.ar('الخدعة: أوهم الضحية أنها أداة لفك حظر واتساب.')}")
        input(f"\n{G} {self.ar('اضغط انتر للعودة...')}")

    def attack_ui(self, name):
        self.banner()
        print(f"{C} --- [ {self.ar('بدء الهجوم')}: {name} ] ---")
        target = input(f"{Y} [#] {self.ar('ادخل رقم الضحية')}: {W}")
        if target == "+967713551980":
            print(f"{R} {self.ar('هههههه.. هذا رقم المطور! لا تقترب من لعنة المالك.')}")
            time.sleep(3); return
        try:
            count = int(input(f"{Y} [#] {self.ar('كم تريد إرسال طلبات (العدد)')}: {W}"))
        except: count = 10
        
        print(f"{G}\n {self.ar('جاري تشفير الهجوم وإرسال')} {count} {self.ar('طلب...')}")
        for i in range(count):
            time.sleep(0.1)
            print(f"{C} [→] {self.ar('تم إرسال الطلب')} ({i+1}) {self.ar('بنجاح')}...", end="\r")
        print(f"\n{G} ✅ {self.ar('تم اكتمال الهجوم بنجاح!')}")
        input("...")

    async def welcome_screen(self):
        os.system("clear")
        print(f"{P}" + self.ar("جاري الاتصال بخوادم SUKUNA-CLOUD..."))
        time.sleep(2)
        print(f"{G}" + self.ar("تم التحقق! أهلاً بك في جيش ملك اللعنات."))
        self.u['n'] = input(f"{Y} " + self.ar("ادخل اسمك القتالي: ") + f"{W}")
        print(f"{R}" + self.ar("تنبيه: يجب عليك الولاء المطلق للمطور SUKUNA_ii لضمان بقاء حسابك."))
        time.sleep(2)

    async def main(self):
        await self.welcome_screen()
        while True:
            self.banner()
            print(f" {B}[1] {self.ar('الأدوات (100)')}  [2] {self.ar('المتجر النخبوي')}")
            print(f" {B}[3] {self.ar('تجميع النقاط')}   [4] {self.ar('معلومات المطور')}")
            print(f" {B}[5] {self.ar('تغيير اللغة')}     [6] {self.ar('المتصدرين عالمياً')}")
            print(f" {B}[7] {self.ar('البحث')}           [8] {self.ar('شحن الرصيد')}")
            print(f" {B}[9] {self.ar('خدمات أخرى')}     [10] {self.ar('الدردشة الملكية')}")
            
            cmd = input(f"\n{R} SUKUNA > {W}").strip()
            
            if cmd == "1":
                self.banner()
                for i in range(1, 101):
                    lock = "🔓" if i <= self.u['lv'] else "🔒"
                    print(f" [{i}] {self.tools[str(i)]} {lock}", end="\t" if i%3!=0 else "\n")
                choice = input(f"\n\n{Y} {self.ar('اختر رقم الأداة')}: {W}")
                if choice in self.tools: self.attack_ui(self.tools[choice])
            
            elif cmd.upper().startswith("SUKUNA") and len(cmd) > 6:
                tid = cmd.upper().replace("SUKUNA", "")
                self.show_info(tid)
            
            elif cmd == "4":
                self.banner()
                print(f"{C} {self.ar('المطور')}: {G}علي طالب (SUKUNA)")
                print(f"{C} {self.ar('حساب السحابة')}: {W}{GITHUB_USER}")
                print(f"{C} {self.ar('واتساب')}: {W}+967713551980")
                input(f"\n {self.ar('اضغط انتر للعودة...')}")
            
            elif cmd.upper() == "SUKUNA": continue

if __name__ == "__main__":
    app = SukunaEmpireV20()
    asyncio.run(app.main())
