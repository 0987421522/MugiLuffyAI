[app]

title = MUGIWARA LUFFY AI
package.name = mugiwara_luffy
package.domain = com.mugiwara.luffy
version = 1.0.0

source.dir = .
source.include_exts = py,png,jpg,jpeg,wav,mp3

requirements = python3,kivy

android.permissions = INTERNET,READ_EXTERNAL_STORAGE

orientation = portrait
fullscreen = 0

# 🔥 إعدادات أندرويد المهمة
android.minapi = 21
android.sdk.api_level = 31
android.ndk = 28c

# أيقونة (اختياري إذا موجودة)
# icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
