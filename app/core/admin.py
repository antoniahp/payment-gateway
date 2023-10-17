from django.contrib import admin

from .models import PaymentMethodDataBankCardModel, PaymentMethodDataBizumModel, PaymentMethodDataPayPalModel

admin.site.register(PaymentMethodDataBankCardModel)
admin.site.register(PaymentMethodDataBizumModel)
admin.site.register(PaymentMethodDataPayPalModel)
