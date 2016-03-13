# NowPlaying
Python command line tool to control iTunes playback and see what song is currently playing **(OS X only)**.


#### Usage

Requirements: Python 3.

+ Clone project 
   
    ```
    git clone http://github.com/kshvmdn/nowplaying && cd nowplaying
    ```

+ Install requirements
    
    ```
    pip install -r requirements.txt
    ```

+ Run `main.py` to see current song.

    ```
    $ python main.py
    Can't Tell Me Nothing - Kanye West
    Graduation (Deluxe Edition)
    ```

+ Commands:

    + now playing: `main.py` (also can be used to open iTunes & play song if iTunes is not open)
    + play: `main.py play`
    + pause: `main.py pause`
    + stop: `main.py stop`
    + play next: `main.py next`
    + play previous: `main.py prev`
    + close: `main.py close`

+ _Optional_ step: create aliases in `.bashrc` to run without the `python main.py`.

    + `nowplaying="python /path/to/main.py"`
    + `playsong="python /path/to/main.py play"`
    + `next="python /path/to/main.py next"`

#### Contribute

Feel free to open an [issue](https://github.com/kshvmdn/nowplaying/issues) or make a [pull request](https://github.com/kshvmdn/nowplaying/pulls). All contributions are welcome.
