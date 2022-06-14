import random
import datetime
from unittest import skip

# グローバル変数
target_char=10
missing_char=2
max_repete=5


def main():
    st=datetime.datetime.now() #時間の計測(開始)
    for i in range(max_repete):
        collect=shutudai()
        ans=kaitou(collect)
        if ans==1:
            break
    ed=datetime.datetime.now() #時間の計測(終了)
    print(f"所要時間:{(ed-st).seconds}秒かかりました")


def shutudai():
    az=[chr(c+65) for c in range(26)]

    #対象文字
    random_az=random.sample(az,target_char)
    print(f"対象文字:{random_az}")
    
    #欠損文字
    target_missing=random.sample(random_az,missing_char)
    #print(f"欠損文字:{target_missing}")

    #表示文字
    display_char=[c for c in random_az if c not in target_missing]
    print(f"表示文字:{display_char}")


def kaitou(collect):
    num=int(input("欠損文字はいくつあるでしょうか？:")) #欠損文字数の正誤
    if num != missing_char:
        print("不正解です。")
        return 0
    else:
        print("正解です。それでは具体的に欠損文字を1つずつ入力してください") #欠損文字の正誤
        for i in range(missing_char):
            c=input(f"{i+1}つ目の文字を入力してください:")
            if c != collect:
                print("不正解です。またチャレンジしてください")
                return 0
            collect.remove(c)
        print("正解です。ゲームを終了します") #完全解答
        return 1


if __name__ == "__main__":
    main()

