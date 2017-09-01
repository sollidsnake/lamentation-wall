from django.http.request import HttpRequest
from lamentation_wall.settings import RECAPTCHA_PRIVATE_KEY
import requests


def is_valid(request: HttpRequest):
    payload = {'secret': RECAPTCHA_PRIVATE_KEY,
               'response': request.POST.get('g-recaptcha-response')}

    return requests.post('https://www.google.com/recaptcha/api/siteverify', payload)\
                   .json().get('success', False)

