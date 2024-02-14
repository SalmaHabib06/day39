from django import forms
from myapp.models import Employee

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
    class  Meta:
        model = Employee
        fields='__all__'
        
class SignUpForm(UserCreationForm):
    email       = forms.EmailField()
    first_name  = forms.CharField(required=False,max_length=100)
    last_name   = forms.CharField(required=False,max_length=100)
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)
        
        # fields = "__all__"
        
  #day38      
class EmailForm(forms.Form):
    email = forms.EmailField(max_length=100,widget= forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Email Address'}))
    subject = forms.CharField(max_length=100,widget= forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'subject'}))
    message = forms.CharField(max_length=100,widget= forms.Textarea(attrs={'class':'form-control col-sm-4'}), label=(''))
        
        