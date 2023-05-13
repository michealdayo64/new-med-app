from django.urls import path
from .views import registerView, loginView, update_profile, logoutView

urlpatterns = [
    path('register-page/', registerView, name = 'register'),
    path('login-page/', loginView, name = 'login'),
    path('logout-page/', logoutView, name = 'logout'),
    path('update-profile/', update_profile, name = 'update-user'),
]