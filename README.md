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

+ Run `./nowplaying.py` to see current song.

    ```
    $ ./nowplaying.py np
    Can't Tell Me Nothing - Kanye West
    Graduation (Deluxe Edition)
    ```

+ Commands (replace `np` with the command you want to use):

    + View now playing - `np` (also can be used to open iTunes & play song if iTunes is not open)
    + Play - `play`
    + Pause - `pause`
    + Stop - `stop`
    + Play next - `next`
    + Play previous  - `prev`
    + Close iTunes - `close`

+ _Optional_ step: create [aliases](http://tldp.org/LDP/abs/html/aliases.html) in your `.bashrc` / `.zshrc` to run without the `./nowplaying.py`. Here are some examples:

    + `np="/path/to/nowplaying.py np"`
    + `play="/path/to/nowplaying.py play"`
    + `next="/path/to/nowplaying.py next"`

#### Contribute

Feel free to open an [issue](https://github.com/kshvmdn/nowplaying/issues) or make a [pull request](https://github.com/kshvmdn/nowplaying/pulls). All contributions are welcome.
