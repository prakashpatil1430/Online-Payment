from django.shortcuts import render
from account.models import KYC, Account
from account.forms import KYCForm


def kyc_registration(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        kyc = KYC.objects.get(user=user)
    except:
        kyc = None

    pass



