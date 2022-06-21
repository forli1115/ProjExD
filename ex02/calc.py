import tkinter as tk
import tkinter.messagebox as tkm
import math


def button_click(event): #ボタンがクリックされたときに実行される関数
    btn = event.widget
    num = btn["text"]
    eqn = entry.get()

    if num == "=": #計算結果を表示するイコールボタン
        res=eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    elif num == "C": #1文字消去するクリアボタン
        entry.delete(len(eqn)-1,tk.END)

    elif num == "AC": #すべて消去するオールクリアボタン
        entry.delete(0,tk.END)

    elif num == "%": #%(100で割った数)表示するパーセントボタン
        per=int(eqn)/100
        entry.delete(0,tk.END)
        entry.insert(tk.END,per)

    elif num == "!": #階乗計算をするファクトリアルボタン
        fact=math.factorial(int(eqn))
        entry.delete(0,tk.END)
        entry.insert(tk.END,fact)

    else: #数字を表示    
        entry.insert(tk.END,num)


if __name__ == "__main__":
    root=tk.Tk()
    root.title("電卓")
    
    entry=tk.Entry(root,justify="right",width=10,font=("Times New Roman", 40))#文字盤の作成
    entry.grid(row=0,column=0,columnspan=6)#横方向に6マス結合

    r,c=1,0   #r:行番号　c:列番号
    for i,num in enumerate(["AC","C","%","/",7,8,9,"*",4,5,6,"-",1,2,3,"+",0,".","!","="]): #表示ボタンの設定
        btn = tk.Button(root,
                        text = num,
                        width = 3,
                        height = 1,
                        font=("Times New Roman", 30)
                        )

        btn.bind("<1>",button_click)#<1>は左クリック
        btn.grid(row = r,column = c)
        c += 1
        if (i+1)%4 == 0:#4マスおきに改行
            r += 1
            c = 0
    

    root.mainloop()
