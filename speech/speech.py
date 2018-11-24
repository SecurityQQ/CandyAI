from google.cloud import texttospeech
import os
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file("C:/Users/dyako/Downloads/moscowhack-c25932a920be.json")

scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/cloud-platform'])

# Instantiates a client
client = texttospeech.TextToSpeechClient(credentials=credentials)

def playsound(text, name):
	# Set the text input to be synthesized
	synthesis_input = texttospeech.types.SynthesisInput(text=text)

	# Build the voice request, select the language code ("en-US") and the ssml
	# voice gender ("neutral")
	voice = texttospeech.types.VoiceSelectionParams(
	    language_code='en-US',
	    name=name)

	# Select the type of audio file you want returned
	audio_config = texttospeech.types.AudioConfig(
	    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

	# Perform the text-to-speech request on the text input with the selected
	# voice parameters and audio file type
	response = client.synthesize_speech(synthesis_input, voice, audio_config)

	# The response's audio_content is binary.
	with open('output.mp3', 'wb') as out:
	    # Write the response to the output file.
	    out.write(response.audio_content)
	    print('Audio content written to file "output.mp3"')



	from pydub import AudioSegment

	sound = AudioSegment.from_mp3("output.mp3")
	sound.export("output.wav", format="wav")


	import winsound
	winsound.PlaySound('output.wav', winsound.SND_ALIAS)


def greeting(age, gender):

	if (age<14 and gender=='male'):
		playsound('Hello Little Boy, do you want some kandies?', 'en-US-Wavenet-F')
	elif (age<14 and gender=='female'):
		playsound('Hello Little Girl, do you want some kandies?', 'en-US-Wavenet-F')
	elif (age<30 and gender=='male'):
		playsound('Hi guy, if you brave enough try your lack try your luck', 'en-US-Wavenet-E')
	elif (age<30 and gender=='female'):
		playsound('Hi girl, you is as sweet as my candies, I have a personal present for you', "en-US-Wavenet-B")
	elif (age>30 and gender=='male'):
		playsound('Welcome men, we have a special offer for you', 'en-US-Wavenet-A')
	else:
		playsound('Welcome lady, do you want to get a special offer?', 'en-US-Wavenet-A')


greeting(5, 'female')