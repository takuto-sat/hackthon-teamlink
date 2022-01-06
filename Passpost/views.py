from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login


# Create your views here.
def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        phone_number = request.POST.get('phone_number_data')
        student_number = request.POST.get('student_number')
        user = User.objects.create_user(username_data, '',password_data,'',phone_number,'',student_number)
        try:
            User.objects.create_user(username_data,'',password_data,'',phone_number,'',student_number)
        except IntegrityError:
            return render(request, 'signup.html',{'error':'このユーザーはすでに登録されています。'})


    else:
        return render(request, 'signup.html', {})

"""
def loginview(request):
    if request.method=='POST':
            username_data = request.POST['username_data']
            password_data = request.POST['password_data']
            user = authenticate(request, username=username_data,password=password_data)
            if user is not None:
                login(request,user)
                return redirect('list')
            else:
                return redirect('login')
    return render(request, 'login.html')

"""