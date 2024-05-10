'''
功能介绍：
指定练习音高的范围和乐器种类，根据播放的音乐来输入音高，每10次可以计算准确率。

'''



import pygame
import random
import time
import os
import sys
import re
# Initialize the pygame mixer
pygame.mixer.init()

# Path to the directory containing the audio files
# NOTES_DIR = "notes/Violin" # 小提琴
# NOTES_DIR = "notes/Piano_2s" # 钢琴
NOTES_DIR = "notes/SteelGuitarF" # 吉他（钢弦）



pattern = r'/([^/]+)'
match = re.search(pattern, NOTES_DIR)
if match:
    instrumentType = match.group(1)
else:
    instrumentType = None


# Mapping of musical notes to their corresponding audio files
NOTES = { # 可以修改练习的范围
    # "F1": "F1.wav",
    # "G1": "G1.wav",
    # "A1": "A1.wav",
    # "B1": "B1.wav",
    # "C2": "C2.wav",
    # "D2": "D2.wav",
    # "E2": "E2.wav",
    "F2": "F2.wav",
    "G2": "G2.wav",
    "A2": "A2.wav",
    "B2": "B2.wav",
    "C3": "C3.wav",
    "D3": "D3.wav",
    "E3": "E3.wav",
    "F3": "F3.wav",
    "G3": "G3.wav",
    "A3": "A3.wav",
    "B3": "B3.wav",
    "C4": "C4.wav",
    "D4": "D4.wav",
    "E4": "E4.wav",
    "F4": "F4.wav",
    "G4": "G4.wav",
    "A4": "A4.wav",
    "B4": "B4.wav",
    "C5": "C5.wav",
    "D5": "D5.wav",
    "E5": "E5.wav",
    "F5": "F5.wav",
    "G5": "G5.wav",
    # "A5": "A5.wav",
    # "B5": "B5.wav",
    # "C6": "C6.wav",
    # "D6": "D6.wav",
    # "E6": "E6.wav",
    # "F6": "F6.wav",
    # "G6": "G6.wav",
    # "A6": "A6.wav",
    # "B6": "B6.wav",
    # "C7": "C7.wav"
}


# Load audio files from the notes directory
for note, file in NOTES.items():
    NOTES[note] = pygame.mixer.Sound(os.path.join(NOTES_DIR, file))


def play_note(note, times=1, interval=1):
    """Play a note a specified number of times with an interval in seconds."""
    for _ in range(times):
        NOTES[note].play()
        time.sleep(interval)

def absolute_pitch_training():
    print(f"Instrument type is : {instrumentType}")
    all_notes = list(NOTES.keys())
    print(f"All Notes are: {all_notes}")

    def play_exercise():

        print(f"Listen carefully to the target note played three times.")
        # Choose a target note
        target_note = random.choice(all_notes)
        play_note(target_note, times=3, interval=1)
        time.sleep(3)  # Pause for 3 seconds before continuing

        user_input = str(input("Identify the target note : "))
        print(f"\nTarget Note: {target_note}")


        if user_input == target_note:
            print("Correct!")
            print("Play again!")
            play_note(target_note, times=3, interval=1)
            next_exercise = input("Do you want to continue with another exercise? (y/n): ").strip().lower()
            if next_exercise != 'y':
                sys.exit("Exiting the program.")
            else:
                time.sleep(1)
            return True
        else:
            print(f"Wrong! The correct answer was {target_note}")
            print("Play again!")
            play_note(target_note, times=3, interval=1)
            next_exercise = input("Do you want to continue with another exercise? (y/n): ").strip().lower()
            if next_exercise != 'y':
                sys.exit("Exiting the program.")
            else:
                time.sleep(1)
            return False
    

    def training_session():
        correct_answers = 0
        for _ in range(10):
            if play_exercise():
                correct_answers += 1
        print(f"\nSummary: You got {correct_answers} out of 10 correct.\n")

    while True:
        training_session()
        next_session = input("Do you want to continue with another session? (y/n): ").strip().lower()
        if next_session != 'y':
            break

# Run the training program
absolute_pitch_training()
