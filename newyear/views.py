from django.http import HttpResponse
from . import views
import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, 'newyear/index.html', {
        'newyear': now.date == 1 and now.month ==1
    })