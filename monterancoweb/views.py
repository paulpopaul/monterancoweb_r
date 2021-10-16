
from django.conf import settings
from django.shortcuts import redirect, render
from django.template.loader import get_template

def index(request):
    return render(request,'index.html')  