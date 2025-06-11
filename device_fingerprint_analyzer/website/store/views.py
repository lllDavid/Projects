from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def show_headers(request):
    headers = request.headers  
    output = "\n".join(f"{key}: {value}" for key, value in headers.items())
    print("Request headers:\n" + output)  

    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    print(ip)

    return HttpResponse("Headers printed to server log.")
