from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,'inavlid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        username =request.POST['username']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        email =request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists(): 
                messages.info(request,'mail id taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
             messages.info(request,'password name taken')
             return redirect('register')
                
        return redirect('/')

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def meal(request):
    if request.method == 'POST':
        meal=request.POST['meal']
        if meal == 'idly':
            print('yes')
            messages.info(request,'50g of protein')
            return redirect('/')
        if meal == 'sambar':
            print('yes')
            messages.info(request,'100g of protein')
            return redirect('/')
        if meal == 'ooats':
            print('yes')
            messages.info(request,'75g of protein')
            messages.info(request,'50g of fibre')
            return redirect('/')
        if meal == 'biriyani':
            print('yes')
            messages.info(request,'Protein	4.8 g	9% Carbohydrates	13.9 g	5% Fiber	3.3 g	13% Fat	17.9 g	27%')
           
            return redirect('/')
        if meal == 'parotta':
            print('yes')
            messages.info(request,'2.5g of protein')
            messages.info(request,'17.8g of carb')
            return redirect('/')
        if meal == 'chapathi':
            print('yes')
            messages.info(request,'3g of protein')
            messages.info(request,'0.4g of fibre')
            return redirect('/')
        if meal == 'dosa':
            print('yes')
            messages.info(request,'2.7g of protein')
            messages.info(request,'18.8g of fibre')
            return redirect('/')
        if meal == 'curd rice':
            print('yes')
            messages.info(request,'8.5g of protein')
            messages.info(request,'36.9g of carb')
            return redirect('/')
        if meal == 'upma':
            print('yes')
            messages.info(request,'4g of protein' )
            messages.info(request,'7g of carbs' )
            
            return redirect('/')