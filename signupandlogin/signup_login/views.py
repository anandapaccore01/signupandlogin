from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db.models import Q
from .models import *
from .utill import *
import random
import string


# Create your views here.

def Registerview(request): 
    if request.method == 'POST':
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
        return HttpResponse('User is successfully register, A verification link is sent your email')
    else:     
        return render(request,'registrations.html')
        
def loginview(request):
    if request.method == 'POST':
        username1=request.POST.get('username') 
        password = request.POST.get('password')
        my_user = CustomUsers.objects.filter(Q(username=username1) | Q(email=username1)).first()
        if my_user is not None:
            username = my_user.username
            if my_user.status == 'Active':
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponse('u login successfully')
                else:
                    return HttpResponse('Invalid credentials')
            else:
                return HttpResponse('Please verify your email before login')        
            # if user is not None:
                
        else:
            return HttpResponse('Invalid credentials')
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
    return redirect('login')

def resetpasswordView(request):    
    if request.method == 'POST':
        email=request.POST.get('useremail')
        user=CustomUsers.objects.filter(email=email).first()
        if user is not None:
             
            request.session['token'] = PasswordResetTokenGenerator().make_token(user)
            send_resetpasswordemail(user, request.session['token'])
            
        else:
            return HttpResponse('User is not found')
         
    return render(request, 'reset_password.html')

def resetpassword(request, pk=None):    
    user_id=request.GET.get('user_id','')
    user = CustomUsers.objects.get(pk=user_id)
    token = request.GET.get('token','')
    check = PasswordResetTokenGenerator().check_token(user,token=token)
    return HttpResponse(check)

def resetpasswordconfirm(request):
    return (request, 'change_password.html')

