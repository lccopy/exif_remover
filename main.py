import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from functools import partial
import sv_ttk
from PIL import Image


def validation():
    """"Pressing 'OK' button launches main() function"""
    main()


def openfile(entry_box):
    """function working with tkinter to choose file"""
    global file
    file = filedialog.askopenfilename()
    entry_box.delete(0, tk.END)
    entry_box.insert(tk.END, file)


def app():
    """tk init and grids"""
    # tk init
    root = tk.Tk()
    root.title("EXIF REMOVER")
    width = 600
    height = 500
    root.geometry(f"{width}x{height}")
    frame = ttk.Frame(root)
    frame.grid()

    button_ok = ttk.Button(frame, command=validation, text="OK")
    file_selector = ttk.Frame(frame)
    file_entry = ttk.Entry(frame)
    ttk.Button(frame, text="Quit", command=root.destroy).grid(column=0,
                                                              row=0)  # quit
    select_button1 = ttk.Button(file_selector, text="Browse",
                                command=partial(openfile, file_entry))

    file_selector.grid(row=2, column=2)
    file_entry.grid(row=2, column=1)
    select_button1.grid(row=2, column=3)
    button_ok.grid(row=3, column=1)
    sv_ttk.set_theme("dark")
    root.mainloop()


def main():
    """exif remover"""
    print(file)
    image = Image.open(file)
    # strip exif
    data = list(image.getdata())
    image_wo_exif = Image.new(image.mode, image.size)
    image_wo_exif.putdata(data)
    image_wo_exif.save(f"{file}_no_exif.jpg")  # add "_no_exif.jpg" to the
                                               # end of the file w/o exif.
    print("Done")


if __name__ == "__main__":
    app()
