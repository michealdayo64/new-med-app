from datetime import datetime
from django.shortcuts import render
from .models import Ailments, Appointment
from auths.models import Account
from django.http import JsonResponse
import json

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

def writeUs(request):
    pass

def fifteenMinBook(request):
    data = {}
    if request.user.is_authenticated:
        user_id = request.user.id
        user = Account.objects.get(id = user_id)
        if request.method == "POST":
            user.fifteen_min_trial = True
            user.save()
            data["response"] = "15min free trial Selected"
            return JsonResponse(data = data)
    else:
        data["response"] = "User not authenticated"
        return JsonResponse(json.dumps(data), safe=False)
    
def bookingDetails(request, id = None):
    payload = {}
    ns = json.loads(request.body)
    user = request.user
    if request.user.is_authenticated:
        if request.method == "POST":
            date = ns["date"]
            date_format = datetime.strptime(date, '%d/%m/%Y')
            time = ns["time"]
           
            phone_no = ns["phone"]
            
            message = ns["message"]
            

            if id:
                ailment_id = Ailments.objects.get(id = id)
                Appointment.objects.create(user = user, ailment_id = ailment_id, phone_no = phone_no, message = message, date = date_format, appointment_time = time)
                payload["response"] = "Appointment Order"
                return JsonResponse(json.dumps(payload), safe=False)
            else:
                Appointment.objects.create(user = user, phone_no = phone_no, message = message, date = date_format, appointment_time = time)
                payload["response"] = "Appointment Order"
                return JsonResponse(json.dumps(payload), safe=False)
    else:
        payload["response"] = ["User not authenticated"]
        return JsonResponse(json.dumps(payload), safe=False)

def bookingSummary(request, id = None):
    payload = {}
    user = request.user
    if user.is_authenticated:
        if id:
            appointment = Appointment.objects.filter(ailment_id = id)[0]
            print(appointment)
            payload = {
                    "firstname": appointment.user.first_name,
                    "lastname": appointment.user.last_name,
                    "service": appointment.ailment_id.title,
                    "date_and_time": f'{appointment.date}, {appointment.appointment_time}'
                }
            return JsonResponse(data = payload, safe=False)
        else:
            appointment = Appointment.objects.filter(ailment_id = id)[0]
            print(appointment)
            payload = {
                    "firstname": appointment.user.first_name,
                    "lastname": appointment.user.last_name,
                    "service": "15min Consultation",
                    "date_and_time": f'{appointment.date}, {appointment.appointment_time}'
                }
            return JsonResponse(data = payload, safe=False)
    else:
        payload["response"] = "User not authenticated"
        return JsonResponse(json.dumps(payload), safe=False)


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

