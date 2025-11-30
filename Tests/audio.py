import os
import winsound
import time

# Build absolute path to the WAV file in the same folder as this script
this_dir = os.path.dirname(os.path.abspath(__file__))
music_file = os.path.join(this_dir, "Organization Battle.wav")

if not os.path.exists(music_file):
    print(f"Audio file not found: {music_file}")
else:
    # Play asynchronously in the background, looping until stopped
    winsound.PlaySound(music_file, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    # Keep the program alive while the music loops
    try:
        while True:
            time.sleep(1)  # Sleep in small increments to keep program running
    except KeyboardInterrupt:
        # Stop playback when you press Ctrl+C
        winsound.PlaySound(None, winsound.SND_PURGE)