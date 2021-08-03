import pygame as pg
import game_functions as gf
from settings import Settings
from ship import Nave
from pygame.sprite import Group



def run_game():

    pg.init() # Iniciação do jogo e cria-se uma tela
    config = Settings()
    tela = pg.display.set_mode((config.tela_comprimento, config.tela_altura)) # Dimensional da tela em pixels
    pg.display.set_caption("Alien Invasion")
    nave = Nave(tela, config)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(config, tela, aliens) # Cria a frota de alienígenas

    while True:
        gf.update_tela(config, tela, nave, aliens, bullets)
        gf.check_events(config, tela, nave, bullets)
        nave.update()
        gf.update_bullets(bullets)



run_game()


