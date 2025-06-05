import tkinter as tk
from tkinter import ttk
 
dim_level = 0.8

def save_mouse_position(event, root, canvas, player_position, helper_text, user_font_size):
    player_position += [event.x, event.y]                     # save the choosen location for the video player box
    draw_video_player_box(root, canvas, player_position, helper_text, user_font_size)

def draw_video_player_box(root, canvas, player_position, helper_text, user_font_size):
    if len(player_position) == 4:                                # this will trigger after the press the second time         
        left_x, top_y, right_x, bottom_y = player_position
        canvas.delete(helper_text)
        canvas.create_text(10, 10, text="Click on black overlay to close", anchor="nw", font=("Arial", user_font_size, "bold"), fill="white")    # Insert helping text to stop the program
        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="red") 
        root.attributes("-alpha", dim_level)                    # dim it to 80% since i don't know how to set canvas transparent
        root.config(cursor="arrow")
        # bind ESC key and mouse to close the window
        root.bind("<Escape>", lambda event: root.quit())
        root.bind("<Button-1>", lambda event: root.quit())
        root.bind("<Button-3>", lambda event: root.quit())
    

def main():
    
    root = tk.Tk()
    root.config(background="black")                                             # set background to black
    root.attributes("-alpha", 0.4)                                              # dim background slightly 
    
    # put the graphic on the topmost
    root.overrideredirect(True)               
    root.attributes("-topmost", True)
    screen_width = root.winfo_screenwidth()                                     # set window size to cover entire screen
    screen_height = root.winfo_screenheight()   
    root.geometry(f"{screen_width}x{screen_height}")   
    #root.attributes("-fullscreen", "true")                                     # alternative method for geometry..... need further test
    
    root.attributes("-transparentcolor", "red")                                 # set anything with red color will be see through, this will be for the video frame
    canvas = tk.Canvas(root, width=screen_width, height=screen_height, borderwidth=0, highlightthickness=0, background="black")        # the canvas will act as the black background
    canvas.grid()
    user_font_size = int(screen_height/75)                                   # variable to change font size depending on the screen size.
    helper_text = canvas.create_text(10, 10, text="Click to define video box", anchor="nw", font=("Arial", user_font_size, "bold"), fill="white")
    player_position = []                                                       # player_pos have to be outside of the save_mouse_pos function so that it can run when len(player_pos) reaches 4
    canvas.bind("<Button-1>", lambda event: save_mouse_position(event, root, canvas, player_position, helper_text, user_font_size))
    root.config(cursor="crosshair")
    root.bind("<Escape>", lambda event: root.quit())                        #safety feature
    root.mainloop()


        

if __name__ == "__main__":
    main()
