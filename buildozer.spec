[app]

# (str) عنوان التطبيق
title = مضاد الذنوب

# (str) اسم الحزمة
package.name = ramadanshield

# (str) النطاق
package.domain = org.ramadan.app

# (str) الإصدار
version = 0.1
version.release = 0.1
version.code = 1

# (str) مجلد الكود المصدري
source.dir = .

# (list) أنواع الملفات المضمنة
source.include_exts = py,png,jpg,kv,atlas,txt

# (list) متطلبات بايثون
requirements = python3,kivy==2.1.0,pyjnius,android,requests

# (str) ملف شاشة البداية (اختياري)
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) أيقونة التطبيق
# icon.filename = %(source.dir)s/data/icons/shield_icon.png

# (str) اتجاه العرض
orientation = portrait

# (bool) وضع ملء الشاشة
fullscreen = 0

# (list) أذونات Android
android.permissions = INTERNET,ACCESS_NETWORK_STATE,FOREGROUND_SERVICE,WAKE_LOCK

# (int) مستوى Android API - استخدام إصدار مستقر
android.api = 31

# (int) الحد الأدنى للإصدار
android.minapi = 21

# (int) الـ SDK المستهدف
android.target_sdk = 31

# (str) إصدار build-tools المستقر
android.build_tools = 31.0.0

# (bool) تمكين خدمات Google Play
android.google_play_services = False

# (bool) تمكين وضع الإصدار
android.release = False

# (str) مفتاح التوقيع
android.keystore =

# (list) إضافة خدمة VPN إلى البيان
android.add_activities = org.kivy.android.PythonActivity, org.kivy.android.PythonService

# (str) اسم خدمة VPN
android.service = ramadanshield:main.py

# (bool) تمكين تصحيح الأخطاء
android.debug = True

# (str) إعدادات إضافية للبيان
android.manifest = <application android:label="درع رمضان" android:allowBackup="true" android:icon="@mipmap/ic_launcher"><service android:name="android.net.VpnService" android:permission="android.permission.BIND_VPN_SERVICE"><intent-filter><action android:name="android.net.VpnService"/></intent-filter></service></application>

# (str) إصدار NDK
android.ndk = 23b

# (str) إصدار SDK
android.sdk = 30

[buildozer]

# (int) مستوى تسجيل الأخطاء
log_level = 2

# (str) مسار الحفظ
warn_on_root = 1
