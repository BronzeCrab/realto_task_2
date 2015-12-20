from django.conf import settings
from importlib import import_module
from django.utils.module_loading import import_string


class Send(object):

    def __init__(self, key):
        self.key = key
        try:
            self.backend = settings.SMS_TRANSPORTS[self.key]['BACKEND']
        except KeyError:
            print """please check settings: if default
                     field exists and has all necessary fields"""
        try:
            self.params = settings.SMS_TRANSPORTS[self.key]['PARAMS']
        except:
            self.params = dict()

    def send(self, phone, msg):
        try:
            SmsTransport = import_string(self.backend)
        except ImportError:
            print 'please, check settings!'
        else:
            sms_tr = SmsTransport(phone, msg, **self.params)
            sms_tr.print_phone_msg()

if settings.SMS_TRANSPORTS:
    sms_transports = dict()
    for key in settings.SMS_TRANSPORTS.keys():
        if key == 'default':
            sms_transports[key] = import_module('libsms.sms_transport')
        else:
            send = Send(key)
            sms_transports[key] = send
else:
    print 'please, check settings'
