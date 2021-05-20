#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 15:44:30 2021

@author: pi
"""
import datetime
import calendar
import firebase_admin
from firebase_admin import db
import sys

FIREBASE_CERTIFICATE_PATH = 'key.json'
cred_obj = firebase_admin.credentials.Certificate(FIREBASE_CERTIFICATE_PATH)
obj = firebase_admin.initialize_app(cred_obj, {
    "databaseURL": "https://embeddedtesting-default-rtdb.firebaseio.com"
})

def get_now_timestamp():
    current_datetime = datetime.datetime.utcnow()
    current_timetuple = current_datetime.utctimetuple()
    current_timestamp = calendar.timegm(current_timetuple)
    return str(current_timestamp)
def sendAv(carID,availability):
    avTopic="/car_availability/"+carID
    fb = db.reference(avTopic)
    fb.child(get_now_timestamp()).set(True)
carId=sys.argv[1]
sendAv(carId,True)
