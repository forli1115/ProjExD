import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm

def gameover():
    tkm.showerror("Game Over", "こうかとんと爆弾が接触しました")

def count_time():
    time = pg.time.get_ticks()
    time = time / 1000
    tkm.showinfo("time",f"生存時間は{time}秒でした")



def main():
    #練習１
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ!こうかとん")
    screen_sfc = pg.display.set_mode((1600,900)) #Serface
    screen_rct = screen_sfc.get_rect()           #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")   #Surface
    bgimg_rct = bgimg_sfc.get_rect()             #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)
    
    #練習３
    kkimg_sfc = pg.image.load("fig/9.png")       #Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0) #Surface
    kkimg_rct = kkimg_sfc.get_rect()             #Rect
    kkimg_rct.center = 900, 400

    
    #練習５:爆弾
    bmimg_sfc = pg.Surface((20, 20)) #Surface
    bmimg_sfc.set_colorkey((0, 0, 0))
    color1 = random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    pg.draw.circle(bmimg_sfc, (color1, color2, color3), (10, 10), 10)
    bmimg_rct = bmimg_sfc.get_rect() #Rect
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)

    


    #練習６
    vx, vy = +1, +1

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct) #screen Surfaceにbgimg_sfc Surfaceをbgimg_rctに従って張り付ける

        #練習２
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        #練習４
        key_states = pg.key.get_pressed() #辞書
        #矢印キー、w,a,s,dキーで上下左右に移動する
        if key_states[pg.K_UP]    or key_states[pg.K_w]  == True: kkimg_rct.centery -= 1 
        if key_states[pg.K_LEFT]  or key_states[pg.K_a]  == True: kkimg_rct.centerx -= 1
        if key_states[pg.K_DOWN]  or key_states[pg.K_s]  == True: kkimg_rct.centery += 1
        if key_states[pg.K_RIGHT] or key_states[pg.K_d]  == True: kkimg_rct.centerx += 1
        #練習７
        if check_bound(kkimg_rct, screen_rct) != (1, 1): #領域外だったら
            if key_states[pg.K_UP]    or key_states[pg.K_w] == True: kkimg_rct.centery += 1 
            if key_states[pg.K_LEFT]  or key_states[pg.K_a] == True: kkimg_rct.centerx += 1
            if key_states[pg.K_DOWN]  or key_states[pg.K_s] == True: kkimg_rct.centery -= 1
            if key_states[pg.K_RIGHT] or key_states[pg.K_d] == True: kkimg_rct.centerx -= 1
        screen_sfc.blit(kkimg_sfc, kkimg_rct) #screen Surfaceにkkimg_sfc Surfaceをkkimg_rctに従って張り付ける

        #練習６
        bmimg_rct.move_ip(vx, vy)
        
        #練習５
        screen_sfc.blit(bmimg_sfc, bmimg_rct) #screen Surfaceにbmimg_sfc Surfaceをbmimg_rctに従って張り付ける

        #練習７
        yoko, tate = check_bound(bmimg_rct,screen_rct)
        vx *= yoko
        vy *= tate
        
        #練習８
        if kkimg_rct.colliderect(bmimg_rct):
            gameover()
            count_time()
            return


        pg.display.update() #画面を更新する
        clock.tick(1000)


def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect    
    '''
    yoko, tate = +1, +1 #領域内
    #衝突判定
    if rct.left < scr_rct.left or scr_rct.right  < rct.right  : yoko = -1  
    if rct.top < scr_rct.top   or scr_rct.bottom < rct.bottom : tate = -1
    return yoko, tate

if  __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    pg.init()
    main() 
    pg.quit()
    sys.exit()



    