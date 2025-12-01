import os
import winsound
import keyboard

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
            if keyboard.is_pressed("="):
                if current_track:
                    idx = track_names.index(current_track)
                    new_idx = (idx + 1) % len(track_names)
                    play_track(track_names[new_idx])
                else:
                    play_track(track_names[0])
                # debounce: wait a tiny moment so one press = one action
                while keyboard.is_pressed("="):
                    pass  
                
            elif keyboard.is_pressed("-"):
                if current_track:
                    idx = track_names.index(current_track)
                    new_idx = (idx - 1) % len(track_names)
                    play_track(track_names[new_idx])
                else:
                    play_track(track_names[0])
                while keyboard.is_pressed("-"):
                    pass  
                
            elif keyboard.is_pressed("backspace"):
                print("Exiting track mode.")
                break

    elif command == "end":
        winsound.PlaySound(None, winsound.SND_PURGE)
        print("Playback stopped. Goodbye!")
        break

    else:
        print("Unknown command. Try play <name>, pause, track, or end.")