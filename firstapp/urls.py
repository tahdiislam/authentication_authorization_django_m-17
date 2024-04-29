from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="register"),
    path("login/", views.login_user, name="login"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout_user, name="logout"),
    path('change-pass/', views.change_pass, name='change_pass'),
    path('change-pass-2', views.change_pass2, name='change_pass2')
]
