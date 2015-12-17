from django.views import generic


class IndexView(generic.ListView):
    template_name = 'send_sms/index.html'

    def get_queryset(self):
        return
