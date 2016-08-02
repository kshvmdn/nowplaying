#!/usr/bin/env python3
import sys

from appscript import *
from termcolor import colored


class iTunes():
    def __init__(self):
        self.itunes = app('iTunes')

        if not self.is_itunes_open():
            to_open = raw_input('iTunes not running, open now?')
            
            if to_open.lower() in ['0', 'false', 'n', 'nah', 'no', 'nope'] or not bool(to_open):
                return False
            
            self.open()

        self.function_map = {
            'close': self.close,
            'next': self.next,
            'np': self.now_playing,
            'open': self.open,
            'pause': self.pause,
            'play': self.play,
            'previous': self.previous,
            'show': self.open,
            'stop': self.stop
        }

    def is_itunes_open(self):
        return app('System Events').processes[its.name == 'iTunes'].count() == 1

    def open(self):
        return self.itunes.activate()

    def close(self):
        return self.itunes.quit()

    def is_song_playing(self):
        return self.itunes.player_state.get() == k.playing

    def now_playing(self):
        if not self.is_song_playing():
            print('No song playing.')

        track = self.itunes.current_track.get()

        name, artist, album = colored(track.name(), attrs=['bold']),\
            track.artist(), track.album()

        return print('%s - %s\n%s' % (name, artist, album))

    def play(self):
        if not self.is_itunes_open():
            self.open()

        if self.is_song_playing():
            return self.next()

        self.itunes.play()
        return self.now_playing()

    def pause(self):
        if not self.is_song_playing():
            return

        self.itunes.pause()

    def stop(self):
        return self.itunes.stop()

    def next(self):
        if not self.is_song_playing():
            return self.play()

        self.itunes.next_track()
        return self.now_playing()

    def previous(self):
        if not self.is_song_playing():
            return self.play()

        self.itunes.previous_track()
        return self.now_playing()


def exit(msg, err=False):
    print(msg)
    sys.exit(1 if err else 0)


def main(args):
    itunes = iTunes()
    
    if not itunes:
        exit('iTunes must be running!')

    arg = args[1] if len(args) >= 2 else None

    if not arg:
        exit('Expected argument. Run `-h` for help.', True)
        
    if arg == '--help' or arg == '-h':
        with open('./help.txt', 'r') as f:
            exit('\n%s' % f.read())
            
    if arg not in itunes.function_map:
        exit('Invalid command `%s`.' % arg, True)

    itunes.function_map[arg]()

if __name__ == '__main__':
    main(sys.argv)
