import requests
from lamentation_wall.settings import RECAPTCHA_PRIVATE_KEY


def check_recaptcha(request):
    payload = {'secret': RECAPTCHA_PRIVATE_KEY, 'response': request.POST.get('g-recaptcha-response')}
    return requests.post('https://www.google.com/recaptcha/api/siteverify', payload)\
                   .json().get('success', False)
