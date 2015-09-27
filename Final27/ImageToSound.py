__author__ = 'khainguyen'
import ArrayProcessing
import ImageToArray
import pygame
from cs5png import *
from midiutil.MidiFile3 import MIDIFile
from random import *
from threading import  _Timer
import os
import subprocess
from timeit import default_timer as timer


def imageToArray(imageArray,x,y):

    imageArray = ArrayProcessing.arrayBigToSmall(imageArray,x,y)
    imageArray = ArrayProcessing.roundToList(imageArray)
    theSum = 0
    noteArray = []
    for row in range(len(imageArray)):
        theSum = 0
        for column in range(len(imageArray[row])):
            for x in range(0,3):
                theSum += imageArray[row][column][x]
        theSum = theSum %(88) + 21
        noteArray.append(theSum)
    return noteArray

def arrayToMidi(aArray,count):
    MyMIDI = MIDIFile(1)
    MyMIDI.addTrackName(0,0,"Red")
    MyMIDI.addTempo(0,0,120)
    time = 0
    for i in range(100):
        for j in range(len(aArray)):
            # randDur = choice([0.5, 0.25, 1, 2, 4])
            randDur = 1
            pitch = aArray[j]
            MyMIDI.addNote(0,0,pitch,time,randDur,100)
            time += randDur
    name = str(count) + ".mid"
    print(name)
    binfile = open(name, 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()
    print("finishing producing midi")
    return (name)

def arrayToMidiMotion(aArray, count):
    MyMIDI = MIDIFile(1)
    MyMIDI.addTrackName(0,0,"Red")
    MyMIDI.addTempo(0,0,120)
    time = 0
    for j in range(len(aArray)):
        # randDur = choice([0.5, 0.25, 1, 2, 4])
        randDur = 0.25
        pitch = aArray[j]
        MyMIDI.addNote(0,0,pitch,time,randDur,100)
        time += randDur
    name = str(count) + ".mid"
    print(name)
    binfile = open(name, 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()
    print("finishing producing midi")
    return (name)

def arrayToMidiDouble(aArray, count):
    MyMIDI = MIDIFile(1)
    MyMIDI.addTrackName(0,0,"Red")
    MyMIDI.addTempo(0,0,120)
    time = 0
    for j in range(len(aArray)):
        # randDur = choice([0.5, 0.25, 1, 2, 4])
        randDur = 1
        pitch = aArray[j]
        MyMIDI.addNote(0,0,pitch,time,randDur,100)
        time += randDur
    name = str(count) + ".mid"
    print(name)
    binfile = open(name, 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()
    print("finishing producing midi")
    return (name)

global processList
processList = [0] * 10000

def run(imageArray,x,y,count,type):

    currentDirectory=(os.getcwd())
    f=open('midiTemp.py','r')
    code=f.read()
    f.close()

    if (type == 1): midiToRun = arrayToMidi(imageToArray(imageArray,x,y),count)
    elif (type == 2): midiToRun = arrayToMidiMotion(imageToArray(imageArray,x,y),count)
    elif (type == 3): midiToRun = arrayToMidiDouble(imageToArray(imageArray,x,y),count)

    name = str(count) + '.py'
    CODE = "file = " + "\"" + midiToRun + "\"" + code
    f=open(name,'w')
    f.write(CODE)
    f.close()
    PythontoRun='python '+ currentDirectory + "\\" + name
    processList[count]=subprocess.Popen(PythontoRun)
    start = timer()

def kill(count):
    processList[count].kill()