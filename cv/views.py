from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'cv/index.html')


def simple(request):
    return render(request, 'cv/simple.html')


def data(request):
    return render(request, 'cv/data.html')


def fx(request):
    return render(request, 'cv/fx.html')


def patterns(request):
    return render(request, 'cv/patterns.html')
