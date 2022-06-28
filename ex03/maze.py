import tkinter as tk
import maze_maker as mm


def key_down(event): 
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy
    delta = { #キー:押されているキー(key),値:移動幅リスト[x,y]　
        "Up"   :[0, -20],
        "Down" :[0, +20],
        "Left" :[-20, 0],
        "Right":[+20, 0],
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

    maze_bg = mm.make_maze(15, 9)
    print(maze_bg)

    bird = tk.PhotoImage(file="fig/0.png") #こうかとんの描画
    cx, cy =300, 400 #初期位置の設定
    canvas.create_image(cx, cy, image=bird, tag="bird")
    
    key = ""

    root.bind("<KeyPress>", key_down) #キーが押されたときにkey_down関数が実行
    root.bind("<KeyRelease>", key_up) #キーが離されたときにkey_up関数が実行

    main_proc() 
    root.mainloop() #ウィンドウを表示