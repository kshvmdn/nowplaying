# nowplaying

Python CLI to control iTunes playback **(_Currently_ OS X only)**.

## Setup

- Requirements:
    + Python

- Installation:
    
  + Clone project
    
    ```
    git clone https://github.com/kshvmdn/nowplaying.git && cd nowplaying
    ```

  + Install requirements

    ```
    pip install -r ./requirements.txt
    ```

## Usage

+ Run with `./nowplaying.py`.

  ```
  Usage: ./nowplaying [--help] [OPTIONS]
    
    CLI to control iTunes playback.
  
  Example:
    ./nowplaying play

  Options:
    -h --help     Display help and usage details
    np            View currently playing song
    next          Skip to the next song
    previous      Play the previous song
    pause         Pause the current song
    play          Open iTunes and play a song
    stop          Stop the currently playing song
    open          Open iTunes
    close         Close iTunes
  ```

+ _Optionally_ set an [alias](http://tldp.org/LDP/abs/html/aliases.html) to run the CLI using a keyword of your choosing.
  
  * `itunes="/path/to/nowplaying.py"`
  * `play="itunes play"`
  * `np="itunes np"`

#### Contribute

Feel free to open an [issue](https://github.com/kshvmdn/nowplaying/issues) or make a [pull request](https://github.com/kshvmdn/nowplaying/pulls). All contributions are welcome.
