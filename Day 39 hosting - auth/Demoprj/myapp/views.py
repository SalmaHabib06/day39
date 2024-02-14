from django.shortcuts import render,redirect
from myapp.models import Employee

from myapp.forms import EmployeeForm
from django.contrib import messages
from myapp.forms import SignUpForm

from django.core.mail import EmailMessage
from django.conf import settings
from .forms import EmailForm

#Day 36 login

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth. decorators import login_required


# Create your views here.

def index (request) :
    return render (request,'index.html')


# def list_employee(request):
#     return render(request,'list_employee.html')

def list_employee(request):
    allemp = Employee.objects.order_by('-id')
    context = {'employees':allemp}
    return render(request,'list_employee.html',context)

def view_employee(request,id):
    emp = Employee.objects.get(pk=id)
    context = {'employee':emp,'title': 'Employee Details'}
    return render(request,'view_emp.html',context)

#Day 36 login
@login_required(login_url='login')

def create_employee(request):  
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request,"Data Inserted Successfully....")
         
            return redirect('employee_list')
    else:
        form = EmployeeForm()
          
    context = {'title': 'New Employee','form': form}
    return render(request,'empForm.html',context)

def edit_employee(request,id):
    if request.method =="POST":
        employee = Employee.objects.all().order_by('id')
        form = EmployeeForm(request.POST or None, request.FILES,instance=employee)
        if form.is_valid():
            form.save()
        messages.success(request,"Data Updated Successfully...")
        return redirect('employee_list')
    
    else:
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(request.POST or None, instance=employee)
    
    context = {'title':'Edit','form': form,'employee' : employee}
    return render (request, "empForm.html",context)

def destroy(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    messages.success(request,("Data Deleted Successfully"))
    return redirect("employee_list")

def user_register(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('home')
        
    else:
        form = SignUpForm()
        
    context = {'form':form,'title':'Register'}
    return render (request, "registration/register.html",context)

#day 36
def login_user(request):
    if request.method == "POST":
        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(request, username=uname, password=upass)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,("Error logging in try again...."))
            return redirect('login')
    else:
        return render(request,"registration/login.html",{'title':'User Login'})
    
def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out...")
    return redirect('home')

#day 38 email

def sendEmail(request):
    if request.method == 'POST':
       form = EmailForm(request.POST)
       if form.is_valid():
           subject = form.cleaned_data['subject']
           message = form.cleaned_data['message']
           email = form.cleaned_data['email']
           try:
               mail = EmailMessage(subject,message,settings.EMAIL_HOST_USER,[email])
               mail.send()
               messages.success(request,'Email sent successfully ')
               return redirect('home')
           except Exception as e:
               messages.error(request,'Email not sent !!!'+ e)
    else:
        
        form = EmailForm()
    return render(request, "emailForm.html",{'form':form})


    
    
    
        
    
        
        
          
        
    
    
        









