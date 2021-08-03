import sys
import pygame as pg
from bullet import Bullet
from alien import Alien


def check_events(config, tela, nave, bullets):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for eventos in pg.event.get():  # Quando mecher no teclado ou no mouse esse laço for será executado
        if eventos.type == pg.QUIT:  # Eventos do teclado e do mouse
            sys.exit()
        elif eventos.type == pg.KEYDOWN:
            check_keydown_events(eventos, config, tela, nave, bullets)
        elif eventos.type == pg.KEYUP:
            check_keyup_events(eventos, nave)


def check_keydown_events(evento, config, tela, nave, bullets):
    """Responde a pressionamentos de tecla."""
    if evento.key == pg.K_RIGHT:
        nave.moving_rigth = True
    elif evento.key == pg.K_LEFT:
        nave.moving_left = True
    elif evento.key == pg.K_SPACE:
        fire_bullet(config, tela, nave, bullets)
    elif evento.key == pg.K_q:
        sys.exit()


def check_keyup_events(evento, nave):
    """Responde a solturas de tecla."""
    if evento.key == pg.K_RIGHT:
        nave.moving_rigth = False
    elif evento.key == pg.K_LEFT:
        nave.moving_left = False


def update_tela(config, tela, nave, aliens, bullets):
    tela.fill(config.cor_fundo_tela)  # define a cor de funda da tela
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    nave.blitme()
    aliens.blitme()
    pg.display.flip() # Deixa a tela mais recente vísil, sempre criando novas imagens e excluindo a anterior, ilusão de movimentação


def update_bullets(bullets):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
    bullets.update()
    for bullet in bullets.copy():  # Livra-se dos projéteis que desapareceram
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(config, tela, nave, bullets):
    """Dispara um projétil se o limite ainda não foi alcançado."""
    if len(bullets) < config.bullets_allowed: # Cria um novo projétil e o adiciona ao grupo de projéteis.
        new_bullet = Bullet(config, tela, nave)
        bullets.add(new_bullet)


def create_fleet(config, tela, aliens):
    """Cria uma frota completa de alienígenas."""
    alien = Alien(config, tela)
    alien_width = alien.rect.width
    avaliable_space_x = config.tela_comprimento - (2 * alien_width)
    numbers_aliens_x = int(avaliable_space_x / (2 * alien_width))

    # Cria a primeira linha de alienígenas
    for alien_number in range(numbers_aliens_x):
        alien = Alien(config, tela)
        alien.x = (2 * alien_width) + alien_number
        alien.rect.x = alien.x
        aliens.add(alien)




