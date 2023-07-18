import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# Load client id and secret id
if __name__ == "__main__":

    with open("./src/keys.py") as keys:
        exec(keys.read())

# Get client authorization

scope = "user-read-recently-played"
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = CLIENT_ID, client_secret = SECRET_ID, scope = scope, redirect_uri = "http://localhost:8080"))

# Get info about current user
user_info = sp.current_user()
print("User name:", user_info["display_name"] + "\n")

last_songs_info = sp.current_user_recently_played(limit = 10)

print("Last 10 songs played:\n")
for song in last_songs_info["items"]:
    print(song["track"]["name"])

