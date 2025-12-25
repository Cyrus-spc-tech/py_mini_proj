import os
import pygame

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

def play_music(folder, song_n):
    file_path = os.path.join(folder, song_n)

    if not os.path.exists(file_path):
        print("File not found")
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print(f"\nNow playing: {song_n}")
    print("Pause: 'P', Resume: 'R', Stop: 'S', Change : 'C'")

    while True :
        command=input(">").upper()

        if command == "P":
            pygame.mixer.music.pause()
            print('paused')
        elif command == "R":
            pygame.mixer.music.unpause()
            print('resumed')
        elif command == "S":
            pygame.mixer.music.stop()
            print('stopped')
        elif command == "C":
            main()
        else:
            print("Invalid command")


def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print(f"Audio initialization failed! {e}")
        return

    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.join(script_dir, "audio")

    if not os.path.isdir(folder):
        print(f"Error: Audio folder not found at: {folder}")
        print("Please make sure the 'audio' folder exists in the same directory as this script.")
        return

    mp3_files = [f for f in os.listdir(folder) if f.lower().endswith('.mp3')]

    if not mp3_files:
        print("No MP3 files found in the audio folder.")
        return

    print("Found the following MP3 files:")
    for i, song in enumerate(mp3_files, 1):
        print(f"{i}. {song}")

    while True:
        print("___________________ MP3 Player __________________")
        print("Song List:")
        for i, song in enumerate(mp3_files, start=1):
            print(f"{i}. {song}")

        choice = input("\nEnter the song # to play (or Q to quit): ")
        if choice.upper() == 'Q':
            print("Goodbye!")
            break

        if not choice.isdigit():
            print("Enter a valid number")
            continue

        choice = int(choice) - 1

        if 0 <= choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
