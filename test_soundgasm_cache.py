import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import soundgasm


class SoundgasmCacheTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.output = patch.object(soundgasm, "OUTPUT_DIR", self.directory.name)
        self.output.start()
        self.addCleanup(self.output.stop)
        self.cache = Path(self.directory.name) / "cache"
        self.url = "https://soundgasm.net/u/example/recording"

    def test_cached_pages_skip_resolution_and_download(self):
        for ending in ("\n", "\r\n", ""):
            with self.subTest(ending=repr(ending)):
                self.cache.write_bytes((self.url + ending).encode())
                with patch.object(
                    soundgasm, "extract_audio_file_url_from_soundgasm_audio_page_url"
                ) as resolve, patch.object(soundgasm, "extract_audio_from_url") as download:
                    soundgasm.extract_audio_from_page_url(self.url)
                resolve.assert_not_called()
                download.assert_not_called()

    def test_successful_download_is_cached_once(self):
        audio = "https://soundgasm.net/sounds/example.m4a"
        with patch.object(
            soundgasm, "extract_audio_file_url_from_soundgasm_audio_page_url",
            return_value=audio,
        ) as resolve, patch.object(soundgasm, "extract_audio_from_url") as download:
            soundgasm.extract_audio_from_page_url(self.url)
            soundgasm.extract_audio_from_page_url(self.url)
        resolve.assert_called_once_with(self.url)
        download.assert_called_once_with(audio, "example", "recording")
        self.assertEqual(self.cache.read_text(), self.url + "\n")

    def test_unresolved_page_is_not_cached(self):
        with patch.object(
            soundgasm, "extract_audio_file_url_from_soundgasm_audio_page_url",
            return_value=None,
        ), patch.object(soundgasm, "extract_audio_from_url") as download:
            soundgasm.extract_audio_from_page_url(self.url)
        download.assert_not_called()
        self.assertEqual(self.cache.read_text(), "")

    def test_failed_download_is_not_cached(self):
        with patch.object(
            soundgasm, "extract_audio_file_url_from_soundgasm_audio_page_url",
            return_value="https://soundgasm.net/sounds/example.m4a",
        ), patch.object(
            soundgasm, "extract_audio_from_url", side_effect=OSError("mock failure")
        ):
            with self.assertRaises(OSError):
                soundgasm.extract_audio_from_page_url(self.url)
        self.assertEqual(self.cache.read_text(), "")


if __name__ == "__main__":
    unittest.main()
