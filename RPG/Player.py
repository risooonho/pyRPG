import pygame

class Player:
    name = 'Player'
    position = {'x': 100, 'y': 100}
    direction = 'down'

    SPEED_MULTIPLIER = 3 #movement to sprite frame speed multiplier
    SPEED_WALK = 5
    
    speed = 0

    def __init__(self, name, sprite):
        self.name = name
        self.sprite = sprite

    def render(self, screen):
        screen.blit(self.sprite.get_frame(), (self.position['x'], self.position['y']))

    def set_speed(self, speed):
        self.speed = speed
        self.sprite.speed = speed * self.SPEED_MULTIPLIER

    def go_up(self):
        self.direction = 'up'
        self.set_speed(self.SPEED_WALK)
        self.sprite.set_animation('up')
        self.position['y'] -= self.speed

    def go_down(self):
        self.direction = 'down'
        self.set_speed(self.SPEED_WALK)
        self.sprite.set_animation('down')
        self.position['y'] += self.speed

    def go_left(self):
        self.direction = 'left'
        self.set_speed(self.SPEED_WALK)
        self.sprite.set_animation('left')
        self.position['x'] -= self.speed

    def go_right(self):
        self.direction = 'right'
        self.set_speed(self.SPEED_WALK)
        self.sprite.set_animation('right')
        self.position['x'] += self.speed

    def stop(self):
        self.set_speed(0)
        self.sprite.set_animation(self.direction, True)
