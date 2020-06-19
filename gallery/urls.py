from django.urls import path
from . import views
from account import views as account_view

app_name = 'gallery'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),

    path('login', account_view.Login.as_view(), name='login'),
    path('logout', account_view.Logout.as_view(), name='logout'),
    path('register', account_view.Register.as_view(), name='register')
]