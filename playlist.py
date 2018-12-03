import spotipy
import spotipy.oauth2 as oauth2
import urllib.request
import urllib.parse
import re
import secret
import subprocess
import json
from requests.utils import quote
import argparse
import os

def generate_token():
    credentials = oauth2.SpotifyClientCredentials(
        client_id=secret.SPOTIFY_CLIENT_ID,
        client_secret=secret.SPOTIFY_CLIENT_SECRET)
    token = credentials.get_access_token()
    return token

def get_youtube_url(search_query):
    search_query_fixed = quote(search_query)
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=" + search_query_fixed + "&key=" + secret.YOUTUBE_CLIENT_ID
    data = None
    with urllib.request.urlopen(url) as urllib_url:
        data = json.loads(urllib_url.read().decode())
    vid_id = data['items'][0]['id']['videoId']
    youtube_url = "https://www.youtube.com/watch?v=" + vid_id
    print(youtube_url)
    return youtube_url

def download_mp3(url, location):

    bashCommand = 'youtube-dl --extract-audio -o "%(title)s.%(ext)s" --audio-format mp3 --embed-thumbnail ' + url
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, cwd=location)
    output, error = process.communicate()

def write_tracks(text_file, tracks, location):
    with open(text_file, 'a') as file_out:
        while True:
            for item in tracks['items']:
                if 'track' in item:
                    track = item['track']
                else:
                    track = item
                search_query = track['name']
                if "artists" in track:
                    search_query = track['name'] + " " + track['artists'][0]['name']
                file_out.write(search_query + '\n')
                url = get_youtube_url(search_query)
                download_mp3(url, location)
            if tracks['next']:
                tracks = spotify.next(tracks)
            else:
                break

def write_playlist(username, playlist_id):
    results = spotify.user_playlist(username, playlist_id, fields='tracks,next,name')
    playlist_name = results['name']
    text_file = u'{0}.txt'.format(results['name'], ok='-_()[]{}')
    print(u'Writing {0} tracks to {1}'.format(
            results['tracks']['total'], text_file))
    tracks = results['tracks']
    return playlist_name, text_file, tracks

def split_spotify_uri(uri):
    uri_split = uri.split(":")
    return uri_split[2], uri_split[4]

def get_os():
    import platform
    if platform.system() == "Windows":
        return "Windows"
    elif platform.system() == "Darwin":
        return "Mac"
    else:
        return "Linux"

def get_folder(os_type, folder, new, playlist_name):
    if os_type == "Windows":
        if folder == "":
            return os.getcwd() + "\\"
        if not folder[-1] == "\\":
            folder = folder + "\\"
        if not folder[1:2] == ":":
            cwd = os.getcwd() + "\\"
            folder = cwd + folder
        if new:
            folder = folder + playlist_name + "\\"
            try:
                os.mkdir(folder)
            except:
                print("Folder Already Exists! Music will be added to that folder")
    else:
        if folder == "":
            return os.getcwd() + "/"
        if not folder[-1] == "/":
             folder = folder + "/"
        if not folder[0:1] == "/":
            cwd = os.getcwd() + "/"
            folder = cwd + folder
        if new:
            folder = folder + playlist_name + "/"
            try:
                os.mkdir(folder)
            except:
                print("Folder Already Exists! Music will be added to that folder")
    return folder

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", default="",
	help="where the downloaded music will be")
ap.add_argument("-n", "--new", default=False, action="store_true",
    help="should the mp3s be added to a new folder titled after the playlist")
ap.add_argument("-p", "--playlist", required=True,
    help="Spotify Playlist URI")
args = vars(ap.parse_args())

username, playlist_id = split_spotify_uri(args['playlist'])

token = generate_token()
spotify = spotipy.Spotify(auth=token)

os_type = get_os()
folder = args['folder']
playlist_name, text_file, tracks = write_playlist(username, playlist_id)
folder = get_folder(os, folder, args['new'], playlist_name)
write_tracks(text_file, tracks, folder)

os.remove(playlist_name + ".txt")
