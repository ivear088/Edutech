from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as loginUser, logout

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Sas_view,Analysis

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
def sas_view(request):
    if request.method == 'POST':
        
        java=request.POST.get('java'),
        python=request.POST.get('python'),
        ruby=request.POST.get('ruby'),
        html=request.POST.get('html'),
        datascience=request.POST.get('datascience')
        myquery=Sas_view(java=java,python=python,ruby=ruby,html=html,datascience=datascience)
        myquery.save()
        return redirect('/')
        
          # Redirect to a success page or some other page after saving
    return render(request, 'sas.html')

@login_required(login_url='login') 
def analysis(request):
    if request.method=='POST':
        skills=request.POST.get('skills'),
        education_major=request.POST.get('education_major'),
        years_of_experience=request.POST.get('years_of_experience'),
        myquary=Analysis(skills=skills,education_major=education_major,years_of_experience=years_of_experience)
        myquary.save()
        return redirect('/')
    return render(request,'analysis_predi.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            print("ok")
        elif User.objects.filter(email=email).exists():
            
                print("email exits")
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            print("user created")
    
    return render(request,'sign_up.html')
def signin(request):
     if request.method=='POST':
        username=request.POST['username']
        
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print("not ok")
            return redirect('signin')
     else:
        return render(request,'login.html')
     
def signout(request):
    logout(request)
    #using django.contribs logouts the user
    return redirect('/')



    