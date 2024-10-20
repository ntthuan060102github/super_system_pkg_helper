import random

class InvalidOtpLenException(Exception):
    pass

def generate_otp_only_number(otp_len: int) -> str:
    if otp_len < 0 or otp_len > 10:
        raise InvalidOtpLenException("Invalid OTP length!")
    
    return str(random.randint(10**otp_len, 10**(otp_len + 1) - 1))