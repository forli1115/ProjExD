import pygame as pg
import sys


def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ!こうかとん")
    screen_sfc = pg.display.set_mode((1600,900)) #Serface
    screen_rct = screen_sfc.get_rect()           #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")   #Surface
    bgimg_rct = bgimg_sfc.get_rect()             #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)
    
    

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)


        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        pg.display.update() #画面を更新する
        clock.tick(1000)

if  __name__ == "__main__":
    pg.init()
    main() 
    pg.quit()
    sys.exit()