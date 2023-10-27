from django.shortcuts import render,HttpResponse

# Create your views here.
def gallery(request):
    return HttpResponse("<h1>View Gallery Here</h1>")
# Create your views here.
def offers(request):
    return HttpResponse("<h1>latest offers</h1>")
def contact(request):
    return HttpResponse("<h1>phone number/h1>")
def payments(request):
    return HttpResponse("<h1>payment portal/h1>")