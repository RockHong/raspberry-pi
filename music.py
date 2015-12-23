# -*- coding: utf-8 -*-

import os
import glob
import random


def playSongs():
    location = '/home/pi/Music'
    os.chdir(location)

    max = 2
    songs = glob.glob('*.mp3')
    # shuffle
    size = len(songs)
    for x in range(0, size):
        pick = random.randint(x, size-1)
        (songs[x], songs[pick]) = (songs[pick], songs[x])

    for x in songs[:max]:
        print 'song to play: ' + x
        play_mpg321(x)

def play_mpg321(song):
    cmd = 'mpg321 "' + song + '"'
    print 'cmd to run: ' + cmd
    os.system(cmd)


if __name__    == "__main__":
   playSongs()


