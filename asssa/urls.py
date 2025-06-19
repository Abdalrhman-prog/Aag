from django.contrib import admin
from django.urls import path, include  # ✅ استدعاء include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ روابط التطبيقات الجديدة
    path('', include('store.urls')),         # الواجهة الرئيسية من تطبيق store
    path('accounts/', include('accounts.urls')),   # تسجيل الدخول، حسابي، إلخ
    path('dashboard/', include('dashboard.urls')), # لوحة التحكم
]
