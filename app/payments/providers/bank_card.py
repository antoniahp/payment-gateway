from app.payments.providers.payment_method_provider import PaymentMethodProvider


class BankCard(PaymentMethodProvider):
    def __init__(self, card_number: int, cvc: int, date_of_expire: str):
        self.card_number = card_number
        self.cvc = cvc
        self.date_of_expire = date_of_expire

    def pay(self, total: float):
        print(f"Realizando el pago de {total} ")