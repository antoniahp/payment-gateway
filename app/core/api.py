from datetime import date

from ninja import Router, Schema, Query
from core.models import User, PaymentIntent
from payments.providers.bank_card import BankCard
from payments.providers.bizum import Bizum
from payments.providers.payment_method_provider import PaymentMethodProvider
from payments.providers.paypal import PayPal

core_router = Router()


class UserSchema(Schema):
    id: int
    name: str
    surname: str
    dni: str
    address: str
    postal_code: str
    phone_number: int
    email: str


class CreatePayment(Schema):
    user: UserSchema
    payment_method_name: str
    payment_method_data: dict


class BizumData(Schema):
    phone_number: str


class PaypalData(Schema):
    email: str


class BankCardData(Schema):
    card_number: str
    cvc: int
    expiration_date: str


def validate_payment_method_data(payment_method_name: str, payment_method_data: dict):
    if payment_method_name == "bizum":
        BizumData(**payment_method_data)
    if payment_method_name == "paypal":
        PaypalData(**payment_method_data)
    if payment_method_name == "bank_card":
        BankCardData(**payment_method_data)


def verify_or_create_user(user_id: int, user_dni: str, user_name: str, user_surname: str, user_address: str,
                          user_postal_code: str, user_phone_number: int, user_email: str):
    try:
        User.objects.get(dni=user_dni)
    except User.DoesNotExist:
        user = User(
            dni=user_dni,
            id=user_id,
            name=user_name,
            surname=user_surname,
            address=user_address,
            postal_code=user_postal_code,
            phone_number=user_phone_number,
            email=user_email)

        user.save()


def save_request_in_database(user_id: int, payment_method_name: str, payment_method_data: dict):
    user = User.objects.get(id=user_id)
    PaymentIntent.objects.create(
        user=user,
        payment_method_name=payment_method_name,
        payment_method_data=payment_method_data
    )


def payment_method_select(payment_method_name: str, payment_method_data: dict) -> PaymentMethodProvider:
    if payment_method_name == "bizum":
        return Bizum(**payment_method_data)

    if payment_method_name == "paypal":
        return PayPal(**payment_method_data)

    if payment_method_name == "bank_card":
        return BankCard(**payment_method_data)




#@core_router.post("/pay")
def create_payment(request, data: CreatePayment):
    validate_payment_method_data(
        payment_method_name=data.payment_method_name,
        payment_method_data=data.payment_method_data
    )
    verify_or_create_user(
        user_dni=data.user.dni,
        user_id=data.user.id,
        user_name=data.user.name,
        user_surname=data.user.surname,
        user_address=data.user.address,
        user_postal_code=data.user.postal_code,
        user_phone_number=data.user.phone_number,
        user_email=data.user.email
    )
    save_request_in_database(
        user_id=data.user.id,
        payment_method_name=data.payment_method_name,
        payment_method_data=data.payment_method_data
    )
    payment_method_select(
        payment_method_name=data.payment_method_name,
        payment_method_data=data.payment_method_data
    )
