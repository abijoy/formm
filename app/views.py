from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def index(request):
    user = request.user
    if user.is_staff and user.username == 'mannan':
        return render(request, 'app/deptDashboard.html')
    if user.is_staff and user.username == 'provost':
        return render(request, 'app/hallDashboard.html')
    if user.is_staff and user.username == 'register':
        return render(request, 'app/adminDashboard.html')
    return render(request, 'app/dashboard.html')
    # return HttpResponse('hello world!')


def registration(request):
    return render(request, 'app/registration.html')
    # return HttpResponse('hello world!')
