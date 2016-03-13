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

    + View now playing - `main.py np` (also can be used to open iTunes & play song if iTunes is not open)
    + Play - `main.py play`
    + Pause - `main.py pause`
    + Stop - `main.py stop`
    + Play next - `main.py next`
    + Play previous  - `main.py prev`
    + Close iTunes - `main.py close`

+ _Optional_ step: create [aliases](http://tldp.org/LDP/abs/html/aliases.html) in your `.bashrc` to run without the `python main.py`.

    + `nowplaying="python /path/to/main.py"`
    + `playsong="python /path/to/main.py play"`
    + `next="python /path/to/main.py next"`

#### Contribute

Feel free to open an [issue](https://github.com/kshvmdn/nowplaying/issues) or make a [pull request](https://github.com/kshvmdn/nowplaying/pulls). All contributions are welcome.
