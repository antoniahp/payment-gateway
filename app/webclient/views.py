from django.contrib.sites import requests
from django.shortcuts import render
from payments.providers import bank_card


def create_payment(request):
#    query_params = {}
#     if request.method =='POST':
#         payment_method_name = request.POST.get("bank_card") #payment_method_name
#         if payment_method_name == "bank_card":
#             query_params["bank_card"] = bank_card

#     response = requests.get(url="http://localhost:8000/api/core/bank_card", params=query_params) #payment_method_data
#     response.raise_for_status()
#     bank_card_response = response.json(["bank_card"])
    context = {
        #         "bank_card": bank_card_response
    }
    return render(request, "create_payment.html", context)
