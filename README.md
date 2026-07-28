# Sound Scraper

[![GitHub stars](https://img.shields.io/github/stars/chirag127/sound-scraper?style=flat-square)](https://github.com/chirag127/sound-scraper)
[![License](https://img.shields.io/github/license/chirag127/sound-scraper?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue?style=flat-square)](https://python.org)

Python scripts to download audio from Soundgasm and Reddit (r/gonewildaudio) using PRAW and BeautifulSoup.

## Scripts

| Script | Description |
|--------|-------------|
| `soundgasm.py` | Download audio from soundgasm.net user pages or individual audio URLs |
| `redditGWA.py` | Scrape Reddit subreddit posts, extract Soundgasm links, download audio |
| `4chan_scraper.py` | List 4chan boards and threads (stub) |

## Setup

```bash
pip install -r requirements.txt

# Configure Reddit API credentials
cp praw.ini.example praw.ini
# Edit praw.ini with your Reddit API credentials from reddit.com/prefs/apps

# Set output directory (default: ~/audio/Soundgasm)
export SOUNDGASM_OUTPUT_DIR=~/audio/Soundgasm
```

## Reddit API Setup

1. Go to https://www.reddit.com/prefs/apps
2. Create a new "script" app
3. Copy client_id and client_secret to `praw.ini`

## Usage

```bash
# Download from a specific Soundgasm user
python soundgasm.py  # edit the users list in the script

# Download from Reddit r/gonewildaudio
python redditGWA.py
```

## Configuration

- `SOUNDGASM_OUTPUT_DIR` — where audio files are saved (default: `~/audio/Soundgasm`)
- `praw.ini` — Reddit API credentials (never commit this file)

## Requirements

Python 3.10+, PRAW (Reddit API), BeautifulSoup4, requests, tqdm

## License

MIT
