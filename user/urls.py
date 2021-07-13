from django.contrib.auth.views import LogoutView, LoginView
# from .views import login_view, register_view
from user import views
from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("logout", LogoutView.as_view(next_page="/"), name="logout"),
    path("profile", views.my_profile, name="profile")
]