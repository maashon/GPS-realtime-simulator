#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:30:22 2021

@author: pi
"""

import sys
#from firebase import firebase
#from datetime import datetime
import datetime
import calendar
import firebase_admin
from firebase_admin import db
carId=sys.argv[1]
def get_now_timestamp():
    current_datetime = datetime.datetime.utcnow()
    current_timetuple = current_datetime.utctimetuple()
    current_timestamp = calendar.timegm(current_timetuple)
    return str(current_timestamp)


FIREBASE_CERTIFICATE_PATH = 'key.json'
cred_obj = firebase_admin.credentials.Certificate(FIREBASE_CERTIFICATE_PATH)
obj = firebase_admin.initialize_app(cred_obj, {
    "databaseURL": "https://embeddedtesting-default-rtdb.firebaseio.com"
})

#ref = db.reference("/car_location/1")


ref="stats"
fb=db.reference(ref)


num_cars=fb.child("n_cars").get()
t=int(num_cars)
fb.child(str(t)).set(carId)
t=t+1
fb.child("n_cars").set(str(t))


