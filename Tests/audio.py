import os
import winsound

this_dir = os.path.dirname(os.path.abspath(__file__))
music_file = os.path.join(this_dir, "Organization Battle.wav")

if not os.path.exists(music_file):
    print(f"Audio file not found: {music_file}")
else:
    print('Commands: "play", "pause", "end"')

    while True:
        command = input("> ").strip().lower()

        if command == "play":
            winsound.PlaySound(music_file, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
            print("Music started looping.")

        elif command == "pause":
            winsound.PlaySound(None, winsound.SND_PURGE)
            print("Music paused (stopped).")

        elif command == "end":
            winsound.PlaySound(None, winsound.SND_PURGE)
            print("Playback stopped. Goodbye!")
            break

        else:
            print("Unknown command. Try play, pause, or end.")