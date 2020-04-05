from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views
from .views import SignupView, LoginView

app_name="auths"

urlpatterns = [
    path('register/', SignupView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('base-connect/', views.baseConnect, name='baseConnect'),
    path('base-connect/ajax/follow/', views.follow, name='follow')
    ]
