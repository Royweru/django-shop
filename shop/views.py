from django.shortcuts import render, redirect


def home_page(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def why(request):
    return render(request, 'why.html')