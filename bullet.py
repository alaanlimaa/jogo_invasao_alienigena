import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # Uma classe que administra projéteis disparados pela espaçonave

    def __init__(self, config, tela, nave):
        """Uma classe que administra projéteis disparados pela espaçonave"""
        super().__init__()
        self.tela = tela
        self.rect = pygame.Rect(0, 0, config.bullet_width, config.bullet_height)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top
        self.y = float(self.rect.y)  # Armazena a posição do projétil como um valor decimal
        self.color = config.bullet_color
        self.speed_factor = config.bullet_speed_factor

    """Move o projétil para cima na tela."""
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y


    """Desenha o projétil na tela."""
    def draw_bullet(self):
        pygame.draw.rect(self.tela, self.color, self.rect)







