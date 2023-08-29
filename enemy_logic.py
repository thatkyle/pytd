from math import atan2, cos, sin, sqrt
import random
from pgzero.rect import Rect
import tower

def draw_enemies(screen, enemies):
    for enemy in enemies:
        screen.draw.filled_circle((enemy['x'], enemy['y']), 20, 'red')

        health_width = 40 * (enemy['health'] / 100.0)
        screen.draw.filled_rect(Rect(enemy['x'] - 20, enemy['y'] - 30, health_width, 5), 'green')

def update_enemies(enemies, center_x, center_y, gold):
    
    for enemy in enemies[:]:
        angle = atan2(center_y - enemy['y'], center_x - enemy['x'])
        enemy['x'] += enemy['speed'] * cos(angle)
        enemy['y'] += enemy['speed'] * sin(angle)

        distance = sqrt((center_x - enemy['x'])**2 + (center_y - enemy['y'])**2)

        if distance < 50:
            tower.tower_health -= 10
            enemies.remove(enemy)

        if enemy['health'] <= 0:
            enemies.remove(enemy)
            gold += 10

def create_enemy(WIDTH, HEIGHT):
    side = random.choice(['top', 'bottom', 'left', 'right'])
    
    if side == 'top':
        x, y = random.randint(0, WIDTH), 0
    elif side == 'bottom':
        x, y = random.randint(0, WIDTH), HEIGHT
    elif side == 'left':
        x, y = 0, random.randint(0, HEIGHT)
    elif side == 'right':
        x, y = WIDTH, random.randint(0, HEIGHT)

    speed = 2
    health = 100
    
    return {'x': x, 'y': y, 'speed': speed, 'health': health}
