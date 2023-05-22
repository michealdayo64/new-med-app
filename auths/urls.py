from django.urls import path
from .views import registerView, loginView, update_profile, logoutView, forgetPass, resetPass

urlpatterns = [
    path('register-page/', registerView, name = 'register'),
    path('login-page/', loginView, name = 'login'),
    path('logout-page/', logoutView, name = 'logout'),
    path('update-profile/', update_profile, name = 'update-user'),
    path('forgot-pass/', forgetPass, name = 'forgot-pass'),
    path('reset-pass/', resetPass, name = 'reset-pass')
]