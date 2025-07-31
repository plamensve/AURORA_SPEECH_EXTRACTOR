import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from tkinterdnd2 import TkinterDnD, DND_FILES
from moviepy import VideoFileClip
from PIL import Image, ImageTk
import whisper
import threading
import os
import sys

last_transcription_path = None
transcribed_text = ""


def extract_audio(video_path, output_audio_path):
    update_progress(20)
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(output_audio_path, logger=None)


def transcribe_audio(audio_path):
    update_progress(40)
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, language="english")
    update_progress(90)
    return result["text"]


def update_progress(percent):
    load_bar["value"] = percent
    load_label.config(text=f"{percent}%")
    root.update_idletasks()


def reset_progress():
    load_bar["value"] = 0
    load_label.config(text="0%")
    root.update_idletasks()


def process_path(file_path):
    global last_transcription_path, transcribed_text

    if not file_path:
        return

    file_label.config(text=f"Selected: {os.path.basename(file_path)}")
    reset_progress()
    update_progress(10)

    is_video = file_path.lower().endswith((".mp4", ".mkv", ".avi"))
    audio_path = "temp_audio.wav" if is_video else file_path

    try:
        if is_video:
            extract_audio(file_path, audio_path)

        transcribed_text = transcribe_audio(audio_path)

        save_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text Files", "*.txt")]
        )
        if save_path:
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(transcribed_text)
            last_transcription_path = save_path
            update_progress(100)
            messagebox.showinfo("Success", "Transcription saved successfully.")
            reset_progress()

        if is_video and os.path.exists("temp_audio.wav"):
            os.remove("temp_audio.wav")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        reset_progress()


def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Audio/Video Files", "*.mp3 *.mp4 *.wav *.m4a *.mkv *.avi")]
    )
    if file_path:
        threading.Thread(target=process_path, args=(file_path,)).start()


def drop(event):
    file_path = event.data.strip("{}")
    if os.path.isfile(file_path):
        threading.Thread(target=process_path, args=(file_path,)).start()


# --- GUI setup ---
root = TkinterDnD.Tk()


def resource_path(relative_path):
    """Работи както при разработка, така и в .exe файл"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


icon_path = resource_path("icon.ico")
if os.path.exists(icon_path):
    root.iconbitmap(default=icon_path)

try:
    logo_path = resource_path("logo.png")
    logo_image = Image.open(logo_path).resize((350, 250), Image.Resampling.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo, bg="#f5f5f5")
    logo_label.image = logo_photo
    logo_label.place(x=210, y=270)
except Exception as e:
    print("Logo not loaded:", e)

root.title("Speech to Text Converter")
root.geometry("800x500")
root.configure(bg="#f5f5f5")
root.resizable(False, False)

# --- Enable drag and drop ---
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

# --- Styling ---
style = ttk.Style()
style.theme_use("default")

style.configure("Custom.TButton",
                background="#4CAF50",
                foreground="white",
                font=("Segoe UI", 10, "bold"),
                padding=10
                )
style.map("Custom.TButton",
          background=[("active", "#45A049")]
          )

# --- Title ---
tk.Label(root, text="Speech to Text Converter", font=("Segoe UI", 16, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)
tk.Label(root, text="Select or drag an audio/video file to transcribe", font=("Segoe UI", 11), bg="#f5f5f5",
         fg="#555").pack()

# --- File Label ---
file_label = tk.Label(root, text="No file selected", font=("Segoe UI", 10), bg="#f5f5f5", fg="#888")
file_label.pack(pady=5)

# --- Select Button ---
ttk.Button(root, text="Select or Drop the File", command=select_file, style="Custom.TButton").pack(pady=10)

# --- Upload Progress ---
tk.Label(root, text="Progress:", font=("Segoe UI", 10, "bold"), bg="#f5f5f5", fg="#333").pack(pady=(25, 0))

style.configure("green.Horizontal.TProgressbar",
                troughcolor="#b6bfc1",
                background="#00ceff")

load_bar = ttk.Progressbar(root, orient="horizontal",
                           length=490,
                           mode="determinate",
                           style="green.Horizontal.TProgressbar")
load_bar.pack()
load_label = tk.Label(root, text="0%", font=("Segoe UI", 10), bg="#f5f5f5", fg="#333")
load_label.pack()

# --- Info Message ---
info_text = (
    "The file is currently being processed. Please do not close the application.\n"
    "Processing time may vary depending on the file size and system performance.\n"
    "Once transcription is complete, you will be prompted to choose where to save the extracted text."
)
tk.Label(
    root,
    text=info_text,
    font=("Segoe UI", 10),
    bg="#f5f5f5",
    fg="#555",
    justify="left",
    wraplength=500
).pack(pady=(10, 3))

# --- Footer Separator ---
ttk.Separator(root, orient='horizontal').pack(fill='x', padx=33, pady=(100, 0))

# --- Footer ---
footer = tk.Label(
    root,
    text="© 2025 Pynexor Ltd. · All rights reserved.",
    font=("Segoe UI", 10),
    bg="#f5f5f5",
    fg="#aaa"
)
footer.pack(side="bottom", pady=10)

# --- Mainloop ---
root.mainloop()
