import tkinter as tk 
from tkinter import ttk 
import draw_overlay

def main():
    window = tk.Tk()
    window.geometry("115x50+50+40")                       # set window size and where it will appear
    window.title("Dim the light")                           # set title
    window.attributes('-topmost', True, "-toolwindow", 1)   # make window always on top 
    window.resizable(False, False)                          # disable window resize capability

    # create button
    button = ttk.Button(window, text="Start", command=draw_overlay.main)  # button will start the main function
    button.pack(pady=10)
    
    window.mainloop()

if __name__ == "__main__":
    main()