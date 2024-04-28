from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def about_me(request):
    return render(request, "pages/about.html")
