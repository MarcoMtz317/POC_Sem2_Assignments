import tkinter as tk

live = 3 

root = tk.Tk()

frame = tk.Frame(root)

canvas = tk.Canvas(frame, width=600, height=400, bg="#AAAAFF")
frame.pack()
canvas.pack()
root.title("BREAKOUT")
root.mainloop()