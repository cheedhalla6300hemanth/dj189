from django.shortcuts import render,HttpResponse

# Create your views here.
def payments(request):
    return HttpResponse("<h1>select card ,upi,debit option</h1>")
def card(request):
    return HttpResponse("<h1>choose an option</h1>")
# Create your views here.
def debit(request):
    return HttpResponse("<h1>offers</h1>")
def UPI(request):
    return HttpResponse("<h1>number<python manage.py startapp artist/h1>")
