# Script to read audio files from a folder and then choose one at random to play upon signal

from os import walk
from os import system
from random import choice

audio = [] # List of audio file names from the audio directory
for (dirpath, dirnames, filenames) in walk('./Audio/'): # Read in names from the directory and populate the list
    audio.extend(filenames) # Populating the list
    break # Only need top level names for now

system("aplay ./Audio/"+choice(audio))


# Need an auto 
