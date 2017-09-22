#!/bin/env/python

class SMSPriv(object) :

    def __init__(self):
        self.site = 'http://sms.priv.pl/'

    def send_sms(self, receiver_phone_number, sender_name, sms_content):
        """
        :param receiver_phone_number:
        :param sender_name:
        :param sms_content:
        :return:
        """
