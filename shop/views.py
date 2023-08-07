from django.shortcuts import render, redirect


def home_page(request):
    return render(request, 'pages/index.html')


def contact(request):
    return render(request, 'pages/contact.html')

def shop(request):
    return render(request, 'pages/shop.html')

def testimonial(request):
    return render(request, 'pages/testimonial.html')

def why(request):
    return render(request, 'pages/why.html')