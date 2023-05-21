from datetime import datetime
from django.shortcuts import render, redirect
from .models import Ailments, Appointment
from auths.models import Account
from django.http import JsonResponse
import json
from django.contrib import messages
from .forms import WriteUsForm

# Create your views here.

def index(request):
    ailment_list = Ailments.objects.all()
    if request.method == "POST":
        form = WriteUsForm(request.POST or None)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, "Form Submitted Successfully")     
            return redirect('index')   
        else:
            WriteUsForm()
            messages.success(request, "You need to fill the form")     
            return redirect('index') 
    context = {
        "ailment_list": ailment_list
    }
    return render(request, 'index.html', context)

def booking_page(request):
    context = {}
    if request.user.is_authenticated:
        ailment_list = Ailments.objects.all()
        context ["ailment_list"] = ailment_list
    else:
        messages.info(request, "You have to Login to book an appointmnt")
        return redirect("index")
    return render(request, 'view/schedule.html', context)

"""def writeUs(request):
    if request.method == "POST":
        form = WriteUsForm(request.POST or None)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, "Form Submitted Successfully")     
            return redirect('index')   
    else:
        WriteUsForm()
        return render(request, 'view/write_us.html')"""
    
    

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
                app_id = Appointment.objects.create(user = user, ailment_id = ailment_id, phone_no = phone_no, message = message, date = date_format, appointment_time = time, is_booked = False)
                payload["response"] = "Appointment Order"
                payload['app_id'] = app_id.id
                payload['firstname'] = app_id.user.first_name
                payload['lastname'] = app_id.user.last_name
                payload['service'] = app_id.ailment_id.title
                payload['date_and_time'] = f'{app_id.date}, {app_id.appointment_time}'
                return JsonResponse((payload), safe=False)
            else:
                app_id = Appointment.objects.create(user = user, phone_no = phone_no, message = message, date = date_format, appointment_time = time, is_booked = False)
                payload["response"] = "Appointment Order"
                payload['app_id'] = app_id.id
                payload['firstname'] = app_id.user.first_name
                payload['lastname'] = app_id.user.last_name
                payload['service'] = "15min Consultation"
                return JsonResponse((payload), safe=False)
    else:
        payload["response"] = ["User not authenticated"]
        return JsonResponse(json.dumps(payload), safe=False)

'''def bookingSummary(request, id = None):
    payload = {}
    user = request.user
    if user.is_authenticated:
        if id:
            #ailment_id = Ailments.objects.get(id = id)
            #print(ailment_id)
            appointment = Appointment.objects.filter(id = id).first()
            if appointment:
                appoint = appointment
            #print(appointment.date, appointment.appointment_time)
                payload = {
                        "firstname": appoint.user.first_name,
                        "lastname": appoint.user.last_name,
                        "service": appoint.ailment_id.title,
                        "date_and_time": f'{appoint.date}, {appoint.appointment_time}'
                    }
                return JsonResponse(data = payload, safe=False)
        else:
            appointment = Appointment.objects.all().first()

            payload = {
                    "firstname": appointment.user.first_name,
                    "lastname": appointment.user.last_name,
                    "service": "15min Consultation",
                    "date_and_time": f'{appointment.date}, {appointment.appointment_time}'
                }
            return JsonResponse(data = payload, safe=False)
    else:
        payload["response"] = "User not authenticated"
        return JsonResponse(json.dumps(payload), safe=False)'''
    

def bookingSummary(request, id):
    payload = {}
    user = request.user
    if user.is_authenticated:
        print(id)
        appointment = Appointment.objects.get(id = id, user = user)
        print(appointment.date, appointment.appointment_time)
        payload = {
                "firstname": appointment.user.first_name,
                "lastname": appointment.user.last_name,
                "service": appointment.ailment_id.title,
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
    if request.method == "POST":
        form = WriteUsForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Form Submitted Successfully")     
            return redirect('faq')   
        else:
            WriteUsForm()
            messages.success(request, "You need to fill the form")     
            return redirect('faq') 
    return render(request, 'view/faq.html')

def private_policy(request):
    return render(request, 'view/private_policy.html')

def t_and_c(request):
    return render(request, 'view/t_and_c.html')

