import tkinter as tk
import tkinter.font as font
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Progressbar
from dct_compresser import compress
import matplotlib.pyplot as plt
import time
import threading
import numpy as np

window = tk.Tk()
window.geometry("330x245")
window.title("Compresser")
window.resizable(False, False)
default_font = font.Font(family="Helvetica", size=12)


"""
Verifica il contenuto del risultato dell'elaborazione dell'immagine contenuto in im_compressed;
nel caso la variabile fosse stata popolata, esegue il plot delle immagini affiancate
"""
def observe_data():
    global im_compressed
    if len(im_compressed) != 0:
        set_progress_bar(False)
        compress_button.configure(state="normal")
        print("Plotting...")
        plot_image()
        im_compressed = []
    else:
        # Variabile vuota, rescheduling
        window.after(1000, observe_data)

def plot_image():
    im = plt.imread(img_path)
    fig, axis = plt.subplots(1,2)
    axis[0].imshow(im, cmap="gray")
    axis[0].set(title="Immagine originale")
    axis[1].imshow(im_compressed, cmap="gray")
    axis[1].set(title="Immagine compressa")
    plt.show()

"""
Esegue la compressione dell'immagine e salva il risultato in im_compressed
"""
def compress_threading():
    global im_compressed
    print("Compressione in corso ...")
    f = int(window_text_input.get())
    d = int(compress_text_input.get())
    im = plt.imread(img_path)
    im_compressed = compress(im, f, d)

"""
Apre finestra di dialogo per selezionare l'immagine
"""
def file_browser():
    global img_path
    window.filename = filedialog.askopenfilename(initialdir="./", title="Seleziona un'immagine", 
                                             filetype=(("BMP", "*.bmp"), ("All", "*.*")))
    img_path = str(window.filename)
    if img_path != "":
        tmp = img_path.split("/")
        img_name = tmp[len(tmp) - 1]
        img_name_label.configure(text=img_name)
        print(f"Immagine selezionata: {img_path}")


"""
Esegue la validazione dell'input e crea il thread per processare l'immagine
"""
def button_compress_clk():
    if check_input() != False:
        # Schedulazione observer
        window.after(1000, observe_data)
        compress_button.configure(state="disable")
        set_progress_bar(True)
        t = threading.Thread(target=compress_threading)
        t.start()

def check_input():
    if not(img_name_label.cget("text")):
        messagebox.showwarning(title="Attenzione", 
                               message="Seleziona un'immagine da comprimere")
        return False
    if not(window_text_input.get()):
        messagebox.showwarning(title="Attenzione", 
                               message="Inserisci la dimensione delle fainestra")
        return False
    if not(compress_text_input.get()):
        messagebox.showwarning(title="Attenzion", 
                               message="Inserisci il parametro di compressione d")
        return False

    f = int(window_text_input.get())
    d = int(compress_text_input.get())
    im = plt.imread(img_path)
    im_shape = np.shape(im)

    if f <= 0:
        messagebox.showerror(title="Errore", 
                             message="Dimesnione finestra non valida: inserire un valore maggiore di zero")
        return False
    if f > im_shape[0] or f > im_shape[1]:
        messagebox.showerror(title="Errore", 
                             message="Dimesnione finestra non valida: inserire un valore minore della dimensione dell'immagine")
        return False
    if d < 0 or d > (2*f - 2):
        messagebox.showerror(title="Errore", 
                             message="Parametro di compressione non valido: inserire un valore compreso tra zero e (2*f - 2)")
        return False
    return True


def set_progress_bar(visibility):
    if visibility == True:
        space_holder.grid_remove()
        progress_bar.grid(row=4, column=0, padx=5, pady=5, columnspan=2)
        progress_bar.start(10)
    else:
        space_holder.grid(row=4, column=0, padx=5, pady=5, columnspan=2)
        progress_bar.grid_remove()

select_label = tk.Label(window, text="Seleziona un'immagine", font=default_font)
select_label.grid(row=0, column=0, sticky="W", padx=10, pady=10)

search_button = tk.Button(text="Sfoglia", command=file_browser, font=default_font)
search_button.grid(row=0, column=1, sticky="W", padx=10, pady=10)

img_name_label = tk.Label(window, text = "")
img_name_label.grid(row=1, column=0, columnspan=2)

window_label = tk.Label(window, text="Dimensione finestra",font=default_font)
window_label.grid(row=2, column=0, sticky="W", padx=10, pady=10)

window_text_input = tk.Entry(font=default_font, width=3, justify="center")
window_text_input.grid(row=2, column=1, padx=10, pady=10)

compress_label = tk.Label(window, text="Parametro di compressione (d)",font=default_font)
compress_label.grid(row=3, column=0, sticky="W", padx=10, pady=10)

compress_text_input = tk.Entry(font=default_font, width=3, justify="center")
compress_text_input.grid(row=3, column=1, padx=10, pady=10)

progress_bar = tk.ttk.Progressbar(window, orient='horizontal', mode='indeterminate')

space_holder = tk.Label(window, text="")
space_holder.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

compress_button = tk.Button(text="Comprimi immagine", command=button_compress_clk, font=default_font, width=32)
compress_button.grid(row=5, column=0, padx=10, pady=10, columnspan=2, rowspan=2, sticky="S")

if __name__ == "__main__":   
    im_compressed = []
    window.mainloop()