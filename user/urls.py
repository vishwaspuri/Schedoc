from django.contrib.auth.views import LogoutView, LoginView
# from .views import login_view, register_view
from user import views
from user import api
from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("logout", LogoutView.as_view(next_page="/"), name="logout"),
    path("profile", views.my_profile, name="profile"),
    path("otp", views.get_email_and_generate_otp, name="otp"),
    path("otp_verification/<str:email>", views.otp_verification, name="otp-verification"),
    path("send-otp", api.send_otp, name="send-otp"),
    path("update_user", views.update_user, name="update-user"),
    path("view_doctor/<str:doctor_id>", views.view_doctor, name="view-doctor")
]