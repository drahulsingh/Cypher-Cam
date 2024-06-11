import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk
from find_motion import find_motion
from identify import maincall

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    
    if dark_mode:
        bg_color = "#333333"
        fg_color = "#FFFFFF"
        button_bg = "#555555"
        toggle_button.config(text="Light Mode")
    else:
        bg_color = "#FFFFFF"
        fg_color = "#000000"
        button_bg = "#DDDDDD"
        toggle_button.config(text="Dark Mode")
    
    window.config(bg=bg_color)
    frame1.config(bg=bg_color)
    label_title.config(bg=bg_color, fg=fg_color)
    label_icon.config(bg=bg_color)
    
    buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7]
    for button in buttons:
        button.config(bg=button_bg, fg=fg_color)

# Initialize the main window
window = tk.Tk()
window.title("CYPHER CAM")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x700')

dark_mode = False

frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="CYPHER CAM")
label_font = font.Font(size=35, weight='bold', family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10, 10), column=2)

icon = Image.open('icons/spy.png')
icon = icon.resize((150, 150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5, 10), column=2)

# Load images for buttons
btn1_image = Image.open('icons/lamp.png')
btn1_image = btn1_image.resize((50, 50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/rectangle-of-cutted-line-geometrical-shape.png')
btn2_image = btn2_image.resize((50, 50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn3_image = Image.open('icons/security-camera.png')
btn3_image = btn3_image.resize((50, 50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn4_image = Image.open('icons/rec.png')
btn4_image = btn4_image.resize((50, 50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50, 50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn6_image = Image.open('icons/incognito.png')
btn6_image = btn6_image.resize((50, 50), Image.ANTIALIAS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn7_image = Image.open('icons/main.png')
btn7_image = btn7_image.resize((50, 50), Image.ANTIALIAS)
btn7_image = ImageTk.PhotoImage(btn7_image)

# Button font
btn_font = font.Font(size=24)

# Create buttons
btn1 = tk.Button(frame1, text='Monitor', height=90, width=190, fg='green', command=find_motion, image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=3, pady=(20, 10))

btn2 = tk.Button(frame1, text='Rectangle', height=90, width=190, fg='orange', command=rect_noise, compound='left', image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20, 10), column=3, padx=(20, 5))

btn3 = tk.Button(frame1, text='Noise', height=90, width=190, fg='green', command=noise, image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=5, pady=(20, 10))

btn4 = tk.Button(frame1, text='Record', height=90, width=190, fg='orange', command=record, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20, 10), column=3)

btn6 = tk.Button(frame1, text='In Out', height=90, width=190, fg='green', command=in_out, image=btn6_image, compound='left')
btn6['font'] = btn_font
btn6.grid(row=5, pady=(20, 10), column=2)

btn5 = tk.Button(frame1, height=90, width=190, fg='red', command=window.quit, image=btn5_image)
btn5['font'] = btn_font
btn5.grid(row=6, pady=(20, 10), column=2)

btn7 = tk.Button(frame1, text="Identify", height=90, width=190, fg='orange', command=maincall, image=btn7_image, compound='left')
btn7['font'] = btn_font
btn7.grid(row=3, pady=(20, 10), column=2)

toggle_button = tk.Button(window, text="Dark Mode", command=toggle_dark_mode)
toggle_button.pack(side='top', anchor='ne', padx=10, pady=10)

frame1.pack()
window.mainloop()