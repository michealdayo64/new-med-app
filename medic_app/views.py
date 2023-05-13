from django.shortcuts import render
from .models import Ailments

# Create your views here.

def index(request):
    ailment_list = Ailments.objects.all()
    context = {
        "ailment_list": ailment_list
    }
    return render(request, 'index.html', context)

def booking_page(request):
    return render(request, 'view/schedule.html')

def blog(request):
    return render(request, 'view/blog.html')

def about(request):
    return render(request, 'view/about.html')

def contact(request):
    return render(request, 'view/contact.html')

def faq(request):
    return render(request, 'view/faq.html')

def private_policy(request):
    return render(request, 'view/private_policy.html')

def t_and_c(request):
    return render(request, 'view/t_and_c.html')

