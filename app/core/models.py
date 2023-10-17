from django.db import models


class PaymentMethodDataBankCardModel(models.Model):
    card_number = models.IntegerField()
    cvc = models.IntegerField()
    date_of_expire = models.DateField()

    def __str__(self) -> str:
        return f"{self.id}"

class PaymentMethodDataBizumModel(models.Model):
    phone_number = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id}"

class PaymentMethodDataPayPalModel(models.Model):
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.id}"