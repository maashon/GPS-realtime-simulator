"""
from firebase import firebase

fb = firebase.FirebaseApplication('https://gps-test-d73fb-default-rtdb.europe-west1.firebasedatabase.app/', None)

data={"name": "parsa","dSize":15}
fb.post("/info",data)
print("data was sent to the database")

"""
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y%m%d%H%M%S")


