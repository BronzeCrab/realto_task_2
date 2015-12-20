from django.conf import settings
from django.utils.module_loading import import_string


def send(phone, msg):
    if settings.SMS_TRANSPORTS:
        try:
            SmsTransport = import_string(
                settings.SMS_TRANSPORTS['default']['BACKEND'])
            params = settings.SMS_TRANSPORTS['default']['PARAMS']
        except KeyError:
            print """please check settings: if default
                     field exists and has all necessary fields"""
        sms_tr = SmsTransport(phone, msg, **params)
        sms_tr.print_phone_msg()
    else:
        print 'please, check settings'
