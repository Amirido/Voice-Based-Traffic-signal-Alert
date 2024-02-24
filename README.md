# Voice-Based-Traffic-signal-Alert
This is a python script to provide a voice alert to a driver about upcoming traffic signal using OSM data. Used requests, geopy,  gTTS and geocoder libraries.
This script uses geolocation and text-to-speech functionality to inform drivers about upcoming signals within a certain radius, includes functions for fetching traffic signal data, calculating distances, and generating alerts.
I have used Overpass API to get the data for Traffic Signals, so by querying the Overpass API, the script retrieves information about traffic signals located within a 5000-meter radius of the users current location.
(You have to put your current location manually in the form of latitude and longitude, I tried adding a function to get mt current location automatically but couldn't do it, so I just decided to go with the manual entry of current locstion's latitude and longitude.)
 The script uses the geodesic function from the geopy.distance module that  calculates the distance between two geographical coordinates, allowing the script to identify traffic signals that are within a predefined distance threshold (in this case, 200 meters) from the current location.
 Upon detecting a nearby signal the script generates audio alerts using the gTTS (Google Text-to-Speech) library , saves them as mp3 files and then the alerts are played to the driver using the os.system function.
 In the absence of nearby signals, the script also generates an alert to inform of the lack of traffic signals in the vicinity.

