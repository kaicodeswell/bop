import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "3e8926b4d02449e5b9ab84c00ab721a5"
CLIENT_SECRET = "8c726df566994d5ea2de6df43858a059"
REDIRECT_URI = "http://127.0.0.1:8888/callback/"
SCOPE = "user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

def search_and_play():
    query = input("🔎 Search for a song: ")
    results = sp.search(q=query, limit=1, type='track')
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        uri = track['uri']
        name = track['name']
        artist = track['artists'][0]['name']
        print(f"🎶 Playing: {name} - {artist}")
        sp.start_playback(uris=[uri])
    else:
        print("❌ Song not found.")

def pause():
    sp.pause_playback()
    print("⏸️ Paused.")

def play():
    sp.start_playback()
    print("▶️ Resumed.")

def next_track():
    sp.next_track()
    print("⏭️ Next track.")

def previous_track():
    sp.previous_track()
    print("⏮️ Previous track.")

def show_recent():
    print("🕘 Recently Played Tracks:")
    recent = sp.current_user_recently_played(limit=5)
    for idx, item in enumerate(recent['items']):
        track = item['track']
        print(f"{idx + 1}. {track['name']} - {track['artists'][0]['name']}")

def main():
    print("🎧 Welcome to Spotiterm 🎧")
    while True:
        print("""
📀 Menu:
1. Search & Play a Song
2. Pause
3. Resume
4. Next Track
5. Previous Track
6. Show Recently Played
7. Exit
        """)
        choice = input("📌 Your choice: ").strip()
        if choice == '1':
            search_and_play()
        elif choice == '2':
            pause()
        elif choice == '3':
            play()
        elif choice == '4':
            next_track()
        elif choice == '5':
            previous_track()
        elif choice == '6':
            show_recent()
        elif choice == '7':
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
