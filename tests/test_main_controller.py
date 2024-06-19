import pytest
from unittest import mock
from spd.controllers.main_controller import MainController
from spd.models.spotify_api import SpotifyAPI
from spd.views.main_view import MainView
from spd.utils.downloader import download_mp3

@pytest.fixture
def controller():
    with mock.patch.object(SpotifyAPI, '__init__', lambda x: None):
        with mock.patch.object(MainView, '__init__', lambda x, y: None):
            controller = MainController()
            controller.model = mock.Mock(spec=SpotifyAPI)
            controller.view = mock.Mock(spec=MainView)
            return controller

def test_get_playlist(controller):
    mock_playlist = [{"name": "Track 1", "artist": "Artist 1"}, {"name": "Track 2", "artist": "Artist 2"}]
    controller.model.get_playlist.return_value = mock_playlist
    
    url = "https://open.spotify.com/playlist/mockplaylistid"
    result = controller.get_playlist(url)
    
    assert result == mock_playlist
    controller.model.get_playlist.assert_called_with(url)

def test_download_playlist(controller):
    mock_playlist = [{"name": "Track 1", "artist": "Artist 1"}, {"name": "Track 2", "artist": "Artist 2"}]
    controller.model.get_playlist.return_value = mock_playlist

    url = "https://open.spotify.com/playlist/mockplaylistid"
    destination = "/mock/destination/folder"
    
    with mock.patch('spd.controllers.main_controller.download_mp3') as mock_download_mp3:
        controller.download_playlist(url, destination)
        
        controller.model.get_playlist.assert_called_with(url)
        mock_download_mp3.assert_called_with(mock_playlist, destination)

def test_run(controller):
    with mock.patch.object(controller.view, 'mainloop') as mock_mainloop:
        controller.run()
        mock_mainloop.assert_called()
