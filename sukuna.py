import os, sys, time, base64, json, asyncio, socket, random
from arabic_reshaper import reshape
from bidi.algorithm import get_display

# --- إعدادات الملك SUKUNA_ii (تشفير نووي) ---
TOKEN = "8382035555:AAEyKqioQySc5HNLSJ3NwrDh89p3RpDPY"
ID = "6709215417"

# الألوان الملكية
G, R, Y, C, W, B, P = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;36m', '\033[1;37m', '\033[1;34m', '\033[1;35m'

class SukunaEmpireV20:
    def __init__(self):
        self.lang = "EN"
        self.u = {"n": "Guest", "id": str(random.randint(100000, 999999)), "lv": 1, "p": 0, "d": 5}
        self.tools = {str(i): f"Tool_S{i}" for i in range(1, 101)}

    def ar(self, text):
        # إصلاح الخط العربي لترمكس
        if self.lang == "EN": return text
        reshaped = reshape(text)
        return get_display(reshaped)

    def banner(self):
        os.system("clear")
        print(f"{R}   ██████  ██    ██ ██   ██ ██    ██ ███    ██  █████  ")
        print(f"  ██       ██    ██ ██  ██  ██    ██ ████   ██ ██   ██ ")
        print(f"   █████   ██    ██ █████   ██    ██ ██ ██  ██ ███████ ")
        print(f"  {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{Y} User: {G}{self.u['n']} {W}|{Y} ID: {G}{self.u['id']} {W}|{Y} Level: {G}{self.u['lv']}")
        print(f"{C} Points: {G}{self.u['p']} {W}|{C} Daily: {G}{self.u['d']}/5 {W}|{C} Rank: {P}Curse King")
        print(f"{W}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    def show_info(self, tid):
        self.banner()
        print(f"{Y} --- [ {self.ar('شرح الأداة')} {tid} ] ---")
        if self.lang == "AR":
            print(f"{W} 1. الاستخدام: ادخل الرقم وحدد عدد الهجمات.")
            print(f"{W} 2. الغرض: تجميد هاتف الضحية وسحب البيانات.")
            print(f"{W} 3. الخدعة: قل له أنها أداة لزيادة سرعة الإنترنت.")
        else:
            print(f"{W} 1. Usage: Enter number and attack count.")
            print(f"{W} 2. Purpose: Freeze device and pull data.")
            print(f"{W} 3. Trick: Tell them it's an internet booster.")
        input(f"\n{G} {self.ar('اضغط انتر للعودة...')}")

    def attack_ui(self, name):
        self.banner()
        print(f"{C} --- [ {self.ar('بدء الهجوم')}: {name} ] ---")
        target = input(f"{Y} [#] {self.ar('ادخل الرقم المستهدف')}: {W}")
        if target == "+967713551980":
            print(f"{R} هههههه.. هذا رقم المطور! انصحك ألا تقترب من لعنة المالك.")
            time.sleep(3); return
        try:
            count = int(input(f"{Y} [#] {self.ar('كم تريد إرسال طلبات (العدد)')}: {W}"))
        except: count = 10
        
        print(f"{G}\n {self.ar('جاري تشفير الهجوم وإرسال')} {count} {self.ar('طلب')}...")
        for i in range(count):
            time.sleep(0.2)
            print(f"{C} [→] {self.ar('تم الإرسال بنجاح')} ({i+1})...", end="\r")
        print(f"\n{G} ✅ {self.ar('تم الانتهاء بنجاح!')}")
        input("...")

    async def main(self):
        # تسجيل الدخول والترحيب بالالوان
        os.system("clear")
        print(f"{G} مبروك! تم تسجيل دخولك كـ هكر قوي.")
        self.u['n'] = input(f"{Y} ادخل اسم حسابك: {W}")
        
        while True:
            self.banner()
            # الأقسام العشرة
            print(f" {B}[1] {self.ar('الأدوات (100)')}  [2] {self.ar('المتجر النخبوي')}")
            print(f" {B}[3] {self.ar('تجميع النقاط')}   [4] {self.ar('معلومات المطور')}")
            print(f" {B}[5] {self.ar('الإعدادات واللغة')} [6] {self.ar('المتصدرين عالمياً')}")
            print(f" {B}[7] {self.ar('بحث مستخدمين')}   [8] {self.ar('شحن رصيد/لفل')}")
            print(f" {B}[9] {self.ar('خدمات إضافية')}   [10] {self.ar('دردشة عالمية')}")
            
            cmd = input(f"\n{R} SUKUNA > {W}").strip()
            
            if cmd == "1":
                self.banner()
                for i in range(1, 101):
                    lock = "🔓" if i <= self.u['lv'] else "🔒"
                    print(f" [{i}] {self.tools[str(i)]} {lock}", end="\t" if i%3!=0 else "\n")
                choice = input(f"\n\n{Y} اختر رقم الأداة: {W}")
                if choice in self.tools: self.attack_ui(self.tools[choice])
            
            elif cmd.upper().startswith("SUKUNA") and len(cmd) > 6:
                tid = cmd.upper().replace("SUKUNA", "")
                self.show_info(tid)
            
            elif cmd == "4":
                self.banner()
                print(f"{C} المطور: {G}علي طالب (SUKUNA)")
                print(f"{C} واتساب: {W}+967713551980")
                print(f"{C} تلجرام: {W}SUKUNA_i")
                input("\n [SUKUNA] للعودة...")
            
            elif cmd == "5":
                self.lang = "AR" if self.lang == "EN" else "EN"
            
            elif cmd.upper() == "SUKUNA": continue

if __name__ == "__main__":
    app = SukunaEmpireV20()
    asyncio.run(app.main())
