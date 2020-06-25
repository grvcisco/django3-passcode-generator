from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home1(request):
    return HttpResponse("Hi There!!")

def home(request):
    return render(request, 'generator/home.html', {'passcode':'GameOfThrones'})

def generatedPasscode(request):
    genPass = ''
    strList = list('abcdefghijklmnopqrstuvwxyz')
    passLen = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        upperList = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        strList.extend(upperList)
        
    if request.GET.get('number'):
        numList = list('1234567890')
        strList.extend(numList)
        
    if request.GET.get('alphanumeric'):
        alphaList = list('!@#$%^&*()_+{}[]')
        strList.extend(alphaList)
        
    for _ in range(passLen):
        genPass += random.choice(strList)
    
    print(request.GET.get('number'))
    print(request.GET.get('alphanumeric'))
    print(request.GET.get('uppercase'))
    
    return render(request, 'generator/passcode.html', {'passcode':genPass})