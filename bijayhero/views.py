from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect

import sys, os 
import json
import requests




from django.shortcuts import render
from django.http import HttpResponse
from . import models

from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse



def register_fun(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        phone = request.POST.get('phone', False)
        email = request.POST.get('email', False)
        print ('im inisde here**************')
        models.register_model(username, password, phone, email)
        return redirect('login')
    return render(request, 'register.html')






def login_fun(request):
    if request.session.__contains__('username'):
        return render(request, 'dashboard.html', {})


    if request.method == 'POST':
        uname = request.POST.get('name', False)
        pwd = request.POST.get('password', False)

        phone_no = models.login_model(uname, pwd)
        # print uname + pwd
        if phone_no != None:
            request.session['username'] = uname
            request.session['phone']= phone_no

            models.is_active(uname, phone_no)
            return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html', {})


    return render(request, 'login.html', {})


def logout_fun(request):
    uname= request.session['username']
    phone= request.session['phone']
    models.is_inactive(uname,phone)
    request.session.flush()
    return redirect('login')



def online(request):
    online_users=models.is_online()
    return render(request,'online.html',{'online_users':online_users})

