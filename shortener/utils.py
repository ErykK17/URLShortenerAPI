import string 
import random

def generate_short_url(length=7):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))