from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib import messages
from django.db.models import Q
from .forms import Myform
from .models import *
from .utill import *
import random
import string


# Create your views here.
def homeview(request):
    return render(request, 'base.html')

def Registerview(request): 
    if request.method == 'POST':
        form=Myform(request.POST)
        if form.is_valid():    
            user = CustomUsers.objects.create(
                first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                username = request.POST.get('username'),
                date_of_birth = request.POST.get('date_of_birth'),
                gender = request.POST.get('gender'),
                email = request.POST.get('email'),   
                phone = request.POST.get('phone'),
                verify_string="".join(random.choices(string.ascii_letters+string.digits,k=20)),
                )
            user.set_password(request.POST.get('password'))
            user.save()
            sendemail(user, request.POST.get('password'))
            messages.success(request,'User is successfully register, A verification link is sent your email')
            return redirect('Register')
        else:
            return render(request,'registrations.html',{'form':form}) 
    else:
        form = Myform()    
        return render(request,'registrations.html',{'form':form})
        
def loginview(request):
    if request.method == 'POST':
        username=request.POST.get('username')         
        password = request.POST.get('password')
        try:
            my_user = CustomUsers.objects.get(Q(username=username)|Q(email=username))
        except CustomUsers.DoesNotExist:
            my_user=None        
        if my_user is not None:
            username = my_user.username
            if my_user.status == 'Active':
                user = authenticate(username=username, password=password)
                if user is not None:                    
                    login(request, user)                    
                    return HttpResponseRedirect('profile/%d'%user.id)
                else:
                    messages.error(request, 'Invalid credentials')
                    return redirect('login')
            else:
                messages.error(request, 'your email is not verified, Please check your register EMAIL ID.')
                return redirect('login')       
        else:
           messages.error(request, 'Invalid credentials')
           return redirect('login')
    else:
        return render(request, 'login.html')

def emailactivate(request, pk=None):    
    user_id=request.GET.get('user_id','')
    confirmation_token = request.GET.get('confirmation_token','')
    try:
        user=CustomUsers.objects.get(pk=user_id) 
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is None:
        return  HttpResponse('User not found')
    if not (user, confirmation_token):
        return HttpResponse('Token is invalid or expired. Please request another confirmation email by signing in.')
    user.is_active = True
    user.status = 'Active'
    user.save()
    messages.success(request, 'Successfully, your EMAIL ID is verified. you can login now.')
    return redirect('login')

def resetpasswordView(request):    
    if request.method == 'POST':
        email=request.POST.get('useremail')
        user=CustomUsers.objects.filter(email=email).first()
        if user is not None:             
            request.session['token'] = PasswordResetTokenGenerator().make_token(user)
            send_resetpasswordemail(user, request.session['token'])            
        else:
            messages.error(request, 'User is not found')
            return redirect('resetpasswordview')         
    return render(request, 'reset_password.html')

def resetpassword(request, pk=None):
    user_id=request.GET.get('user_id','')
    user = CustomUsers.objects.get(pk=user_id)
    token = request.GET.get('token','')
    check = PasswordResetTokenGenerator().check_token(user,token=token)
    if check:
       if request.method=='POST':
            password=request.POST.get('password')
            user.set_password(password)
            user.save()
            return redirect('login')
       return render(request, 'change_password.html')
    else:
        return HttpResponse(" Invalid user or token")
    

def Profileview(request,id):
    user=CustomUsers.objects.get(id=id)
    
    return render(request, 'profile.html',{'user':user})

def logoutview(request):
    logout(request)
    messages.info(request,'u logout successfully')
    return redirect('login')

def changeemail(request):
    if request.method == 'POST':
        id=request.POST.get('user_id')
        user=CustomUsers.objects.get(id=id)

        email=request.POST.get('email')
        try:
            email1=CustomUsers.objects.get(email=email)
        except(TypeError, ValueError, OverflowError, user.DoesNotExist):
            email1=None
        
        if email1 is None:
            sendchangeemail(email,user)
        else:
            print(type(id)) 
            messages.error(request, 'This email is already exists, Please give another email')
            return HttpResponseRedirect('profile/%d'%int(id))            
        messages.success(request,'A verification link is sent your new email, please verify emailID')
        user.email=email
        user.save()
        print(user.email)
        return redirect('logout')
