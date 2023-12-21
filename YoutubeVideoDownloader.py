from tkinter import *
import tkinter as tk
import customtkinter as ctk
from pytube import YouTube, Stream

num = 0
def number():
    global num
    num += 1
    return num

def Download():
    i=number()
    yt = YouTube(link_entry.get())
    history_label = ctk.CTkLabel(history_frame, text=str(i)+"] "+ yt.title, font=ctk.CTkFont(family="Comic Sans MS"))
    history_label.pack()
    youtubeObject = YouTube(link_entry.get(), on_progress_callback=update_progress)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    youtubeObject.download(path_entry.get())
    print("Download is completed successfully")
       
def update_progress(stream: Stream, chunk: bytes, bytes_remaining: int):                                                                   
    filesize = stream.filesize
    bytes_received = filesize - bytes_remaining
    percent = 100.0 * (bytes_received / filesize)
    progress_var.set(percent)
    root.update()

root = ctk.CTk()
root.geometry("750x550")
root.title("YouTube Video Downloader")
root.iconbitmap("Icon.ico")

title_label = ctk.CTkLabel(root, text="YouTube Video Downloader", font=ctk.CTkFont(family="Comic Sans MS", size=30, weight="bold")).pack(padx=10, pady=(40,10))

link_entry = ctk.CTkEntry(root, placeholder_text="Enter Your Link Here", font=ctk.CTkFont(family="Comic Sans MS"), width=300)
link_entry.place(relx=0.08, rely=0.2)

path_entry = ctk.CTkEntry(root, placeholder_text="Enter Your Download Destination Here", font=ctk.CTkFont(family="Comic Sans MS"), width=300)
path_entry.place(relx=0.52, rely=0.2)

download_button = ctk.CTkButton(root, text="Download",command=Download,hover_color="#3bb143", fg_color="#800000")
download_button.place(relx=0.4, rely=0.3)

progress_var = tk.DoubleVar(value=0.0)
progressbar = ctk.CTkProgressBar(root, variable=progress_var, orientation="horizontal", mode="determinate")
progressbar.place(relx=0.35, rely=0.4)

history_title_label = ctk.CTkLabel(root, text="HISTORY", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
history_title_label.place(relx=0.43, rely=0.45)

history_frame = ctk.CTkScrollableFrame(root, width=600, height=250, border_width=1)
history_frame.place(relx=0.1, rely=0.51)

root.mainloop()