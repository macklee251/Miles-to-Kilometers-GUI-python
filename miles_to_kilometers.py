from curses import window
from doctest import master
from importlib.metadata import entry_points
import tkinter as tk # Provides the basic logic
from tkinter import Entry, ttk # Provides all the widgets
import ttkbootstrap as ttk
from turtle import left
from psutil import boot_time
from sympy import Float

def convert():
    mile_input:Float = float(entry.get())
    km_output:str = str(mile_input*1.61)
    output_string.set(km_output + ' km')


# Window
window = ttk.Window(themename='journal')
window.title('Converter')
window.geometry('300x150')

# Title
title_label = ttk.Label(master=window, 
                        text='Miles to kilometers', 
                        font='Calibre 24 bold')
title_label.pack()

# Input field
input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# Output label
output_string = tk.StringVar()
output_label = ttk.Label(master=window, 
                         text='output', 
                         font='Calibre 24',
                         textvariable=output_string)
output_label.pack(pady=5)


# Run
window.mainloop()