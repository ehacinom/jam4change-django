from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def hello0(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)

def hello1(request):
    today = datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    paragraph = 'This is a test\nof newlines.'
    var = {"today" : today, "days_of_week" : daysOfWeek, "paragraph": paragraph}
    return render(request, "hello1.html", var)

def hello2(request, number):
    text = "<h1>welcome to my app number %s!</h1>"% number
    return HttpResponse(text)

def hello3(request, month, year):
    return HttpResponse('month {}, year {}'.format(month, year))

    

