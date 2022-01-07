from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, get_user_model
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
            user = User.objects.create_user(username, phone_number, password)
            user.profile.school_number = school_number
            user.save()

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
