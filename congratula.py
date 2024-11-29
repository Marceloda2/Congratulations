import tkinter as tk
from pygame import mixer
import time
import threading

# Ruta al archivo de audio
AUDIO_FILE = r"C:/Users/marce/Downloads/Mac Miller - Congratulations (feat. Bilal).mp3"

# Letra con tiempos en segundos
LYRICS = [
    (0, "Where are you? 🌍"),
    (1.7, "Oh-oh 🎶"),
    (8.3, "Oh 💭"),
    (12.4, "\"The Divine Feminine, \" an album by Mac Miller ✨"),
    (15.9, "Oh-oh 🌙"),
    (21.24, "(\"The Divine Feminine\")"),
    (26.42, "Oh 💫"),
    (29.62, "Am I supposed to? Okay 🤔"),
    (34.72, "Love, love, love, love, love, love (sex ❤️‍🔥)"),
    (39.5, "Love, love, love, love, love, love, love (sex ❤️‍🔥)"),
    (44.64, "This sun don't shine when I'm alone 🌞"),
    (49.94, "I lose my mind and I lose control 🤯"),
    (53.88, "I see your eyes look through my soul 👀"),
    (57.82, "Don't be surprised this all I know 💡"),
    (61.16, "I felt the highs and they felt like you 🎢"),
    (65.0, "See, a love like mine is too good to be true 💕"),
    (68.92, "And you too divine to just be mine 🙏"),
    (72.74, "You remind me of the color blue 💙"),
    (76.58, "Girl, I'm so in love with you, yeah 💖"),
    (80.84, "Girl, I'm so in love with you 💖"),
]

# Función para reproducir la canción
def play_song():
    mixer.init()
    mixer.music.load(AUDIO_FILE)
    mixer.music.play()

# Función para mostrar la letra sincronizada
def show_lyrics():
    global start_time
    for timestamp, line in LYRICS:
        delay = timestamp - (time.time() - start_time)
        if delay > 0:
            time.sleep(delay)
        display_line(line)

# Función para mostrar una línea con estilos
def display_line(line):
    # Limpiar el texto actual
    label.config(text="")
    # Dividir las palabras
    words = line.split(" ")
    formatted_text = ""
    for word in words:
        if "sex" in word.lower():
            formatted_text += f"🔴 {word} 🔴 "
        elif "blue" in word.lower():
            formatted_text += f"🔵 {word} 🔵 "
        else:
            formatted_text += f"{word} "
    label.config(text=formatted_text.strip())

# Interfaz gráfica
root = tk.Tk()
root.title("Reproductor con Letra - Congratulations")
root.geometry("800x400")
root.configure(bg="black")

# Etiqueta para mostrar la letra centrada
label = tk.Label(
    root, 
    text="", 
    font=("Helvetica", 20), 
    wraplength=700, 
    fg="white", 
    bg="black", 
    justify="center",
)
label.place(relx=0.5, rely=0.5, anchor="center")  # Centrar completamente

# Iniciar reproducción de la canción y mostrar letra
start_time = time.time()
threading.Thread(target=play_song, daemon=True).start()
threading.Thread(target=show_lyrics, daemon=True).start()

root.mainloop()
