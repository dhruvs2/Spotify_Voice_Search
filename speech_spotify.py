import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data

import speech_recognition as sr
import webbrowser

# Converting Speech to Text
def Text():
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		print("Say Something...")

		audio = r.listen(source)
		
		try:
			text = r.recognize_google(audio)
			return text
		except Exception as e:
			error = "Error"
			return error


client_id = 'f51a0e90f3284eddbc69dc411c015441'
client_secret = '935f531abb8b45a2a611205736b38211'

client_credentials_manager = SpotifyClientCredentials(client_id = client_id,client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

find = Text()
name = "{" + find + "}"

result = sp.search(name) #search query: Lists within Lists
print(result['tracks']['items'][0]['artists'])
print(result['tracks']['items'][0]['artists'][0]['external_urls']['spotify'])
re = result['tracks']['items'][0]['artists'][0]['external_urls']['spotify']
webbrowser.open_new(re)

