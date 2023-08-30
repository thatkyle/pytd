import pygame
from constants import *

class Tower:
    def __init__(self, x, y, radius=30, max_health=100):
        self.x = x
        self.y = y
        self.radius = radius
        self.max_health = max_health
        self.current_health = max_health

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)
        self.draw_health_bar(screen)

    def draw_health_bar(self, screen):
        health_bar_length = 50
        health_bar_height = 5
        fill = (self.current_health / self.max_health) * health_bar_length
        pygame.draw.rect(screen, RED, (self.x - health_bar_length // 2, self.y - self.radius - 10, health_bar_length, health_bar_height))
        pygame.draw.rect(screen, GREEN, (self.x - health_bar_length // 2, self.y - self.radius - 10, fill, health_bar_height))

    def damage(self, amount):
        self.current_health -= amount
        self.current_health = max(self.current_health, 0)  # prevent negative health
