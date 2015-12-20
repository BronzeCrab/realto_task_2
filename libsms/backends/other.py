class SmsTransport(object):

    def __init__(self, phone, msg, **params):
        self.params = dict()
        self.params.update(params)
        self.phone = phone
        self.msg = msg

    def print_phone_msg(self):
        print 'phone %s' % self.phone
        print 'msg %s' % self.msg
