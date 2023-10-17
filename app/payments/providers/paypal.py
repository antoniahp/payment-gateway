from app.payments.providers.payment_method_provider import PaymentMethodProvider


class PayPal(PaymentMethodProvider):
    def __init__(self, correo: str):
        self.correo = correo

    def pay(self, total:float):
        print(f"Realizando pago de {total}  con el correo {self.correo}")