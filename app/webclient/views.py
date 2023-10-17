from django.shortcuts import render
from core.models import PaymentMethodDataBankCardModel

def home(request):
    context = {

    }
    return render(request, "home.html", context)
