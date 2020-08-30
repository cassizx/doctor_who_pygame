class Settings():
    '''Класс для хранения всех настроек игры Alien Invasion'''
    def __init__(self):
        ''' Инициализирует настройки игры'''
        # Параметры экрана
        self.screen_width = 800
        self.screen_heigth = 850
        self.bg_color = (230,230,230)

        # Настройки корабля
        self.ship_speed_factor = 2.5