from django.contrib.sites import requests
from django.shortcuts import render



def checkout(request):

    context = {

    }
    return render(request, "checkout.html", context)


def bizum(request):

    context = {

    }
    return render(request, "bizum.html", context)
