from django.urls import path
from django.contrib.auth import views as authViews
from . import views
from .forms import LoginForm

urlpatterns = [
    path('login/', authViews.LoginView.as_view(template_name='user/login.html', redirect_authenticated_user=True, authentication_form=LoginForm), name="user-login"),
    path('logout/', authViews.LogoutView.as_view(template_name='user/logout.html', next_page='/user/login'), name="user-logout"),
    path('register/', views.register, name='user-register'),

]