from django.contrib import admin

from .models import User, PaymentMethodData, PaymentIntent

admin.site.register(User)
admin.site.register(PaymentMethodData)
admin.site.register(PaymentIntent)
