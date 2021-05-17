
"""
Created on Mon May 10 20:01:15 2021

@author: pi
"""
import sys
#from firebase import firebase
#from datetime import datetime
import datetime
import calendar
import firebase_admin
from firebase_admin import db
#https://embeddedtesting-default-rtdb.firebaseio.com/
#fb = firebase.FirebaseApplication('https://gps-test-d73fb-default-rtdb.europe-west1.firebasedatabase.app/',None)
FIREBASE_CERTIFICATE_PATH = 'key.json'
cred_obj = firebase_admin.credentials.Certificate(FIREBASE_CERTIFICATE_PATH)
app = firebase_admin.initialize_app(cred_obj, {
    "databaseURL": "https://embeddedtesting-default-rtdb.firebaseio.com"
})
carID=sys.argv[1]
topic="car_location/"+carID
fb = db.reference(topic)
lat=sys.argv[2]
longt=sys.argv[3][:-1]
#timeStamp=sys.argv[5]+sys.argv[6]+sys.argv[4]+" "+sys.argv[7];
#now = datetime.now()
#timeStamp = datetime.now().strftime("%Y%m%d%H%M%S")
#now = datetime.now()
#current_time = now.strftime("%H:%M:%S")
#current_time='"'+current_time+'"'
#data=current_time+': { "lat" : " ' +lat+' " , "long" : " ' +longt+ ' " } '
#data=timeStamp+': { lat : ' +lat+', long:' +longt+ '}'
def get_now_timestamp():
    current_datetime = datetime.datetime.utcnow()
    current_timetuple = current_datetime.utctimetuple()
    current_timestamp = calendar.timegm(current_timetuple)
    return str(current_timestamp)
#data={datetime.now().strftime("%Y%m%d%H%M%S"):{"lat":lat ,"long":longt}}
#data={get_now_timestamp():{"lat":lat ,"long":longt}}
#fb.push().set(data)

data={"lat":lat ,"long":longt}
fb.child(get_now_timestamp()).set(data)

