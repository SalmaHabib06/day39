from django.contrib import admin
from myapp.models import Department,Employee

#day38

from import_export import resources
from import_export.admin import ImportExportMixin

# Register your models here.
#export
class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
        exclude = ('photo',)

#Export
# class EmployeeAdmin(ImportExportMixin,admin.ModelAdmin):
        
#         db_table = ''
#         managed = True
#         verbose_name = 'ModelName'
#         verbose_name_plural = 'ModelNames'
class EmployeeAdmin(ImportExportMixin,admin.ModelAdmin):
            
    search_fields = ['email','name']
    
    list_display = ['name','email','phone','doj','salary']
    list_per_page = 6
    
    #import
    resource_class = EmployeeResource
    
    #class Meta:
        #model = Employee
        


admin.site.register(Department)
admin.site.register(Employee,EmployeeAdmin)


    