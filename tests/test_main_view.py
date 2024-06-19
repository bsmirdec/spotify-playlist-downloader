import pytest
import tkinter as tk
from unittest.mock import MagicMock, patch
from spd.views.main_view import MainView

class TestMainView:
    @pytest.fixture
    def setup_view(self):
        # Mock le contrôleur et initialise la vue
        controller = MagicMock()
        view = MainView(controller)
        return view, controller

    def test_init(self, setup_view):
        view, _ = setup_view
        assert view.title() == "Spotify Playlist Downloader"
        assert isinstance(view.url_entry, tk.Entry)
        assert isinstance(view.download_button, tk.Button)

    @patch('tkinter.filedialog.askdirectory', return_value="/mock/path")
    def test_download_playlist(self, mock_filedialog, setup_view):
        view, controller = setup_view
        view.url_entry.insert(0, "https://open.spotify.com/playlist/1yxx3XX1b2b3b4c5d6e7f8g9")
        view.download_playlist()
        controller.download_playlist.assert_called_once_with(
            "https://open.spotify.com/playlist/1yxx3XX1b2b3b4c5d6e7f8g9", "/mock/path"
        )