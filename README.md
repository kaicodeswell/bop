## 🎵 Moodify - Terminal Spotify Controller with Mood-Based Music
Moodify is a terminal-based Python tool that lets you control Spotify and discover songs based on your mood — all from your command line.

# 🌟 Features
⏯️ Play / pause, skip songs, show current track

🔍 Search and play any song on Spotify

🧠 Suggest songs/playlists based on your mood (e.g., happy, sad, focus, chill)

💻 All from the terminal — no browser needed!

# 📦 Requirements
Python 3.7+

A Spotify Premium account

A registered Spotify Developer App

Install the required libraries:


`pip install spotipy termcolor`
# 🛠️ Setup
Register your app at Spotify Developer Dashboard.

Set the Redirect URI to:

```
http://localhost:8888/callback
```
Copy your Client ID and Client Secret.

In your terminal, run:

```
export SPOTIPY_CLIENT_ID='your_client_id_here'
export SPOTIPY_CLIENT_SECRET='your_client_secret_here'
export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
```
(For Windows: use set instead of export)

🚀 How to Run
bash
`python moodify.py`
Follow the terminal prompts to:

Select your mood 🎭

Or use direct commands to control playback 🎵

🧠 Example Moods
happy

sad

chill

focus

workout

love

party

🧑‍💻 Author
Made with ❤️ by kaicodeswell
