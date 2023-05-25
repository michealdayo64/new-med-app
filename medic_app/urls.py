from django.urls import path
from .views import index, about, blog, contact, booking_page, faq, private_policy, t_and_c, fifteenMinBook, bookingDetails, bookingSummary, getAllAppointment, paymnent
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', index, name = 'index'),
    path('about-page/', about, name = 'about'),
   path('blog-page/', blog, name = 'blog'),
   path('contact-page/', contact, name='contact'),
   path('booking-page/', booking_page, name = 'booking'),
   path('faq-page/', faq, name = 'faq'),
   path('private-policy-page/', private_policy, name = 'private-policy'),
    path('t-and-c/', t_and_c, name = 't-and-c'),
    path('fifteen-min/', csrf_exempt(fifteenMinBook), name = 'fifteen-min'),
    path('booking-order/', csrf_exempt(bookingDetails), name = 'booking-order'),
    path('booking-order/<id>/', csrf_exempt(bookingDetails), name = 'booking-order-id'),
    path('summary/<id>/', bookingSummary, name = "summary-id"),
    path('get-appointment/', getAllAppointment, name='get-appointment'),
    path('payment/', paymnent, name='payment')
]
