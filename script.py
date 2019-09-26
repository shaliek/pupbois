# Script to read audio files from a folder and then choose one at random to play upon signal

from os import walk
from os import system
from random import choice
import RPi.GPIO as GPIO
from time import sleep

# GPIO INSTANTIATION
GPIO.setmode(GPIO.BCM)
MAGNET_GPIO = 17
GPIO.setup(MAGNET_GPIO, GPIO.IN) # GPIO Assign mode
###

ready_to_play = True # Bool flag

audio = [] # List of audio file names from the audio directory
for (dirpath, dirnames, filenames) in walk('./Audio/'): # Read in names from the directory and populate the list
    audio.extend(filenames) # Populating the list
    break # Only need top level names for now

# Callback
def choose_play(pin):
    if ready_to_play:
        system("aplay ./Audio/"+choice(audio))
        ready_to_play = False

def ready_flag(pin):
   ready_to_play = True
        
# Listener
GPIO.add_event_detect(MAGNET_GPIO, GPIO.FALLING, callback=choose_play, bouncetime=200)
GPIO.add_event_detect(MAGNET_GPIO, GPIO.RISING, callback=)

while True:
    print(MAGNET_GPIO)
    sleep(1)
