import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

# ------------------ CONFIG ------------------
CLIENT_ID = "your_client_id_here"
CLIENT_SECRET = "your_client_secret_here"
REDIRECT_URI = "http://localhost:8888/callback"
SCOPE = "user-read-playback-state user-modify-playback-state user-read-currently-playing"

MOOD_PLAYLISTS = {
    "happy": "37i9dQZF1DXdPec7aLTmlC",
    "sad": "37i9dQZF1DX7qK8ma5wgG1",
    "energetic": "37i9dQZF1DX1g0iEXLFycr",
    "chill": "37i9dQZF1DX4WYpdgoIcn6",
    "romantic": "37i9dQZF1DWVpvU5duQ5Wv"
}

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

def get_device_id():
    devices = sp.devices()
    for device in devices["devices"]:
        if device["is_active"]:
            return device["id"]
    return None

def play_mood_playlist(mood):
    playlist_id = MOOD_PLAYLISTS.get(mood.lower())
    if not playlist_id:
        print("⚠️ Mood not found. Try happy, sad, energetic, chill, or romantic.")
        return

    device_id = get_device_id()
    if not device_id:
        print("⚠️ No active device found. Open Spotify and play a song once, then try again.")
        return

    sp.start_playback(device_id=device_id, context_uri=f"spotify:playlist:{playlist_id}")
    print(f"🎵 Playing a {mood} playlist!")

def search_and_play(song_name):
    results = sp.search(q=song_name, type='track', limit=1)
    tracks = results['tracks']['items']
    if not tracks:
        print("❌ Song not found.")
        return

    track_uri = tracks[0]['uri']
    device_id = get_device_id()
    if not device_id:
        print("⚠️ No active device found. Open Spotify and try again.")
        return

    sp.start_playback(device_id=device_id, uris=[track_uri])
    print(f"🎶 Now playing: {tracks[0]['name']} - {tracks[0]['artists'][0]['name']}")

def show_current_song():
    current = sp.current_playback()
    if current and current['item']:
        name = current['item']['name']
        artist = current['item']['artists'][0]['name']
        print(f"🎧 Now playing: {name} - {artist}")
    else:
        print("🎧 No song is currently playing.")

def show_menu():
    print("""
🎵 Spotify Terminal Controller 🎵
1️⃣ Play/Pause
2️⃣ Next Track
3️⃣ Previous Track
4️⃣ Show Current Song
5️⃣ Search and Play a Song
6️⃣ Play Mood Playlist
7️⃣ Exit
    """)

def main():
    while True:
        show_menu()
        choice = input("📌 Choose an option (1-7): ").strip()

        if choice == "1":
            playback = sp.current_playback()
            if playback and playback['is_playing']:
                sp.pause_playback()
                print("⏸️ Paused.")
            else:
                sp.start_playback()
                print("▶️ Playing.")
        elif choice == "2":
            sp.next_track()
            print("⏭️ Skipped to next track.")
        elif choice == "3":
            sp.previous_track()
            print("⏮️ Went back to previous track.")
        elif choice == "4":
            show_current_song()
        elif choice == "5":
            song = input("🔍 Enter song name: ")
            search_and_play(song)
        elif choice == "6":
            mood = input("💭 How are you feeling? (happy/sad/energetic/chill/romantic): ")
            play_mood_playlist(mood)
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

