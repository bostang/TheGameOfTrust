# Nama File : Leaderboard.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : Rabu, 22 Mei 2024 ; Jumat, 31 Mei 2024

import tkinter as tk
from tkinter import ttk
import display_leaderboard2 as dl
# import ServerGOT as sg
import client2 as c

def show_leaderboard_page(root, show_main_page_func, show_login_page_func,user):
    for widget in root.winfo_children():
        widget.destroy()

    root.title('Leaderboard')
    title_label = ttk.Label(root, text="Leaderboard Page", font=("Helvetica", 18))
    title_label.pack(pady=20)

    data = eval(c.socket_client([2,user])) # dari string diubah ke array
    print(data)
    dl.show_leaderboard(root,data)

    back_button = ttk.Button(root, text="Back to Main", command=lambda: show_main_page_func(root, show_login_page_func,user))
    back_button.pack(fill='x', expand=True, padx=20, pady=5)

# END_OF_FILE[]