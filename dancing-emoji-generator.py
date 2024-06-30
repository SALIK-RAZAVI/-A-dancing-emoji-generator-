import tkinter as tk
import random
import time
from pygame import mixer

# Initialize pygame mixer
mixer.init()

# List of random music files (ensure these files are in the same directory or provide the full path)
music_files = ['music1.mp3', 'music2.mp3', 'music3.mp3']

# Randomly select a music file and play it
random_music = random.choice(music_files)
mixer.music.load(random_music)
mixer.music.play(-1)  # Play the music in a loop

# List of emojis for dance routines
emojis = ['💃', '🕺', '🦄', '🐱', '🐸', '🐍', '🐒', '🐦','🕺','🦄']

# Function to create a random dance routine
def create_dance_routine():
    routine = []
    for _ in range(10):  # Create a sequence of 10 random emojis
        routine.append(random.choice(emojis))
    return routine

# Function to display the dance routine
def display_routine(routine, label):
    def update_label(i=0):
        if i < len(routine):
            label.config(text=routine[i])
            root.after(500, update_label, i + 1)
        else:
            label.config(text="Dance Over!")

    update_label()

# Setup tkinter GUI
root = tk.Tk()
root.title("Dancing Emoji Generator")
root.geometry("400x200")

# Label to display emojis
emoji_label = tk.Label(root, text="", font=("Helvetica", 80))
emoji_label.pack(expand=True)

# Button to generate and display a new dance routine
def generate_dance():
    routine = create_dance_routine()
    display_routine(routine, emoji_label)

generate_button = tk.Button(root, text="Generate Dance Routine", command=generate_dance)
generate_button.pack(pady=20)

# Start the tkinter main loop
root.mainloop()

# Quit the mixer on exit
mixer.quit()
