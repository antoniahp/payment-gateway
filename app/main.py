from app.payments.payments_method_selector import PaymentMethodSelector

payment_method_name = "bank_card"
payment_method_data = {
    "card_number": 1234567812345678,
    "cvc": 987,
    "date_of_expire": "07/32"
}

payment_method_selector = PaymentMethodSelector()

payment_method = payment_method_selector.select(payment_method_name=payment_method_name, payment_method_data=payment_method_data)

payment_method.pay(39.02)