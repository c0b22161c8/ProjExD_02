import sys
import pygame as pg
from random import randint


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    draw_c = pg.Surface((20, 20))
    pg.draw.circle(draw_c, (255,0,0), (10,10), 10)
    draw_c.set_colorkey((0,0,0))
    c_rect = (draw_c.get_rect())
    clock = pg.time.Clock()
    tmr = 0
    x=randint(10, WIDTH)
    y=randint(10, HEIGHT)
    c_rect.center=(x,y)
    vx = vy = 5
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(draw_c, c_rect)
        c_rect.move_ip(vx,vy)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()