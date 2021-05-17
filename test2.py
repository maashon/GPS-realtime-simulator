"""
from firebase import firebase

fb = firebase.FirebaseApplication('https://gps-test-d73fb-default-rtdb.europe-west1.firebasedatabase.app/', None)

data={"name": "parsa","dSize":15}
fb.post("/info",data)
print("data was sent to the database")
"""

import firebase_admin
from firebase_admin import db
import time

import datetime
import calendar
def get_now_timestamp():
    current_datetime = datetime.datetime.utcnow()
    current_timetuple = current_datetime.utctimetuple()
    current_timestamp = calendar.timegm(current_timetuple)
    return str(current_timestamp)

FIREBASE_CERTIFICATE_PATH = 'key.json'
cred_obj = firebase_admin.credentials.Certificate(FIREBASE_CERTIFICATE_PATH)
app = firebase_admin.initialize_app(cred_obj, {
    "databaseURL": "https://embeddedtesting-default-rtdb.firebaseio.com"
})

ref1 = db.reference("/cmd/client_car_request/1")
data1={"client_id":"85"}
D=ref1.get()
for id, info in D.items():
    for key in info:
        val=info[key]
print(val)    
    

