import pygame as pg
from pygame.sprite import Sprite


class Alien(Sprite):
    """Uma classe que representa um único alienígena da frota."""

    def __init__(self, config, tela):
        super(Alien, self).__init__()
        self.tela = tela
        self.config = config

        # Carrega a imagem do alienígena e define seu atributo
        self.imagem_alien = pg.image.load('imagens/alien1.png')
        self.rect = self.imagem_alien.get_rect()

        # Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alienígena em sua posição atual."""
        return self.tela.blit(self.imagem_alien, self.rect)

