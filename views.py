from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from . models import Add
from . forms import addForm

# Create your views here.

def index(request):
   return render(request, 'index.html')

def signup(request):
   if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      email = request.POST['email']
      my_user = User.objects.create_user(username,email,password)
      my_user.save()
      return redirect('signin')
   return render(request, 'signup.html')

def signin(request):
   if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
         login(request, user)
         return redirect('/form')
      else:
         return redirect('signup')
   return render(request, 'signin.html')

def Logout(request):
     logout(request)
     return render(request,'index.html')



def form(request):
   if request.method == "POST":
      fm = addForm(request.POST)
      if fm.is_valid():
         fm.save()
   else:
      fm = addForm()
   s = Add.objects.all()   
   return render(request,'form.html',{'form':fm,'stud':s})       


  
    


