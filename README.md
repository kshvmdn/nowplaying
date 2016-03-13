# NowPlaying
Python command line tool to see what song is currently playing in iTunes **(OS X only)**.


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
    
    + now playing: `main.py`
    + play: `main.py play`
    + pause: `main.py pause`
    + stop: `main.py stop`
    + play next: `main.py next`
    + play previous: `main.py prev`
    + close: `main.py close`

+ _Optional_ step: create aliases in `.bashrc` to run without the `python main.py`

    i.e.
    + `nowplaying="python /path/to/main.py"`
    + `playsong="python /path/to/main.py play"`
    + `next="python /path/to/main.py next"`

#### Contribute

Feel free to open an issue or make a pull request. All contributions are welcome.
