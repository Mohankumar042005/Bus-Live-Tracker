import firebase_admin
from firebase_admin import credentials, db
import time

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bus-tracker-b1516-default-rtdb.firebaseio.com/'
})

# Dummy live location updates
locations = [
    {"lat": 12.9716, "lon": 77.5946},
    {"lat": 12.9720, "lon": 77.5950},
    {"lat": 12.9725, "lon": 77.5955}
]

for loc in locations:
    ref = db.reference("buses/bus1")  # ✅ Note the "buses" parent
    ref.set({
        "from": "koyambedu",
        "to": "tambaram",
        "latitude": loc["lat"],
        "longitude": loc["lon"]
    })
    print("✅ Updated location:", loc)
    time.sleep(5)
