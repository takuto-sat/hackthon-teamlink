from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, get_user_model
from django.contrib.auth import login
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import SignUpForm, ProfileForm
from .models import Profile

# Create your views here.
User = get_user_model()

def unlockview(request):
    return render(request, 'home.html')

def signupview(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if signup_form.is_valid() and profile_form.is_valid():
            username = signup_form.cleaned_data.get('username')
            tel_number = signup_form.cleaned_data.get('tel_number')
            password = signup_form.cleaned_data.get('password')
            school_number = profile_form.cleaned_data.get('school_number')
            try:
                user = User.objects.create_user(username, phone_number, password)
                user.profile.school_number = school_number
                user.save()
            except IntegrityError:
                return render(request, 'signup.html', {'error':'このユーザー名はすでに使われています'})
            except  ValueError:
                return render(request, 'signup.html', {'error':'ユーザー名または電話番号を入力してください'})
            user = authenticate(request, username=username, password=password)
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.add_message(request, messages.SUCCESS, 'ユーザー登録が完了しました！')
            return redirect('unlock')
    else:
        signup_form = SignUpForm()
        profile_form = ProfileForm()

    context = {
        'signup_form': signup_form,
        'profile_form': profile_form,
    }
    return render(request, 'signup.html', context)

def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('unlock')
        else:
            return render(request, 'login.html', {'error':'このユーザー名は存在しません'})
    return render(request, 'login.html')