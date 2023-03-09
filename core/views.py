from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Product, Blog
from uuid import uuid4
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.

def emailer(subject,to,message,name):
    msg_html = render_to_string('email/verifyEmail.html', {'name':name,'token':message})
    send_mail(
        subject,
        message,
        'developer@earthie.co.in',
        [to],
        fail_silently=False,
        html_message=msg_html,
    )

def home(request):
    prods = Product.objects.all()
    prods = prods.filter(is_published=True)
    param = {
        'prods' : prods
    }
    return render(request, 'home.html', param)

def signupView(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        name = fname + " " + lname
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        if not User.objects.filter(email=email):
            token = str(email) + str(uuid4()) + str(phone)
            user = User(name=name,email=email,phone=phone,token=token)
            user.set_password(password)
            user.save()
            subject = "Please Verify your account"
            message = f"http://127.0.0.1:8000/verifyEmail/{token}"
            emailer(subject,email,message,name)
        else:
            print('user already exists')

        
    return render(request, 'signup.html')

def verifyEmail(request,token):
    user = User.objects.filter(token=token)
    if user:
        user1 = User.objects.get(token=token)
        print(user1)
        user1.is_verified = True
        user1.save()
    return redirect('/signup/')

def loginView(request):
    return render(request, 'login.html')

def blogs(request):
    allBlogs =  Blog.objects.all()
    allBlogs = allBlogs.filter(status='publish')
    param = {
        'blogs' : allBlogs
    }
    return render(request, 'blog.html',param)

def blogItem(request,id):
    blog = Blog.objects.all()
    blog = blog.get(id=id)
    param = {
        'blog' : blog
    }

    return render(request, 'blogItem.html',param)
