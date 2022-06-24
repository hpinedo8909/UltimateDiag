from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    # Home page
    path('', views.index, name='home'),
    path('login', views.log_in, name='log_in'),
    path('register', views.register, name='register')
]
