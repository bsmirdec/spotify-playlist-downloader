import pytest
from unittest import mock
import spotipy
from spotipy.exceptions import SpotifyException
from spd.models.spotify_api import SpotifyAPI

@pytest.fixture
def spotify_api():
    return SpotifyAPI()

def test_extract_playlist_id():
    url = "https://open.spotify.com/playlist/5boS8fbEUdx9APCMMMx4bi?si=79f8f63f6b034dad"
    playlist_id = SpotifyAPI.extract_playlist_id(url)
    assert playlist_id == "5boS8fbEUdx9APCMMMx4bi"

def test_extract_playlist_id_invalid():
    url = "https://open.spotify.com/invalid/5boS8fbEUdx9APCMMMx4bi"
    with pytest.raises(ValueError):
        SpotifyAPI.extract_playlist_id(url)

def test_get_playlist(spotify_api):
    url = "https://open.spotify.com/playlist/5boS8fbEUdx9APCMMMx4bi?si=79f8f63f6b034dad"
    mock_playlist_id = "5boS8fbEUdx9APCMMMx4bi"
    mock_tracks = {
        'items': [
            {'track': {
                'name': 'Track 1',
                'artists': [{'name': 'Artist 1'}],
                'album': {'name': 'Album 1', 'release_date': '2020-01-01'},
                'external_urls': {'spotify': 'https://open.spotify.com/track/mocktrack1'}
            }},
            {'track': {
                'name': 'Track 2',
                'artists': [{'name': 'Artist 2'}],
                'album': {'name': 'Album 2', 'release_date': '2020-01-02'},
                'external_urls': {'spotify': 'https://open.spotify.com/track/mocktrack2'}
            }},
        ]
    }

    with mock.patch.object(spotify_api.sp, 'playlist_tracks', return_value=mock_tracks) as mock_playlist_tracks:
        result = spotify_api.get_playlist(url)
        
        expected_result = [
            {
                'name': 'Track 1',
                'artist': 'Artist 1',
                'album': 'Album 1',
                'release_date': '2020-01-01',
                'track_url': 'https://open.spotify.com/track/mocktrack1'
            },
            {
                'name': 'Track 2',
                'artist': 'Artist 2',
                'album': 'Album 2',
                'release_date': '2020-01-02',
                'track_url': 'https://open.spotify.com/track/mocktrack2'
            }
        ]

        assert result == expected_result
        mock_playlist_tracks.assert_called_once_with(mock_playlist_id)

def test_get_playlist_spotify_exception(spotify_api):
    url = "https://open.spotify.com/playlist/5boS8fbEUdx9APCMMMx4bi?si=79f8f63f6b034dad"
    mock_playlist_id = "5boS8fbEUdx9APCMMMx4bi"
    
    with mock.patch.object(spotify_api.sp, 'playlist_tracks', side_effect=SpotifyException(400, -1, "Mock error")):
        result = spotify_api.get_playlist(url)
        
        assert result is None
