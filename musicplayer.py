# -*- coding: utf-8 -*-
"""

@author: musta
"""

import os
import pygame
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, Scrollbar

# Initialize pygame mixer for playing music
pygame.mixer.init()

class MusicPlayer:
    def __init__(self, window):
        self.window = window
        self.window.title("Music Player by Mustafa")
        self.window.geometry("500x400")
        self.window.config(bg='black')

        # Create buttons and labels for the music player
        self.label = tk.Label(window, text="Music Player", font=("Arial", 20), bg='lightblue')
        self.label.pack(pady=10)

        # Label to display the current song name
        self.song_label = tk.Label(window, text="No song loaded", font=("Arial", 14), bg='lightblue')
        self.song_label.pack(pady=10)

        # Create a listbox to display the songs in the folder
        self.song_listbox = Listbox(window, font=("Arial", 12), bg="white", selectmode=tk.SINGLE, height=10)
        self.song_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        # Scrollbar for the listbox
        self.scrollbar = Scrollbar(self.song_listbox)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.song_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.song_listbox.yview)

        # Buttons to control the music player
        self.load_folder_button = tk.Button(window, text="Load Folder", command=self.load_folder, font=("Arial", 14))
        self.load_folder_button.pack(pady=5)

        self.play_button = tk.Button(window, text="Play", command=self.play_music, font=("Arial", 14))
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(window, text="Pause", command=self.pause_music, font=("Arial", 14))
        self.pause_button.pack(pady=5)

        self.resume_button = tk.Button(window, text="Resume", command=self.resume_music, font=("Arial", 14))
        self.resume_button.pack(pady=5)

        self.stop_button = tk.Button(window, text="Stop", command=self.stop_music, font=("Arial", 14))
        self.stop_button.pack(pady=5)

        self.current_song = None
        self.song_list = []
        self.is_paused = False

    # Load music folder and display song list
    def load_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            # Get list of all .mp3 and .wav files in the selected folder
            self.song_list = [f for f in os.listdir(folder_selected) if f.endswith(('.mp3', '.wav'))]
            if self.song_list:
                self.song_listbox.delete(0, tk.END)  # Clear the listbox before loading new songs
                for song in self.song_list:
                    self.song_listbox.insert(tk.END, song)  # Add songs to the listbox
                messagebox.showinfo("Folder Loaded", f"{len(self.song_list)} songs loaded.")
            else:
                messagebox.showwarning("No Songs Found", "No MP3 or WAV files found in this folder.")

    # Play the selected song
    def play_music(self):
        selected_song_index = self.song_listbox.curselection()
        if selected_song_index:
            selected_song = self.song_listbox.get(selected_song_index)
            folder_path = filedialog.askdirectory()  # Get the folder from where the user loaded the songs
            song_path = os.path.join(folder_path, selected_song)  # Full path to the selected song
            if os.path.exists(song_path):
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play(loops=0)
                self.is_paused = False
                self.song_label.config(text=f"Playing: {selected_song}")  # Update the label with the playing song
            else:
                messagebox.showwarning("Error", "Unable to play the selected song.")
        else:
            messagebox.showwarning("No Song Selected", "Please select a song from the list.")

    # Pause the music
    def pause_music(self):
        if not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
            self.song_label.config(text="Paused")

    # Resume the music
    def resume_music(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            selected_song = self.song_listbox.get(tk.ACTIVE)  # Get the currently selected song
            self.song_label.config(text=f"Playing: {selected_song}")  # Update label back to "Playing"

    # Stop the music
    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_paused = False
        self.song_label.config(text="Stopped")

# Create the main application window
window = tk.Tk()
app = MusicPlayer(window)

# Run the application
window.mainloop()
