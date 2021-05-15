
"""
Created on Mon May 10 20:01:15 2021

@author: pi
"""
import sys
from firebase import firebase
from datetime import datetime

fb = firebase.FirebaseApplication('https://gps-test-d73fb-default-rtdb.europe-west1.firebasedatabase.app/', None)

carID=sys.argv[1]
topic="car_location/"+carID
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
data={datetime.now().strftime("%Y%m%d%H%M%S"):{"lat":lat ,"long":longt}}
fb.post(topic,data)

