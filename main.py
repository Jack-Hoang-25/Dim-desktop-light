import tkinter  
from tkinter import *
from tkinter import ttk
import time
from pynput import mouse
 
dim_level = 0.85

def mouse_click1(x, y, button, pressed):      # first mouse click
    if pressed:
        global left_x, top_y
        left_x = x
        top_y = y
        return False                          # stop mouse.Listener after a click and get out of the loop

def mouse_click2(x, y, button, pressed):      # second mouse click
    if pressed:
        global right_x, bottom_y
        right_x = x
        bottom_y = y
        return False                          # stop mouse.Listener after a click and get out of the loop

def main():
    
    # wait to to start video
    time.sleep(2) 
 
    root = Tk()
    root.config(background="black")                                             # set background to black
    root.attributes("-alpha", dim_level)                                        # dim it to 85% since i don't know how to set canvas transparent

    # put the graphic on the topmost
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    screen_width = root.winfo_screenwidth()                                     # set window size to cover entire screen
    screen_height = root.winfo_screenheight()   
    root.geometry(f"{screen_width}x{screen_height}")   
    #root.attributes("-fullscreen", "true")                                     # alternative method for geometry..... need further test
    
    with mouse.Listener(on_click=mouse_click1) as listener:                     # wait for first mouse click to find left_x and top_y
        listener.join()
    with mouse.Listener(on_click=mouse_click2) as listener:                     # wait for second mouse click to find right_x and bottom_y
        listener.join()

    # bind ESC key and mouse to close the window
    root.bind('<Escape>', lambda event: root.quit())
    root.bind('<Button-1>', lambda event: root.quit())
    root.bind('<Button-3>', lambda event: root.quit())

    root.attributes("-transparentcolor", "red")                                 # set anything with red color will be see through, this will be for the video frame
    
    canvas = Canvas(root, width=screen_width, height=screen_height, borderwidth=0, highlightthickness=0, background="black")        # the canvas will act as the black overlay
    canvas.grid(sticky=(N, W, E, S))
    
    # Insert helping text to stop the program
    dynamic_font_size = int(screen_height/75)                                   # variable to change font size depending on the screen size
    canvas.create_text(10, 10, text='Click on black overlay to close', anchor='nw', font=('Arial', dynamic_font_size, 'bold'), fill='white')
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='red')      

    root.mainloop()


if __name__ == '__main__':
    main()
