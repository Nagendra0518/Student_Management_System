from django.urls import path

from sales import views

urlpatterns = [
    path('',views.login_fun,name='log'),
    path('signup/',views.signup_fun,name="sigup"),
    path('home/',views.home_fun,name="home"),
    path('add/',views.add_student,name="add"),
    path('display/',views.display_student,name="display"),
    path('update/<int:id>',views.update_student,name="update"),
    path('delete/<int:id>',views.delete_student,name="delete"),
]