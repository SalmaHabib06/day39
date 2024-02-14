from django.urls import path
from myapp import views

urlpatterns = [
    path('list/',views.list_employee,name='employee_list'),
    path('details/<int:id>/',views.view_employee,name='employee_view'),
    path('create/',views.create_employee,name='employee_create'),
    path('edit/<int:id>/',views.edit_employee,name='employee_edit'),
    path('delete/<int:id>/',views.destroy,name='employee_delete'),
    path('register/',views.user_register,name='register'),
    #Day 36 login
    path('login/',views.login_user,name='login_user'),
    path('logout/',views.logout_user,name='logout_user'),
    path('send/',views.sendEmail,name='send'),
    
    
   
   
]
