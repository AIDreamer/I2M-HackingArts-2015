# file = "output.mid"
from midiutil.MidiFile3 import MIDIFile
import pygame
freq = 44100
bitsize = -16
channels = 2
buffer = 1024
pygame.mixer.init(freq, bitsize, channels, buffer)
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    clock.tick(30)