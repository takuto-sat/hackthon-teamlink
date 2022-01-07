from django.contrib import admin
from django.urls import path
from .views import signupview, unlockview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signupview,name='signup'),
    path('unlock', unlockview, name='unlock'),
    path('login/',loginview, name='login'),
]
