#!/usr/bin/env python3

import sys
from appscript import *
from termcolor import colored


def open_(itunes):
    return itunes.activate()


def close(itunes):
    return itunes.quit()


def is_playing(itunes):
    return itunes.player_state.get() == k.playing


def now_playing(itunes):
    if not is_playing(itunes):
        print('No song playing, starting now...')
        return play(itunes)
    track = itunes.current_track.get()
    return print('{} - {}\n{}'.format(colored(track.name(), attrs=['bold']),
                                      track.artist(),
                                      track.album()))


def play(itunes):
    if is_playing(itunes):
        return play_next(itunes)
    itunes.play()
    return now_playing(itunes)


def pause(itunes):
    if is_playing(itunes):
        return itunes.pause()


def stop(itunes):
    return itunes.stop()


def play_next(itunes):
    if not is_playing(itunes):
        return play(itunes)
    itunes.next_track()
    return now_playing(itunes)


def play_previous(itunes):
    if not is_playing(itunes):
        return play(itunes)
    itunes.previous_track()
    return now_playing(itunes)


def main():
    cmd = None

    is_open = app('System Events').processes[its.name == 'iTunes'].count() == 1
    itunes = app('iTunes')

    if not is_open:
        print('iTunes not open, opening now...')
        open_(itunes)

    cmds = {
        'np': now_playing,
        'next': play_next,
        'prev': play_previous,
        'play': play,
        'pause': pause,
        'show': open_,
        'stop': stop,
        'close': close
    }
    cmd = cmds[cmd] if cmd in cmds else now_playing
    return cmd(itunes)

if __name__ == '__main__':
    main()
