import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Client ID and Client Secret
CLIENT_ID = "ceec33d0916344e69bd3bd6dd418a2a7"
CLIENT_SECRET = "1fe8732cf1db479f847d33b564ca6d5b"

# Client Credentials Flow
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, 
                                                           client_secret=CLIENT_SECRET))

# Tracks from Spotify's US Top 50 Playlist
playlist_id = "37i9dQZEVXbLRQDuF5jeBp"  # Spotify US Top 50 playlist
results = sp.playlist_tracks(playlist_id, limit=10)

# Print track names
for idx, track in enumerate(results['items']):
    print(f"{idx+1}. {track['track']['name']} by {track['track']['artists'][0]['name']}")
