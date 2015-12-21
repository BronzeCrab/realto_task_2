from django.conf import settings
from importlib import import_module
from django.utils.module_loading import import_string


class Send(object):

    def __init__(self, key):
        self.key = key
        try:
            self.backend = settings.SMS_TRANSPORTS[self.key]['BACKEND']
            self.transport = import_string(self.backend)
        except (KeyError, ImportError):
            pass
        try:
            self.params = settings.SMS_TRANSPORTS[self.key]['PARAMS']
        except:
            self.params = dict()

    def send(self, phone, msg):
        if hasattr(self, 'transport'):
            sms_tr = self.transport(phone, msg, **self.params)
            sms_tr.print_phone_msg()
        else:
            print 'error'

if settings.SMS_TRANSPORTS:
    sms_transports = dict()
    for key in settings.SMS_TRANSPORTS.keys():
        if key == 'default':
            sms_transports[key] = import_module('libsms.sms_transport')
        else:
            sms_transports[key] = Send(key)
else:
    print 'please, check settings'