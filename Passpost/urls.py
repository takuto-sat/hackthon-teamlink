from django.contrib import admin
from django.urls import path
from .views import signupview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signupview,name='signup'),
#    path('login/',loginview, name='login'),
]
