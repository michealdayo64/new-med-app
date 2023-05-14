from django.shortcuts import render
from .models import Ailments
from auths.models import Account
from django.http import JsonResponse

# Create your views here.

def index(request):
    ailment_list = Ailments.objects.all()
    context = {
        "ailment_list": ailment_list
    }
    return render(request, 'index.html', context)

def booking_page(request):
    context = {}
    if request.user.is_authenticated:
        ailment_list = Ailments.objects.all()
        context ["ailment_list"] = ailment_list
    return render(request, 'view/schedule.html', context)

def fifteenMinBook(request):
    data = {}
    if request.user.is_authenticated:
        user_id = request.user.id
        user = Account.objects.get(id = user_id)
        if request.method == "POST":
            user.fifteen_min_trial = True
            user.save()
            data["result"] = "15min free trial Selected"
            return JsonResponse(data = data)
    else:
        data["result"] = "User not authenticated"
        return JsonResponse(data = data)

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

