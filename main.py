#!/bin/env/python

from free_sms_handlers.pl.SMSPriv23102015 import SMSPriv23102015

if __name__ == "__main__":

    phone = SMSPriv23102015()
    phone.send_sms('607809000', 'Kasiulka', 'Hello!')
