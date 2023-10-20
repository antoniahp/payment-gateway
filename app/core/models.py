from django.db import models
from datetime import datetime
from django.db.models import JSONField


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    dni = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=15)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.id}"

class PaymentMethodNameChoices(models.TextChoices):
    BIZUM = "BIZUM"
    PAYPAL = "PAYPAL"
    BANK_CARD = "BANK_CARD"

class PaymentMethodData(models.Model):
    number_card = models.CharField(max_length=30)
    cvc = models.CharField(max_length=5)
    expiration_date = models.CharField(max_length=15)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    def __str__(self) -> str:
        return f"{self.id}"




class PaymentIntent(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="payment_intents")
    payment_method_name = models.CharField(max_length=10, choices=PaymentMethodNameChoices.choices)
    payment_method_data = JSONField("PaymentMethodData", default=dict)
    created_at = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.id}"

    #class Answer(models.IntegerChoices):
    #    NO = 0, _("No")
      #  YES = 1, _("Yes")

    #    __empty__ = _("(Unknown)")