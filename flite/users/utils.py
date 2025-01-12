import uuid, random
from flite.users import models

def generate_new_user_passcode():
    """
    Returns a unique passcode
    """
    def _passcode():
        return str(uuid.uuid4().int)[0:6]
    passcode = _passcode()
    while models.NewUserPhoneVerification.objects.filter(referral_code=passcode).exists():
        passcode = _passcode()
    return passcode


def send_mobile_signup_sms(phone_number, email):

    status=False
    user_passcode = generate_new_user_passcode()
    
    try:
        attempted_verification_obj = models.NewUserPhoneVerification.objects.get(phone_number=phone_number)
    except models.NewUserPhoneVerification.DoesNotExist:
        attempted_verification_obj = None

    if attempted_verification_obj:
        attempted_verification_obj.verification_code = user_passcode
        attempted_verification_obj.email = email
        attempted_verification_obj.is_verified = False
        attempted_verification_obj.save()
    else:
        attempted_verification_obj = models.NewUserPhoneVerification(phone_number=str(phone_number), verification_code=user_passcode,
            is_verified=False, email=email)
        attempted_verification_obj.save()    
    #tasks.send_sms_verification_code.delay(phone_number, user_passcode)
    status = True
    return attempted_verification_obj, user_passcode


def validate_mobile_signup_sms(phone_number, code):

    try:
        new_user_code_obj  = models.NewUserPhoneVerification.objects.get(phone_number=phone_number, verification_code=code)
    except models.NewUserPhoneVerification.DoesNotExist:
        new_user_code_obj = None

    if new_user_code_obj:
        if new_user_code_obj.is_verified:
            return 0, "Code has been verified"
        else:
            new_user_code_obj.is_verified = True
            new_user_code_obj.save()
            return 1, "Code verified"
    return 0, "The code provided is invalid. Kindly check and try again."


def generate_transaction_reference():
    """
    Returns a unique transaction id
    """
    def _transaction_ref():
        return str(random.randint(100000000000, 999999999999))
    ref_number = _transaction_ref()
    while models.Transaction.objects.filter(reference=ref_number).exists():
        ref_number = _transaction_ref()
    return ref_number


# def generate_account_number():
#     """
#     Returns an account number
#     """
#     def _account_number():
#         return str(random.randint(1000000000, 9999999999))
#     wallet_number = _account_number()
#     while models.Account.objects.filter(wallet_number=wallet_number).exists():
#         wallet_number = _account_number()
#     return wallet_number