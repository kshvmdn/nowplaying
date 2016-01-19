#!/usr/bin/env python

from termcolor import colored
from appscript import *
from track import Track


def main():
    print(get_song())


def get_song():
    itunes_open = bool(app('System Events').processes[its.name == 'iTunes'].count())
    if itunes_open:  # check if application open
        itunes = app('iTunes')
        if itunes.player_state.get() == k.playing:  # check if song playing
            track = Track(itunes.current_track.get())
            return track
        return colored('No song currently playing.', 'red')
    return colored('iTunes not open.', 'red')

if __name__ == '__main__':
    main()
