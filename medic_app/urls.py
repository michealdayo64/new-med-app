from django.urls import path
from .views import index, about, blog, contact, booking_page, faq, private_policy, t_and_c, registerView, loginView, update_profile


urlpatterns = [
    path('', index, name = 'index'),
    path('about-page/', about, name = 'about'),
   path('blog-page/', blog, name = 'blog'),
   path('contact-page/', contact, name='contact'),
   path('booking-page/', booking_page, name = 'booking'),
   path('faq-page/', faq, name = 'faq'),
   path('private-policy-page/', private_policy, name = 'private-policy'),
    path('t-and-c/', t_and_c, name = 't-and-c'),
    path('register-page/', registerView, name = 'register'),
    path('login-page/', loginView, name = 'login'),
    path('update-profile/', update_profile, name = 'update-user'),
    
    
]