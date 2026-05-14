from django.urls import path
from account import views

from account import views

urlpatterns = [
    path("singup/",views.sing_up,name='singup'),
    path("singin/",views.sing_in,name='singin'),
    path('profile/',views.user_profile,name='profile'),
    path('singout/',views.sing_out,name='singout'),
    path('change-password/',views.user_password_change,name='changepass'),
    path('user-profile-edit/',views.user_profile_edit,name='profile_edit')
]
