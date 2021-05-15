
"""
Created on Mon May 10 20:01:15 2021

@author: pi
"""
#import sys
from firebase import firebase
from datetime import datetime


topic="car_availability/"
fb = firebase.FirebaseApplication('https://gps-test-d73fb-default-rtdb.europe-west1.firebasedatabase.app/', None)
activeCarList=[]
while True:
    carId=input("Enter the car Id you want to set active or type -1 to break: ")
    if carId=="-1":
        break;
    activeCarList.append(carId)
availabilityList=[]
 
for i in range(len(activeCarList)):
    
    now = datetime.now()
    current_time = now.strftime("%Y%m%d%H%M%S")
    availability={activeCarList[i]:True} 
    availabilityList.append(availability)
    carTopic=topic+activeCarList[i]
    data={current_time:True}
    fb.post(carTopic,data)
def sendAcc(carID,responce):
    accTopic="cmd/car_client_ack/"+carID
    now = datetime.now()
    current_time = now.strftime("%Y%m%d%H%M%S")
    accData={current_time:{"car_id":carID,"is_accepted":responce}}
    fb.post(accTopic,accData)
    
def sendAv(carID,availability):
    avTopic=topic+carID
    now = datetime.now()
    current_time = now.strftime("%Y%m%d%H%M%S")
    availabilityData={current_time:availability} 
    fb.post(avTopic,availabilityData)

sendAcc("3",False)
sendAv("3",False)  

