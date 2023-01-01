from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from .forms import SignUpForm,Profileform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import UserProfile
# Create your views here.

def signup(request):
    form = SignUpForm
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('loginapp:login'))

    dict = {'form':form}
    return render(request,'loginapp/signup.html',dict)        


def login_page(request):
    form = AuthenticationForm
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged In Successfully!')
                # return HttpResponse('Logged In!')
                return HttpResponseRedirect(reverse('loginapp:profile'))

    dict = {'form':form}
    return render(request,'loginapp/login.html',dict)        

def logout_page(request):
    logout(request)
    messages.warning(request,'Logged Out!')
    return HttpResponseRedirect(reverse('loginapp:login'))

def profile(request):
    return render(request,'loginapp/profile.html')

def update_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = Profileform(instance=current_user)
    if request.method =='POST':
        form = Profileform(request.POST,request.FILES,instance=current_user)
        if form.is_valid():
            form.save()
            form = Profileform(instance=current_user)
            messages.success(request,'Profile is Updated Successfully!')
            return HttpResponseRedirect(reverse('loginapp:profile'))

    dict = {'form':form}
    return render(request,'loginapp/update_profile.html',dict)        