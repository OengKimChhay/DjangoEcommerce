from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'manage_store/dansboard.html')


# ----------------------------------- Product -------------------------------------
def create_product(request):
    return HttpResponse('hello')
