
"""
Created on Mon May 10 20:01:15 2021

@author: pi
"""
#import sys
#from firebase import firebase
import datetime
import calendar
import firebase_admin
from firebase_admin import db
clientList=[]
#https://embeddedtesting-default-rtdb.firebaseio.com/
def get_now_timestamp():
    current_datetime = datetime.datetime.utcnow()
    current_timetuple = current_datetime.utctimetuple()
    current_timestamp = calendar.timegm(current_timetuple)
    return str(current_timestamp)



def sendAck(carID,ClientID,responce):
    accTopic="/cmd/car_client_ack/"+ClientID
    #now = datetime.now()
    #current_time = now.strftime("%Y%m%d%H%M%S")
    #accData={get_now_timestamp():{"car_id":carID,"is_accepted":responce}}
    accData={"car_id":carID,"is_accepted":responce}
    fb = db.reference(accTopic)
    fb.child(get_now_timestamp()).set(accData)
    
def sendAv(carID,availability):
    avTopic="/car_availability/"+carID
    #now = datetime.now()
    #current_time = now.strftime("%Y%m%d%H%M%S")
    #availabilityData={get_now_timestamp():availability} 
    fb = db.reference(avTopic)
    fb.child(get_now_timestamp()).set({True})
    #fb.push().set(availabilityData)
def listener(event):
    
    req=event.data
    for key,d in req.items():
        for index in d:
            clientId=d[index]
            clientList.append(clientId)
    msg="Car "+"has been requested by client "+clientId+"enter 1 to accept and 0 to deny"
    responce=input(msg)
    if responce=="1":
        sendAck(carId,clientId,True)
    else:
        sendAck(carId,clientId,False)
            
    
 
FIREBASE_CERTIFICATE_PATH = 'key.json'
cred_obj = firebase_admin.credentials.Certificate(FIREBASE_CERTIFICATE_PATH)
app = firebase_admin.initialize_app(cred_obj, {
    "databaseURL": "https://embeddedtesting-default-rtdb.firebaseio.com"
})
topic="/car_availability/"




ref=db.reference('stats/cars_id')
car_list=ref.get()
activeCarList= [str(int) for int in car_list]
availabilityList=[]

for i in range(len(activeCarList)):
    sendAv(activeCarList[i],True)
    ref="/cmd/client_car_request/"+activeCarList[i]
    db.reference(ref,app=app).listen(listener)
    
    
    
    

