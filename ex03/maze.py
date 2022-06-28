import tkinter as tk



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk .Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    bird = tk.PhotoImage(file="fig/0.png")
    cx, cy =300, 400
    canvas.create_image(cx, cy, image=bird, tag="bird")
    
    root.mainloop()