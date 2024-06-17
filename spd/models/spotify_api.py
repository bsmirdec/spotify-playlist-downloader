import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re

client_id = "f8381a19395f40a9b2e710b4cb8f4f88"
client_secret = "f633a1dadf8a4599b1d5c1095ffaba24"

mock_playlist_url = "https://open.spotify.com/playlist/5boS8fbEUdx9APCMMMx4bi?si=79f8f63f6b034dad"

class SpotifyAPI:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    def get_playlist(self, url):
        playlist_id = self.extract_playlist_id(url)
        print("playlist_id :", playlist_id)
        try:
            results = self.sp.playlist_tracks(playlist_id)
            tracks_info = []
            for item in results['items']:
                track = item['track']
                track_info = {
                    'name': track['name'],
                    'artist': track['artists'][0]['name'],
                    'album': track['album']['name'],
                    'release_date': track['album']['release_date'],
                    'track_url': track['external_urls']['spotify']
                }
                tracks_info.append(track_info)
            return tracks_info
        except spotipy.exceptions.SpotifyException as e:
            print(f"Une erreur est survenue lors de la récupération des pistes de la playlist: {e}")
            return None

    @staticmethod
    def extract_playlist_id(url):
        # Utilisation d'une expression régulière pour extraire l'ID de la playlist depuis l'URL
        match = re.search(r'playlist/([a-zA-Z0-9]+)', url)
        if match:
            return match.group(1)
        else:
            raise ValueError("L'URL de la playlist est invalide")
