import requests
from gtts import gTTS
import os
from geopy.distance import geodesic

# Function to fetch traffic signals from Open Street Map
def get_traffic_signals(latitude, longitude):
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""[out:json];node["highway"="traffic_signals"](around:5000,{latitude},{longitude});out;"""
    response = requests.get(overpass_url, params={'data': overpass_query})
    return response.json()

# Function to calculate distance between two points
def calculate_distance(current_location, destination):
    return geodesic(current_location, destination).meters

# Function to alert driver 
def alert_traffic_signals(current_location):
    traffic_signals = get_traffic_signals(current_location[0], current_location[1])

    nearby_signals = [signal for signal in traffic_signals.get("elements", [])           
            if calculate_distance(current_location, (signal["lat"], signal["lon"])) <= 200]
    
    if nearby_signals:
        distance_to_signal = int(calculate_distance(current_location, (nearby_signals[0]["lat"], nearby_signals[0]["lon"])))
        distance_message = f"The upcoming traffic signal is {distance_to_signal} meters away."
        tts = gTTS(text=distance_message, lang='en')
        tts.save("distance_alert.mp3")
        os.system("distance_alert.mp3")
        print("Upcoming Traffic Signal!")
    else:
        tts = gTTS(text="No traffic signals found in the vicinity.")
        tts.save("no_signal_alert.mp3")
        os.system("no_signal_alert.mp3")
        print("No traffic signals found in the vicinity.")

# Manual Entry for latitude and longitude
current_location = (12.906437219155096, 77.57406414123314)  

alert_traffic_signals(current_location)
