import os
import pytest
from unittest.mock import patch
from yt_dlp import YoutubeDL
from spd.utils.downloader import download_mp3  # Remplacez 'your_module' par le nom de votre module

@pytest.fixture
def sample_tracks():
    # Exemple de données de pistes pour les tests
    return [
        {"name": "Song 1", "artist": "Artist 1"},
        {"name": "Song 2", "artist": "Artist 2"},
    ]

@pytest.fixture
def destination_folder(tmpdir):
    # Utilisation de tmpdir pour créer un dossier temporaire pour les tests
    return str(tmpdir)

def test_download_mp3_existing_files(sample_tracks, destination_folder):
    # Créer un fichier de test existant dans le dossier de destination
    existing_file_name = "Song 1 - Artist 1.mp3"
    existing_file_path = os.path.join(destination_folder, existing_file_name)
    with open(existing_file_path, "w"):
        pass  # Créez simplement le fichier vide pour simuler un fichier existant

    # Mock YoutubeDL pour éviter de télécharger réellement les fichiers
    with patch.object(YoutubeDL, 'extract_info') as mock_extract_info, \
         patch.object(YoutubeDL, 'download') as mock_download:

        # Simulation des informations de téléchargement
        mock_extract_info.return_value = {"title": "Mocked Song"}

        # Exécuter la fonction à tester
        download_mp3(sample_tracks, destination_folder)

        # Vérifier que les fichiers ont été correctement traités
        for track in sample_tracks:
            file_name = f'{track["name"]} - {track["artist"]}.mp3'
            file_path = os.path.join(destination_folder, file_name)

            # Vérifier si le fichier a été créé dans le dossier de destination
            assert os.path.exists(file_path), f"Expected file '{file_name}' not found in '{destination_folder}'"

def test_download_mp3_skip_existing_files(sample_tracks, destination_folder):
    # Créer un fichier de test existant dans le dossier de destination
    existing_file_name = "Song 1 - Artist 1.mp3"
    existing_file_path = os.path.join(destination_folder, existing_file_name)
    with open(existing_file_path, "w"):
        pass  # Créez simplement le fichier vide pour simuler un fichier existant

    # Mock YoutubeDL pour éviter de télécharger réellement les fichiers
    with patch.object(YoutubeDL, 'extract_info') as mock_extract_info, \
         patch.object(YoutubeDL, 'download') as mock_download:

        # Simulation des informations de téléchargement
        mock_extract_info.return_value = {"title": "Mocked Song"}

        # Exécuter la fonction à tester
        download_mp3(sample_tracks, destination_folder)

        # Vérifier que les fichiers existants ne sont pas téléchargés à nouveau
        assert not mock_download.called, "Expected download method not to be called for existing files"
