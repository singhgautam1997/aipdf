import re
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'Aipdf/home.html',{'pdf': ['pdf1','pdf2']})