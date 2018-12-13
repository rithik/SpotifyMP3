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

#### Linux:
Use the following command to install the latest version of python: `sudo apt-get install python3`

### 2. Install the youtube-dl library. You can do this by following one of the steps below:
a. If you have a Mac, you can use `brew install youtube-dl`<br/>
b. If you have a Linux based machine, `sudo pip install --upgrade youtube_dl`<br/>
c. If you have a Windows computer, follow directions at [https://rg3.github.io/youtube-dl/download.html](https://rg3.github.io/youtube-dl/download.html).<br/>

### 3. Now, install all of the required python packages.
`pip3 install -r requirements.txt`

### 4. Get your Spotify API credentials.

a. Navigate to [https://developer.spotify.com/dashboard/login](https://developer.spotify.com/dashboard/login) and create an account.<br/>
b. Click "Create a client id".<br/>
c. Fill out the form.<br/>
d. You should see a client id and a client secret.<br/>

### 5. Get your Youtube Data API key.

a. Navigate to [https://console.cloud.google.com](https://console.cloud.google.com) and create an account.<br/>
b. In the search, search for "Youtube Data API".<br/>
c. Enable the API.<br/>
d. You should see an api key.<br/>

### 6. Run the following command and copy in the appropriate values into the `secret.py` file.

`cp secret.py.example secret.py`

Your `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` will be found in the Spotify API Console. The `YOUTUBE_CLIENT_ID` will be the api key found in your Google Cloud Console.

### 7. Get your Spotify playlist URI.

You can do this by going to the Spotify desktop application and right clicking on the top bar near the playlist name. Click on the "Copy Spotify URI" option located in the "Share" menu.

### 8. Run the program by typing the following command with the following required and optional arguments.
`python3 playlist.py -p SPOTIFY_PLAYLIST_URI -f [OPTIONAL - folder to save the mp3s] -n [OPTIONAL - create new folder to save the mp3s]`
