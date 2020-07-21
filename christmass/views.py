from django.http import HttpResponse
import datetime

from django.shortcuts import render

# Create your views here.
def index1(request):
    now = datetime.datetime.now()
    return render(request, 'christmass/index.html', {
        "christmass": now.date == 25 and now.month == 12
    })