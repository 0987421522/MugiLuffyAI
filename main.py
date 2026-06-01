"""
MUGIWARA & LUFFY AI - نسخة Termux
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import os

# =================== المسارات ===================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# صورتك - نفس الاسم اللي نسخته
SPLASH_IMAGE = os.path.join(BASE_DIR, "splash.jpg")

# صوتك
SOUND_FILE = os.path.join(BASE_DIR, "startup.mp3")

# =================== الألوان ===================
BLACK = (0, 0, 0, 1)
RED = (0.9, 0, 0, 1)
GREEN = (0, 0.8, 0, 1)
DARK_RED = (0.3, 0, 0, 1)
WHITE = (1, 1, 1, 1)
GRAY = (0.15, 0.15, 0.15, 1)

# =================== شاشة البداية ===================
class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
        with layout.canvas.before:
            Color(*BLACK)
            Rectangle(size=Window.size, pos=layout.pos)
        
        # تشغيل الصوت
        if os.path.exists(SOUND_FILE):
            sound = SoundLoader.load(SOUND_FILE)
            if sound:
                sound.play()
        
        # عرض الصورة
        if os.path.exists(SPLASH_IMAGE):
            img = Image(
                source=SPLASH_IMAGE,
                size_hint=(1, 0.85),
                allow_stretch=True,
                keep_ratio=True
            )
            layout.add_widget(img)
        else:
            layout.add_widget(Label(
                text="MUGIWARA & LUFFY\n🏴‍☠️ AI 🏴‍☠️",
                font_size=36,
                color=RED,
                bold=True
            ))
        
        # اسم أسفل الصورة
        layout.add_widget(Label(
            text="MUGIWARA & LUFFY AI",
            font_size=22,
            color=GREEN,
            bold=True,
            size_hint_y=0.1
        ))
        
        self.add_widget(layout)
        
        # بعد 4 ثواني → الشاشة الرئيسية
        Clock.schedule_once(self.go_to_main, 4)
    
    def go_to_main(self, dt):
        self.manager.current = 'main'

# =================== الشاشة الرئيسية ===================
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main = BoxLayout(orientation='vertical', padding=3, spacing=3)
        
        with main.canvas.before:
            Color(*BLACK)
            Rectangle(size=Window.size, pos=main.pos)
        
        # ===== الهيدر الأحمر =====
        header = BoxLayout(size_hint_y=0.07)
        with header.canvas.before:
            Color(*DARK_RED)
            header.rect = Rectangle(size=header.size, pos=header.pos)
        header.bind(pos=self.upd_rect, size=self.upd_rect)
        header.add_widget(Label(text="🏴‍☠️ MUGIWARA & LUFFY 🏴‍☠️", fontSize=16, bold=True, color=WHITE))
        main.add_widget(header)
        
        # ===== صورتك في البروفايل =====
        if os.path.exists(SPLASH_IMAGE):
            profile = Image(
                source=SPLASH_IMAGE,
                size_hint_y=0.2,
                allow_stretch=True,
                keep_ratio=True
            )
            main.add_widget(profile)
        
        # ===== الاسم =====
        name_box = BoxLayout(size_hint_y=0.06, spacing=10)
        name_box.add_widget(Label(text="MUGIWARA", fontSize=20, bold=True, color=RED))
        name_box.add_widget(Label(text="لوفي 🏴‍☠️", fontSize=18, color=GREEN))
        main.add_widget(name_box)
        
        # ===== منطقة الشات =====
        scroll = ScrollView(size_hint_y=0.5)
        self.chat = BoxLayout(orientation='vertical', size_hint_y=None, spacing=2)
        self.chat.bind(minimum_height=self.chat.setter('height'))
        
        # رسالة ترحيب
        welcome = Label(
            text="مرحباً! أنا MUGIWARA & LUFFY AI 🏴‍☠️\nاسألني عن الهكر، البرمجة، التداول...",
            size_hint_y=None,
            height=70,
            color=GREEN,
            halign='left',
            text_size=(Window.width - 20, None)
        )
        self.chat.add_widget(welcome)
        scroll.add_widget(self.chat)
        main.add_widget(scroll)
        
        # ===== حقل الإدخال =====
        inp = BoxLayout(size_hint_y=0.07, spacing=3)
        self.inp_field = TextInput(
            hint_text="اكتب سؤالك...",
            multiline=False,
            background_color=GRAY,
            foreground_color=WHITE,
            cursor_color=GREEN
        )
        self.inp_field.bind(on_text_validate=self.send)
        inp.add_widget(self.inp_field)
        send_btn = Button(text="← إرسال", background_color=RED, color=WHITE, size_hint_x=0.2)
        send_btn.bind(on_press=self.send)
        inp.add_widget(send_btn)
        main.add_widget(inp)
        
        # ===== أزرار سفلية =====
        bottom = BoxLayout(size_hint_y=0.06, spacing=3)
        btn_clear = Button(text="مسح", background_color=DARK_RED, color=WHITE)
        btn_clear.bind(on_press=self.clear_chat)
        bottom.add_widget(btn_clear)
        btn_help = Button(text="مساعدة", background_color=(0,0.3,0,1), color=WHITE)
        btn_help.bind(on_press=self.show_help)
        bottom.add_widget(btn_help)
        main.add_widget(bottom)
        
        self.add_widget(main)
    
    def upd_rect(self, instance, val):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size
    
    def send(self, instance):
        text = self.inp_field.text.strip()
        if not text:
            return
        
        user = Label(
            text=f"👤 {text}",
            size_hint_y=None,
            height=35,
            color=GREEN,
            halign='left',
            text_size=(Window.width - 20, None)
        )
        self.chat.add_widget(user)
        
        # توليد رد
        reply = self.get_reply(text)
        bot = Label(
            text=f"🤖 {reply}",
            size_hint_y=None,
            color=RED,
            halign='left',
            text_size=(Window.width - 20, None)
        )
        bot.bind(texture_size=lambda i, v: setattr(bot, 'height', max(35, v[1]+5)))
        self.chat.add_widget(bot)
        
        self.inp_field.text = ""
    
    def get_reply(self, q):
        q = q.lower()
        if any(w in q for w in ['python', 'بايثون', 'برمجة', 'كود']):
            return "Python:\nprint() → طباعة\ninput() → إدخال\nif/else → شرط\nfor → حلقة\nimport os → استيراد"
        elif any(w in q for w in ['هكر', 'اختراق', 'nmap', 'ثغرة']):
            return "أدوات الاختراق:\nNmap - فحص الشبكات\nMetasploit - استغلال الثغرات\nSQLMap - حقن SQL\nBurp Suite - ويب"
        elif any(w in q for w in ['تداول', 'trading', 'سهم', 'فوركس']):
            return "التداول:\nالتحليل الفني\nالتحليل الأساسي\nإدارة رأس المال\nRSI, MACD, EMA"
        else:
            return f"سؤالك: {q}\n\nأهلاً بك! أنا MUGIWARA 🤖\nاسألني عن: برمجة، هكر، تداول، أو أي شيء!"
    
    def clear_chat(self, instance):
        self.chat.clear_widgets()
        self.chat.add_widget(Label(text="تم المسح ✅", size_hint_y=None, height=40, color=GREEN))
    
    def show_help(self, instance):
        help_text = """🏴‍☠️ MUGIWARA & LUFFY AI 🏴‍☠️
 إصدار 1.0

الأوامر:
/مسح - مسح المحادثة
/مساعدة - هذه المساعدة

يمكنني مساعدتك في:
• الهكر والاختراق الأخلاقي
• البرمجة (Python)
• التداول والأسواق
• أي سؤال آخر

صورتك: luffy.jpg 🖼️
صوتك: Monkey D Luffy 🎵
الألوان: أحمر + أخضر + أسود"""
        msg = Label(
            text=help_text,
            size_hint_y=None,
            color=GREEN,
            halign='left',
            text_size=(Window.width - 20, None)
        )
        msg.bind(texture_size=lambda i, v: setattr(msg, 'height', v[1]+5))
        self.chat.add_widget(msg)

# =================== تشغيل التطبيق ===================
class MugiLuffyApp(App):
    def build(self):
        self.title = "MUGIWARA & LUFFY AI"
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    MugiLuffyApp().run()
