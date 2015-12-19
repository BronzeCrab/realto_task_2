from django.conf import settings
from django.utils.module_loading import import_string

def send(**kargs):
    if settings.SMS_TRANSPORTS:
        test = import_string(settings.SMS_TRANSPORTS['default']['BACKEND'])
        print test
