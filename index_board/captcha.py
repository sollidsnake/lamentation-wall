import requests


def check_recaptcha(request):
    payload = {'secret': 'YOU_SECRET_KEY', 'response': request.POST.get('g-recaptcha-response')}
    return requests.post('https://www.google.com/recaptcha/api/siteverify', payload)\
                   .json().get('success', False)
