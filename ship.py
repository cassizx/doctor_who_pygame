import pygame

class Tardis():
    def __init__(self,ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        # Иконка корабля
        self.image = pygame.image.load('images/tardis.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый карабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #self.rect.centery = self.screen_rect.centery
        # Сохранение вещественоой координаты центра корабля
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0: #and self.rect.top 
            self.rect.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom :
            self.rect.bottom += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
