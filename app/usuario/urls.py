from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .forms import LoginForm
from .views import registrar

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="login.html",
            authentication_form=LoginForm,
            redirect_field_name=None,
        ),
        name="login",
    ),
    path("registrar/", registrar, name="registrar"),
    path("logout/", LogoutView.as_view(next_page="index"), name="logout"),
]
