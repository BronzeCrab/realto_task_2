from django.views import generic
from libsms import sms_transport
from libsms import sms_transports


class IndexView(generic.ListView):
    template_name = 'send_sms/index.html'
    sms_transport.send(phone='123123', msg='qweqwe')
    sms_transports['default'].send(phone='1231234', msg='default')
    sms_transports['dummy'].send(phone='1231234', msg='dummy')
    sms_transports['other'].send(phone='1231234', msg='other')
    sms_transports['test_import_error'].send(phone='1231234', msg='qweqwea')

    def get_queryset(self):
        return
