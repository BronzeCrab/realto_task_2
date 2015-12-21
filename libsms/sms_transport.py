from django.conf import settings
from django.utils.module_loading import import_string

default_transport = import_string(
    settings.SMS_TRANSPORTS['default']['BACKEND'])

default_params = settings.SMS_TRANSPORTS['default']['PARAMS']


def send(phone, msg, tr=default_transport, params=default_params):
        sms_tr = tr(phone, msg, **params)
        sms_tr.print_phone_msg()
