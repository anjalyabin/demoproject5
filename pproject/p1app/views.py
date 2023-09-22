
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
from django.contrib import messages,auth

def login(request):
     if request.method=='POST':
          username2=request.POST['username']
          password2=request.POST['password']
          user=auth.authenticate(username=username2,password=password2)
          if user is not None:
               auth.login(request,user)
               return redirect('/')
          else:
               message.info(request,"invalid credentials")
               return redirect('p1app:login')
     else:

          return render(request,"login.html")
def register(request):
   if request.method == 'POST':
        username1 = request.POST['username']
        firstname1 = request.POST['firstname']
        lastname1 = request.POST['lastname']
        email1 = request.POST['email']
        password1 = request.POST['password']
        cpassword1= request.POST['cpassword']
        if password1 == cpassword1 :
             if User.objects.filter(username=username1).exists():
                  messages.info(request, 'username already exist')
                  return redirect('p1app:register')
             else:
                  if User.objects.filter(email=email1).exists():
                       messages.info(request, 'Registration Failed - Try different email address')
                       return redirect('p1app:register')
                  else:


                       user = User.objects.create_user(password=password1,username=username1,first_name=firstname1,last_name=lastname1,email=email1)
                       user.save();

                       print("user created")
                       return redirect('p1app:login')
        else:
             messages.info(request, 'password dose not match')
             return redirect('p1app:register')
        return redirect('/')

   else:

        return render(request, "register.html")
def logout(request):
     auth.logout(request)
     return redirect('p1app:register')
