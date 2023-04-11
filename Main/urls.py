from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    ##### faculty urls #########
    path('flogin', views.flogin, name='flogin'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('create', views.create, name='create'),
    path('create_account', views.create_account, name='create'),
    path('marks', views.marks, name='marks'),
    path('update_marks', views.updated_marks, name='update_marks'),
    path('check', views.check_marks, name='check'),
    path('faculty', views.faculty, name='faculty'),

    ###### student urls #######
    path('student', views.student, name='student'),
    path('shome', views.shome, name='shome'),
    path('slogin', views.slogin, name='slogin'),
    path('slogout', views.slogout, name='slogout'),
    path('smarks', views.smarks, name='smarks'),
    # path('cmstudent', views.cmstudent, name='cmstudent'),
]