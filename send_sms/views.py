from django.views import generic
from libsms import sms_transport


class IndexView(generic.ListView):
    template_name = 'send_sms/index.html'
    sms_transport()

    def get_queryset(self):
        return
