import pygame as pg


class Nave():

    def __init__(self, tela, config):
        '''Inicia-se a espaçonave e a posição incial'''
        self.tela = tela
        self.config = config

        # Carrega a imagem da espaçonave e cria o retângulo
        self.imagem = pg.image.load('imagens/spaceship.png')
        self.rect = self.imagem.get_rect()
        self.tela_rect = tela.get_rect()

        # Inicia-se com a nave no centro da tela
        self.rect.centerx = self.tela_rect.centerx
        self.rect.bottom = self.tela_rect.bottom
        self.center = float(self.rect.centerx)

        # Movimentação da espaçonave
        self.moving_rigth = False
        self.moving_left = False


    def update(self, x=0):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento."""

        # Atualiza o valor de centro da espaçonave (Obs.: Ela sem começa em 0)
        if self.moving_rigth and self.rect.right < self.tela_rect.right:
            self.center += self.config.nave_speed_factor
        if self.moving_left and self.rect.left > x:
            self.center -= self.config.nave_speed_factor

        # Atualiza a posição da espaçonave
        self.rect.centerx = self.center

    def blitme(self):  # Desenha a respectiva nave em sua posição atual
        return self.tela.blit(self.imagem, self.rect)

