import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm

class DeathB_window:
    def __init__(self):
    #ゲームオーバーと表示する
        tkm.showerror("Game Over", "こうかとんと爆弾が接触しました")
    #生存時間を表示する
        time = pg.time.get_ticks()
        time = time / 1000
        tkm.showinfo("time",f"生存時間は{time}秒でした")

class DeathE_window:
    def __init__(self):
    #ゲームオーバーと表示する
        tkm.showerror("Game Over", "こうかとんが敵に淘汰されました")
    #生存時間を表示する
        time = pg.time.get_ticks()
        time = time / 1000
        tkm.showinfo("time",f"生存時間は{time}秒でした")

class Kill_window: 
    def __init__(self):
    #ゲームクリアと表示する
        tkm.showinfo("Game Clear!","こうかとんが敵を排除しました")
    #クリアタイムを表示する
        time = pg.time.get_ticks()
        time = time / 1000
        tkm.showinfo("time",f"クリアタイムは{time}秒でした")



class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)       # Surface
        self.rct = self.sfc.get_rect()           # Rect
        self.bgi_sfc = pg.image.load(image)      # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()   # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird: #こうかとんの描画、設定
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy   #こうかとん表示

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP] or key_states[pg.K_w]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN] or key_states[pg.K_s]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT] or key_states[pg.K_a]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT] or key_states[pg.K_d]: 
            self.rct.centerx += 1
        
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP] or key_states[pg.K_w]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN] or key_states[pg.K_s]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT] or key_states[pg.K_a]:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT] or key_states[pg.K_d]:
                self.rct.centerx -= 1
        self.blit(scr)

    def attack(self):
        return Shot(self, (+1,+0))


class Bomb: #爆弾の描画、設定
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0))   #黒い部分を透明化
        pg.draw.circle(self.sfc, color, (size, size), size)   #円形の爆弾を作る
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)   #スタート位置をランダムにする
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy 

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)   #爆弾移動
        yoko, tate = check_bound(self.rct, scr.rct)   #こうかとんと爆弾が画面外に出ないようにする
        self.vx *= yoko
        self.vy *= tate
        
        self.blit(scr)


class Shot: #ビームの描画、設定
    def __init__(self, chr: Bird, vxy):
        self.sfc = pg.image.load("fig/beam.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.1) # Surface
        self.rct = self.sfc.get_rect()
        self.rct.midleft = chr.rct.center
        self.vx, self.vy = vxy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)

        self.blit(scr)

        


class Enemy: #敵キャラを描画、設定
    def __init__(self, image: str, size: float, vxy, scr: Screen):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)   #スタート位置をランダムにする
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)   
        yoko, tate = check_bound(self.rct, scr.rct)   #敵キャラが画面外に出ないようにする
        self.vx *= yoko
        self.vy *= tate
        
        self.blit(scr)


        
def main():
    clock = pg.time.Clock()
    
    #Screenクラスのインスタンス
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    #Birdクラスのインスタンス
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    #Bombクラスのインスタンス
    bkd = Bomb((255, 0, 0), 10, (+1,+1), scr)
    #Bomb2クラスのインスタンス
    bkd2 = Bomb((0, 255, 0), 15, (+1, +1), scr)
    #Enemyクラスのインスタンス
    nme = Enemy("fig/nme01.png", 0.5, (+1,+1), scr)
    #Shotクラスのインスタンス
    beam = Shot(kkt, (+1,+0))
    
    
    while True:
        scr.blit()   

        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                beam = kkt.attack()

        #各インスタンスのアップデート
        kkt.update(scr)   
        bkd.update(scr)
        bkd2.update(scr)
        nme.update(scr)
        beam.update(scr)

        
        if kkt.rct.colliderect(bkd.rct): #爆弾と衝突したとき
            DeathB_window()
            return
        
        if kkt.rct.colliderect(bkd2.rct): #爆弾2と衝突したとき
            DeathB_window()
            return

        if kkt.rct.colliderect(nme.rct): #敵キャラと衝突したとき
            DeathE_window()
            return

        if beam.rct.colliderect(nme.rct): #ビームが敵キャラと衝突したとき            gameclear()
            Kill_window()
            return
    

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw() #不要なウィンドウの削除
    pg.init()
    main()
    pg.quit()
    sys.exit()