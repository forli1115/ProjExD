import tkinter as tk
import maze_maker as mm


def key_down(event): 
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy, mx, my
    delta = { #キー:押されているキー(key),値:移動幅リスト[x,y]　
        "Up"   :[0, -1], "w":[0, -1], 
        "Down" :[0, +1], "s":[0, +1],
        "Left" :[-1, 0], "a":[-1, 0],
        "Right":[+1, 0], "d":[+1, 0],
    }
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0: #もし移動先が床なら
            my, mx = my+delta[key][1], mx+delta[key][0]
    except:
        pass

    cx, cy = mx*100+50, my*100+50
    canvas.coords("bird", cx, cy)

    root.after(100,main_proc)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    label = tk.Label(root, text="ゴールを目指そう!", 
            font=("Times New Roman", 40)
            )
    label.pack()

    canvas = tk .Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_bg = mm.make_maze(15, 9) #1:壁,0:床を表す二次元リスト
    mm.show_maze(canvas, maze_bg)
    
    start= tk.PhotoImage(file="fig/s.png") #スタートの設定、描画
    canvas.create_image(150, 150, image=start, tag="start")

    goal= tk.PhotoImage(file="fig/g.png") #ゴールの設定、描画
    canvas.create_image(1350, 750, image=goal, tag="goal")

    bird = tk.PhotoImage(file="fig/0.png") #こうかとんの描画
    mx, my =1, 1
    cx, cy =mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=bird, tag="bird")
    
    key = ""

    root.bind("<KeyPress>", key_down) #キーが押されたときにkey_down関数が実行
    root.bind("<KeyRelease>", key_up) #キーが離されたときにkey_up関数が実行

    main_proc() 
    root.mainloop() #ウィンドウを表示