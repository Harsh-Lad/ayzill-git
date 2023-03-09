from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signupView, name='signup'),
    path('login/', views.loginView, name='login'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<int:id>', views.blogItem, name='blogs'),
    path('verifyEmail/<str:token>', views.verifyEmail, name='verifyEmail')
]

