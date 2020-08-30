import pygame

class Background():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/bg1.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)