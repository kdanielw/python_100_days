import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

def clean_text(text):
    text_list = list(text)
    for i in range(len(text_list) -1, -1, -1):
        if text_list[i] == "\n" or text_list[i] == "\t":
            text_list.pop(i)
    return "".join(text_list)

date_to_travel = input("Which day do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
billboard_url = "https://www.billboard.com/charts/hot-100/" + date_to_travel
response = requests.get(url=billboard_url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names_spans)
print(song_names)
print(len(song_names))

artists_raw = [artist.find_next("span").string for artist in soup.find_all("li", class_="lrv-u-width-100p")]
artist = [clean_text(artist) for artist in artists_raw[::2]]
print(len(artist))
print(artist)

# SPOTIFY
load_dotenv()
SPOTIPY_CLIENT_ID = (os.getenv('SPOTIFY_CLIENT_ID'))
SPOTIPY_CLIENT_SECRET = (os.getenv('SPOTIFY_CLIENT_SECRET'))
SPOTIPY_REDIRECT_URI = (os.getenv('SPOTIFY_REDIRECT_URI'))
SPOTIPY_USERNAME = (os.getenv('SPOTIFY_USERNAME'))

scope = "playlist-modify-public"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=scope,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIPY_USERNAME, 
    )
)
user_id = sp.current_user()["id"]

song_uris =[]
year = date_to_travel.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"{song} add.")
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_id = sp.user_playlist_create(
    user = user_id,
    name = f"{date_to_travel} Billboard 100",
    public=True
)

print(f"\n{playlist_id}\n")

sp.playlist_add_items(
    playlist_id=playlist_id["id"],
    items=song_uris
)
