# -*- coding: utf-8 -*-

import os
import glob
import random


def playSongs():
    location = '/home/pi/Music'
    os.chdir(location)

    max = 2
    played = 0
    songs = glob.glob('*.mp3')
    for x in range(0,max):
        if played == max:
            break
        s = random.randint(1,24) % len(songs)
        print 'song to play: ' + songs[s]
        play_mpg321(songs[s])
        played += 1

def play_mpg321(song):
    os.system('mpg321 ' + song)


if __name__    == "__main__":
   playSongs()
    

