# Nama File : MainPage.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : Rabu, 22 Mei 2024; Jumat, 31 Mei 2024

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Profile import show_profile_page
from StartGame2 import show_start_game_page
from Leaderboard2 import show_leaderboard_page

# def show_main_page(root, show_login_page_func):
def show_main_page(root, show_login_page_func,user):
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("400x300")
    root.title('Main Page')
    root.iconbitmap('./img/logo_2.ico')  # Menambahkan logo

    title_label = ttk.Label(root, text="Main Page", font=("Helvetica", 24))
    title_label.pack(pady=20)

    # Logout button
    logout_button = ttk.Button(root, text="Logout", command=lambda: show_login_page_func(root))
    logout_button.place(relx=0.9, rely=0.05, anchor="ne")

    # Start Game button
    start_game_button = ttk.Button(root, text="Start Game", command=lambda: show_start_game_page(root, show_main_page, show_login_page_func,user))
    start_game_button.pack(fill='x', expand=True, padx=20, pady=5)

    # Leaderboard button
    leaderboard_button = ttk.Button(root, text="Leaderboard", command=lambda: show_leaderboard_page(root, show_main_page, show_login_page_func,user))
    leaderboard_button.pack(fill='x', expand=True, padx=20, pady=5)

    # Profile button
    profile_button = ttk.Button(root, text="Profile", command=lambda: show_profile_page(root, show_main_page, show_login_page_func,user))
    profile_button.pack(fill='x', expand=True, padx=20, pady=5)

# END_OF_FILE[]