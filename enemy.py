import pygame
import math
import random
import time
from constants import *

class Enemy:
    def __init__(self, x, y, speed=2.0, radius=10, max_health=100):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.max_health = max_health
        self.current_health = max_health

    def move_towards_center(self, center_x, center_y):
        dx = center_x - self.x
        dy = center_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance > 0:
            dx /= distance
            dy /= distance
            self.x += dx * self.speed
            self.y += dy * self.speed

    def draw_health_bar(self, screen):
        health_bar_length = self.radius * 2
        health_bar_height = 3
        fill = (self.current_health / self.max_health) * health_bar_length
        pygame.draw.rect(screen, RED, (self.x - health_bar_length // 2, self.y - self.radius - 6, health_bar_length, health_bar_height))
        pygame.draw.rect(screen, GREEN, (self.x - health_bar_length // 2, self.y - self.radius - 6, fill, health_bar_height))

    def damage(self, amount):
        self.current_health -= amount
        self.current_health = max(self.current_health, 0)  # prevent negative health


class EnemyManager:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.enemies = []
        self.last_enemy_spawn_time = 0

    def spawn_enemy(self):
        current_time = time.time()
        if current_time - self.last_enemy_spawn_time > 1:
            self.last_enemy_spawn_time = current_time

            if random.choice([True, False]):
                x = random.randint(0, self.screen_width)
                y = random.choice([0, self.screen_height])
            else:
                x = random.choice([0, self.screen_width])
                y = random.randint(0, self.screen_height)
            self.enemies.append(Enemy(x, y))

    def update_enemies(self):
        for enemy in self.enemies:
            enemy.move_towards_center(self.screen_width // 2, self.screen_height // 2)
    
    def draw_enemies(self, screen, color):
        for enemy in self.enemies:
            pygame.draw.circle(screen, color, (int(enemy.x), int(enemy.y)), enemy.radius)
            enemy.draw_health_bar(screen)
