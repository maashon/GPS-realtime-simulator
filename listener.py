#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 02:21:10 2021

@author: pi
"""
import sys
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
def sendAck(carID,ClientID,responce):
    accTopic="/cmd/car_client_ack/"+ClientID
    accData={"car_id":carID,"is_accepted":responce}
    fb = db.reference(accTopic)
    fb.child(get_now_timestamp()).set(accData)
    
def sendAv(carID,availability):
    avTopic="/car_availability/"+carID
    fb = db.reference(avTopic)
    fb.child(get_now_timestamp()).set(True)
    
    
def listener(event):
    D=event.data
    try:
        client_id=D.get("client_id")
        msg="The client "+client_id+" requested the car. enter 1 to accept and 0 to deny:"
        responce=input(msg)
        if responce=="1":
            sendAck(carId,client_id,True)
            sendAv(carId,False)
        else:
            sendAck(carId,client_id,False)
    except:
        return
    
    
FIREBASE_CERTIFICATE_PATH = 'key.json'
cred_obj = firebase_admin.credentials.Certificate(FIREBASE_CERTIFICATE_PATH)
obj = firebase_admin.initialize_app(cred_obj, {
    "databaseURL": "https://embeddedtesting-default-rtdb.firebaseio.com"
})

#ref = db.reference("/car_location/1")


ref="/cmd/client_car_request/"+carId
db.reference(ref,app=obj).listen(listener)
