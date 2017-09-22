#!/bin/env/python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from free_sms_handlers.pl.SMSPriv import SMSPriv


class SMSPriv23102015(SMSPriv):
    def __init__(self):
        SMSPriv.__init__(self)

    def send_sms(self, receiver_phone_number, sender_name, sms_content):
        try:

            # prepare browser
            driver = webdriver.Firefox()
            driver.get(self.site)

            # select first 3 digits from number
            select = Select(driver.find_element_by_name('siec'))
            select.select_by_visible_text(receiver_phone_number[0:3])

            # set sender name
            from_input = driver.find_element_by_name('od')
            from_input.send_keys(sender_name)

            # set SMS content
            sms_text = driver.find_element_by_name('tresc')
            sms_text.send_keys(sms_content)

            # set remaining part of the number
            phone_number = driver.find_element_by_name('number2')
            phone_number.send_keys(receiver_phone_number[3:])

            # find the send sms button
            send_me = driver.find_elements(By.CLASS_NAME, 'btn')
            send_me[2].click()

            # close the browser
            driver.close()

        except Exception:
            pass