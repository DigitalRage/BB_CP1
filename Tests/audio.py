import os
import winsound
import msvcrt   # replaced keyboard with msvcrt

# Build absolute paths to all files
this_dir = os.path.dirname(os.path.abspath(__file__))
tracks = {
    "battle": os.path.join(this_dir, "Organization Battle.wav"),
    "town": os.path.join(this_dir, "Twilight Town.wav"),
    "destiny": os.path.join(this_dir, "Destiny Islands.wav")
}

# Verify files exist
for name, path in tracks.items():
    if not os.path.exists(path):
        print(f"Missing file for {name}: {path}")

print('Commands: "play <name>", "pause", "track", "end"')

track_names = list(tracks.keys())
current_track = None

def play_track(name):
    global current_track
    current_track = name
    winsound.PlaySound(tracks[current_track],
                       winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    print(f"Playing {current_track}...")

while True:
    command = input("> ").strip().lower()

    if command.startswith("play"):
        parts = command.split()
        if len(parts) == 2 and parts[1] in tracks:
            play_track(parts[1])
        else:
            print("Available tracks:")
            for name in track_names:
                print(f"play {name}")

    elif command == "pause":
        winsound.PlaySound(None, winsound.SND_PURGE)
        print("Playback paused.")

    elif command == "track":
        print("Track mode: press = for next, - for previous, Backspace to exit")
        while True:
            if msvcrt.kbhit():  # check if a key was pressed
                key = msvcrt.getch()

                # decode to string if possible
                try:
                    char = key.decode('utf-8')
                except UnicodeDecodeError:
                    char = ''

                if char == '=':
                    if current_track:
                        idx = track_names.index(current_track)
                        new_idx = (idx + 1) % len(track_names)
                        play_track(track_names[new_idx])
                    else:
                        play_track(track_names[0])

                elif char == '-':
                    if current_track:
                        idx = track_names.index(current_track)
                        new_idx = (idx - 1) % len(track_names)
                        play_track(track_names[new_idx])
                    else:
                        play_track(track_names[0])

                elif key == b'\x08':  # Backspace key
                    print("Exiting track mode.")
                    break

    elif command == "end":
        winsound.PlaySound(None, winsound.SND_PURGE)
        print("Playback stopped. Goodbye!")
        break

    else:
        print("Unknown command. Try play <name>, pause, track, or end.")