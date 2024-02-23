from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages

from . forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from  django.core.mail import EmailMessage
from django.template.loader import render_to_string
# Create your views here.
def index(request):

    return render(request, 'index.html')

def home(request):

    return render(request,'home.html')


def signup(request):

    return render(request,'signup.html')


def userLogin(request):
    if request.method=='POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'succesfully login')
                return redirect('home')
             
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})



def userLogout(request):
    logout(request)
    messages.success(request, 'User logged out')
    return redirect('loginUser')

def registration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user =form.save()
            current_site = get_current_site(request)
            mail_subject = 'an account has been created'
            message = render_to_string('account.html',{
                'user':user,
                'domain':current_site.domain,

                }
                )
            send_mail= form.cleaned_data.get('email')
            email = EmailMessage(mail_subject,message, to=[send_mail])
            email.send()
            messages.success(request,'Successfully created account')

            return redirect('loginUser')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})
   

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password has been changed')
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
        
    return render(request, 'change-pass.html', {'form': form})

# tfmf ycta ejok erfw