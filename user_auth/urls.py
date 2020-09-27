from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('register', views.signup, name="signup"),
    path('login', views.UserLogin.as_view(), name="login"),
    path('logout', views.logout_view, name="logout"),
]
