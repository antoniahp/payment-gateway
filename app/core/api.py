from datetime import date

from ninja import Router, Schema, FilterSchema, Query
from core.models import PaymentMethodDataBankCardModel

core_router = Router()

class BankCardFilterSchema(FilterSchema):
    card_number: int
    cvc: int
    date_of_expire: date

@core_router.get("/bank_card")
def get_bank_card(request, filters: BankCardFilterSchema = Query(...)):
    filtered_payments = filters.filter(
        PaymentMethodDataBankCardModel.objects.all()
    )
    payments = []
    for pay in filtered_payments:
        payments.append({
            "card_number": pay.card_number,
            "cvc": pay.cvc,
            "date_of_expire": pay.date_of_expire
        })
    return{"payments": payments}
