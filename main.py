import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Smart CCTV")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('960x720')  # Updated window size
window.configure(bg='#2e2e2e')  # Set window background color

frame1 = tk.Frame(window, bg='#2e2e2e')  # Set frame background color

label_title = tk.Label(frame1, text="Smart CCTV Camera", bg='#2e2e2e', fg='white')
label_font = font.Font(size=35, weight='bold', family='Helvetica')
label_title['font'] = label_font
label_title.grid(row=0, columnspan=3, pady=(10, 20))

icon = Image.open('icons/spy.png')
icon = icon.resize((150, 150), Image.LANCZOS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon, bg='#2e2e2e')
label_icon.grid(row=1, columnspan=3, pady=(5, 20))

btn2_image = Image.open('icons/rectangle-of-cutted-line-geometrical-shape.png')
btn2_image = btn2_image.resize((50, 50), Image.LANCZOS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50, 50), Image.LANCZOS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('icons/security-camera.png')
btn3_image = btn3_image.resize((50, 50), Image.LANCZOS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn6_image = Image.open('icons/incognito.png')
btn6_image = btn6_image.resize((50, 50), Image.LANCZOS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/recording.png')
btn4_image = btn4_image.resize((50, 50), Image.LANCZOS)
btn4_image = ImageTk.PhotoImage(btn4_image)

# --------------- Button -------------------#
btn_font = font.Font(size=25)
btn2 = tk.Button(frame1, text='Rectangle', height=90, width=180, fg='orange', command=rect_noise, compound='left', image=btn2_image, bg='#2e2e2e', activebackground='#3a3a3a', activeforeground='white')
btn2['font'] = btn_font
btn2.grid(row=2, column=0, padx=20, pady=10)

btn3 = tk.Button(frame1, text='Noise', height=90, width=180, fg='green', command=noise, image=btn3_image, compound='left', bg='#2e2e2e', activebackground='#3a3a3a', activeforeground='white')
btn3['font'] = btn_font
btn3.grid(row=2, column=1, padx=20, pady=10)

btn4 = tk.Button(frame1, text='Record', height=90, width=180, fg='orange', command=record, image=btn4_image, compound='left', bg='#2e2e2e', activebackground='#3a3a3a', activeforeground='white')
btn4['font'] = btn_font
btn4.grid(row=2, column=2, padx=20, pady=10)

btn6 = tk.Button(frame1, text='In Out', height=90, width=180, fg='green', command=in_out, image=btn6_image, compound='left', bg='#2e2e2e', activebackground='#3a3a3a', activeforeground='white')
btn6['font'] = btn_font
btn6.grid(row=3, column=0, columnspan=3, pady=10)

btn5 = tk.Button(frame1, height=90, width=180, fg='red', command=window.quit, image=btn5_image, bg='#2e2e2e', activebackground='#3a3a3a', activeforeground='white')
btn5['font'] = btn_font
btn5.grid(row=4, column=0, columnspan=3, pady=20)

frame1.pack()
window.mainloop()
