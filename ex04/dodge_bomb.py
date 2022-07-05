import pygame as pg
import sys
import random

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
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
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
        if key_states[pg.K_UP]    == True: kkimg_rct.centery -= 1 
        if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -= 1
        if key_states[pg.K_DOWN]  == True: kkimg_rct.centery += 1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1
        screen_sfc.blit(kkimg_sfc, kkimg_rct) #screen Surfaceにkkimg_sfc Surfaceをkkimg_rctに従って張り付ける

        #練習５
        screen_sfc.blit(bmimg_sfc, bmimg_rct) #screen Surfaceにbmimg_sfc Surfaceをbmimg_rctに従って張り付ける

        #練習６
        bmimg_rct.move_ip(vx, vy)


        pg.display.update() #画面を更新する
        clock.tick(1000)

if  __name__ == "__main__":
    pg.init()
    main() 
    pg.quit()
    sys.exit()