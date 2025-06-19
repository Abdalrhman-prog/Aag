from django.http import HttpResponse

def login_view(request):
    return HttpResponse("صفحة تسجيل الدخول")

def register_view(request):
    return HttpResponse("صفحة تسجيل مستخدم جديد")

def profile_view(request):
    return HttpResponse("صفحة حساب المستخدم")
