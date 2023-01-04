from django.shortcuts import render

# Create your views here.

def food(request):
    return render(request,'specific.html')