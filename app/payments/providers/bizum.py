from app.payments.providers.payment_method_provider import PaymentMethodProvider


class Bizum(PaymentMethodProvider):
    def __init__(self, phone_number:int):
        self.phone_number = phone_number

    def pay(self, total: float):
        print(f"Realizando pago de {total} con el telefono {self.phone_number}")