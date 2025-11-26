import os
import winsound
import time

# Build absolute path to the WAV file in the same folder as this script
this_dir = os.path.dirname(os.path.abspath(__file__))
music_file = os.path.join(this_dir, "Organization Battle.wav")

if not os.path.exists(music_file):
    print(f"Audio file not found: {music_file}")
else:
    # Play asynchronously in the background
    winsound.PlaySound(music_file, winsound.SND_FILENAME | winsound.SND_ASYNC)

    # Keep the program alive long enough for the music to play
    # Adjust sleep time to match your audio length
    time.sleep(127)

    # Stop playback when done
    winsound.PlaySound(None, winsound.SND_PURGE)