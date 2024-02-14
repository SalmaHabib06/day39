from django.db import models
from datetime import datetime

# Create your models here.
class Department (models.Model):
    name= models. CharField('Department name',max_length=40)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    GENDER_CHOICES = [
        
        ("Male","Male"), ("Female","Female"), ("Other","Other"),
    ]
    
    
    
    name= models.CharField('Employee Name', max_length=100)
    email= models.EmailField('Employee Email', max_length=100, unique=True)
    address= models.TextField('Employee address', max_length=500)
    phone= models.CharField('Employee phone',max_length=20)
    doj= models.DateField('Date of Joining',default=datetime.now, blank= True)
    salary= models.DecimalField('Employee salary',max_digits=8,decimal_places=2)
    gender= models.CharField('Gender', max_length=10,choices=GENDER_CHOICES,default='Male')
    photo= models.FileField('Employee Photo', upload_to='employee', default= 'employee/blank.jpg')
    department= models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__ (self):
        
        return self.name
    
    def delete(self, using=None, Keep_parents=False):
        
        if self.photo.name != 'employee/blank.jpg':
            self.photo.storage.delete(self.photo.name)
        super().delete()
        
    



