from django.shortcuts import render,redirect

import json
# 6565161651656
# Create your views here.

def index1(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def logins(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        return redirect('主界面')


