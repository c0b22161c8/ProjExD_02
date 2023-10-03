import sys
import pygame as pg
from random import randint


WIDTH, HEIGHT = 1600, 900


key_dct = {pg.K_UP:(0,-5), pg.K_DOWN:(0,5), pg.K_LEFT:(-5,0), pg.K_RIGHT:(5,0)}


def check_round(rect:pg.Rect):
    """
    画面外かどうかの判定
    戻り値 タプル
    """
    yoko = tate = True
    if rect.left < 0 or WIDTH < rect.right:
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom:
        tate = False
    return yoko,tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img2 = pg.transform.flip(kk_img, True, False)
    kk_img_lst = {(-5,0):pg.transform.rotozoom(kk_img, 0, 2.0),
                  (-5,-5):pg.transform.rotozoom(kk_img, 315, 2.0),
                  (0,-5):pg.transform.rotozoom(kk_img2, 90, 2.0),
                  (5,-5):pg.transform.rotozoom(kk_img2, 45, 2.0),
                  (5,0):pg.transform.rotozoom(kk_img2, 0, 2.0),
                  (5,5):pg.transform.rotozoom(kk_img2, 315, 2.0),
                  (0,5):pg.transform.rotozoom(kk_img2, 270, 2.0),
                  (-5,5):pg.transform.rotozoom(kk_img, 45, 2.0),
                  (0,0):pg.transform.rotozoom(kk_img, 0, 2.0)}
    k_rect = (kk_img.get_rect())
    k_rect.center=(900, 400)
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

        if k_rect.colliderect(c_rect):
            print("ゲームオーバー")
            return

        screen.blit(bg_img, [0, 0])
        c_rect.move_ip(vx,vy)
        yoko,tate = check_round(c_rect)
        if not yoko: vx *= -1
        if not tate: vy *= -1
        key_lst = pg.key.get_pressed()
        total_move = [0,0]
        for key, move in key_dct.items():
            if key_lst[key]:
                total_move[0] += move[0]
                total_move[1] += move[1]
        k_rect.move_ip(total_move)
        if check_round(k_rect) != (True,True):
            k_rect.move_ip(-total_move[0],-total_move[1])
        screen.blit(kk_img_lst[tuple(total_move)], k_rect)
        screen.blit(draw_c, c_rect)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()