import tkinter as tk

def key_down(event):
    global key
    key = event.keysym
    #print(f"{key}キーが押されました")


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy
    delta = { #キー:押されているキー(key),値:移動幅リスト[x,y]　
        "w"    :[0, -20],
        "s" :[0, +20],
        "a" :[-20, 0],
        "d":[+20, 0],
        ""     :[0, 0],
    }
    cx, cy = cx+delta[key][0], cy+delta[key][1]
    canvas.coords("bird", cx, cy)
    root.after(100,main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk .Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    bird = tk.PhotoImage(file="fig/0.png")
    cx, cy =300, 400
    canvas.create_image(cx, cy, image=bird, tag="bird")
    
    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc() 
    root.mainloop()