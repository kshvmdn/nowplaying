from termcolor import colored

class Track:
    def __init__(self, track):
        self.track = track
        self.title = track.name.get()
        self.artist = track.artist.get()
        self.album = track.album.get()


    def __str__(self):
        return '{} - {}, {}'.format(colored(self.title, attrs=['bold']), 
                                    colored(self.artist, 'red'), 
                                    self.album)