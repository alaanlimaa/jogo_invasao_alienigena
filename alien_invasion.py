import pygame as pg
import game_functions as gf
from settings import Settings
from ship import Nave
from pygame.sprite import Group
from alien import Alien


def run_game():

    pg.init() # Iniciação do jogo e cria-se uma tela
    config = Settings()
    tela = pg.display.set_mode((config.tela_comprimento, config.tela_altura)) # Dimensional da tela em pixels
    pg.display.set_caption("Alien Invasion")
    nave = Nave(tela, config)
    bullets = Group()
    alien = Alien(config, tela)

    while True:
        gf.check_events(config, tela, nave, bullets)
        gf.update_tela(config, tela, nave, alien, bullets)
        nave.update()
        gf.update_bullets(bullets)


run_game()


