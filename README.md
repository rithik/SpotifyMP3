# Spotify Playlist to MP3s

## Installation

### 1. Install Python3 (the latest version).

You can do this by doing one of the following based on your operating system.

#### Windows:
Download python at the following url: [https://www.python.org/downloads/](https://www.python.org/downloads/). Make sure to download the latest version that formatted like this `Python 3.X.X`.

#### Mac:
First, install HomeBrew, a package manager, that allows you to easily install packages.
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Then, at the bottom of your `~/.profile` file, add the following line:
```
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```
Next, install python with the following command.
```
brew install python
```

### 2. Install the youtube-dl library. You can do this by following one of the steps below:
#### a. If you have a Mac, you can use `brew install youtube-dl`
#### b. If you have a Linux based machine, `sudo pip install --upgrade youtube_dl`
#### c. If you have a Windows computer, follow directions at [https://rg3.github.io/youtube-dl/download.html](https://rg3.github.io/youtube-dl/download.html).

### 3. Now, install all of the python packages required by running the following command `pip3 install -r requirements.txt`.

### 4. Get your Spotify playlist URI.

You can do this by going to the Spotify desktop application and right clicking on the top bar near the playlist name. Click on the "Copy Spotify URI" option located in the "Share" menu.

### 5. Run the program by typing the following command with the following required and optional arguments.
`python3 playlist.py -p SPOTIFY_PLAYLIST_URI -f [OPTIONAL - folder to save the mp3s] -n [OPTIONAL - create new folder to save the mp3s]`
