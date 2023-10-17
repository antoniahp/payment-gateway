from app.payments.providers.bank_card import BankCard
from app.payments.providers.bizum import Bizum
from app.payments.providers.payment_method_provider import PaymentMethodProvider
from app.payments.providers.paypal import PayPal


class PaymentMethodSelector:
    def select(self, payment_method_name: str, payment_method_data: dict) -> PaymentMethodProvider:
        if payment_method_name == "bizum":
            return Bizum(**payment_method_data)

        if payment_method_name == "paypal":
            return PayPal(**payment_method_data)

        if payment_method_name == "bank_card":
            return BankCard(**payment_method_data)

        raise Exception(f"Payment method not supported: {payment_method_name}")