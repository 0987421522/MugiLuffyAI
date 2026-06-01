[app]

# اسم التطبيق
title = MUGIWARA & LUFFY AI

# اسم الحزمة
package.name = mugiluffyai

# اسم الحزمة الكامل (فريد)
package.domain = com.mugiwara.luffy

# الإصدار
version = 1.0.0

# لغة التطبيق
source.dir = .
source.include_exts = py,png,jpg,jpeg,gif,wav,mp3,ttf

# المتطلبات
requirements = python3,kivy

# أذونات Android
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_MEDIA_IMAGES

# أيقونة التطبيق
icon.filename = %(source.dir)s/icon.png

# التوقيع
android.api = 31
android.minapi = 21
android.sdk.api_level = 31
android.ndk = 23b
android.sdk = 24

# اسم المخرجات
android.filename = MugiLuffyAI-v1.0

# صورة الشاشة الافتتاحية
presplash.filename = %(source.dir)s/splash.png
