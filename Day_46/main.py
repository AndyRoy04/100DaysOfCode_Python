import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
ID = os.getenv('SPOT_ID')
USER = os.getenv('USER_ID')
SECRET = os.getenv('SPOT_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
PLAY_ID= os.getenv('PLAYLIST_ID')

period_date = input("Which year do you want to travel to? Type the date in the this format YYYY-MM-DD: ")
year = period_date.split('-')[0]
URL = f"https://www.billboard.com/charts/hot-100/"

response = requests.get(URL)
billboard_website = response.text

soup = BeautifulSoup(billboard_website, 'html.parser')

all_music = soup.select(selector='li ul li h3')
music_list = []

for music in all_music:
    music_list.append(music.getText().strip('\t\t\n\n'))

# #------------------------------ Code to generate access token to user private playlist #------------------------------
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=ID,
        client_secret=SECRET,
        redirect_uri='https://open.spotify.com/',
        scope='playlist-modify-private',
        username='Andy',
        show_dialog=True,
        cache_path='100DaysOfCode_Python/Day_46/token.txt'
    )
)
# user_id = sp.current_user()['id']
# print(user_id)

songs_uri_list = []
for song in music_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        music_uri = result['tracks']['items'][0]['uri']    # Getting the URI of a particular song
        songs_uri_list.append(music_uri)
    except IndexError:
        pass

#------------------------------ Creating a new playlist #------------------------------
# playlist = sp.user_playlist_create(user=USER, name=f'{period_date} Top Songs', public=False)
# print(playlist['id'])  # Get the playlist ID insert in .env file if neccessary

# #------------------------------ Adding songs to an existing list
sp.playlist_add_items(playlist_id=PLAY_ID, items=songs_uri_list)











# #------------------------------ Code to add musics to a new playlist #------------------------------
# play_url = f'https://api.spotify.com/v1/playlists/{PLAY_ID}/tracks'
# data = {
#     'uris': songs_uri_list,
# }
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': f'Bearer {ACCESS_TOKEN}',
# }
# play_response = requests.post(play_url, data, headers=headers)

# pprint(play_response.text)
# # -------------------------------


# #------------------------------ Code to create new playlist #------------------------------
# playlist_endpoint = f'https://api.spotify.com/v1/users/{USER}/playlists'
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': f'Bearer {ACCESS_TOKEN}',
# }
# parameters = {
#     'name': f'{period_date} Billboard Hot 100',
#     'description': 'Top Songs of the year',
#     'public': False,
# }

# new_response = requests.post(playlist_endpoint, json=parameters, headers=headers)

# pprint(new_response.text)