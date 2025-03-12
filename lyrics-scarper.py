import lyricsgenius
import os

# Initialize Genius API (Replace with your actual API key)
genius = lyricsgenius.Genius("jzJO7nGKExU_gcHtd5zyWS3pPjQBGKM9oNvlygDXasJRDo9ez8LL6yTMCjkVRFjK")

# Set the base directory where the songs folder will be created
BASE_DIR = r"D:\Py Projects\Markov Chain"

def save_lyrics(songs, artist_name, album_name="Unknown"):
    # Format artist name for folder naming
    artist_folder = '_'.join(artist_name.split(' '))

    # Define the full path to store lyrics
    save_path = os.path.join(BASE_DIR, "songs", artist_folder)
    
    # Create directories if they don’t exist
    os.makedirs(save_path, exist_ok=True)

    for i, song_title in enumerate(songs, start=1):
        print(f"Fetching lyrics for: {song_title} by {artist_name}...")

        # Search for the song lyrics
        song = genius.search_song(song_title, artist_name)
        
        if song is None:
            print(f"Lyrics not found for {song_title}. Skipping...")
            continue  # Skip to the next song if not found

        # Clean up song title for file naming
        safe_song_title = '-'.join(song_title.replace("'", "").split())

        # Define the full file path
        file_path = os.path.join(save_path, f"{i}_{album_name}_{safe_song_title}.txt")

        # Save lyrics to a file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(song.lyrics)

        print(f"Saved: {file_path}")

if __name__ == '__main__':
    songs = [
        "Headlines",
        "In My Feelings",
        "Hotline Bling",
        "One Dance",
        "Started From the Bottom",
        "Passionfruit",
        "Nonstop",
        "Laugh Now Cry Later",
        "Forever",
        "Take Care"
    ]
    save_lyrics(songs, "Drake")



