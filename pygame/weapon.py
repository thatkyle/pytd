from elements import elements
from constants import *
from math import atan2, sqrt, cos, sin

class Weapon:
    def __init__(self, name, element_type, base_damage, attack_range, attack_speed, attack_type,
                projectile_speed, projectile_model, projectile_size, gold_cost, 
                x = SCREEN_WIDTH // 2, y = SCREEN_HEIGHT // 2, angle = 0):
        self.x = x
        self.y = y
        self.angle = angle
        self.name = name
        self.element_type = element_type
        self.base_damage = base_damage
        self.attack_range = attack_range
        self.attack_speed = attack_speed
        self.attack_type = attack_type
        self.color_code = elements[element_type]['color_code']
        self.damage = self.base_damage
        self.projectile_speed = projectile_speed
        self.projectile_model = projectile_model
        self.projectile_size = projectile_size
        self.gold_cost = gold_cost
        self.strong_against = elements[element_type]['strong_against']
        self.weak_against = elements[element_type]['weak_against']
    
    def draw_weapon(self, screen):
        screen.draw.filled_circle((self.x, self.y), 5, self.color_code)
    
    def face_enemy(self, enemies):
        enemies_in_range = [e for e in enemies if sqrt((self.x - e['x'])**2 + (self.y - e['y'])**2) <= self.attack_range]
        if not enemies_in_range:
            return
        closest_enemy = min(enemies_in_range, key=lambda e: sqrt((self.x - e['x'])**2 + (self.y - e['y'])**2))
        self.angle = atan2(closest_enemy['y'] - self.y, closest_enemy['x'] - self.x)
    
    def spawn_weapon(self, weapons):
        weapons.append({'x': self.x, 'y': self.y, 'speed': self.projectile_speed, 'angle': self.angle, 'model': self.projectile_model, 'size': self.projectile_size})

    def load_model(self):
        # load model with matching shape/model, color and size from images file (need to load images file first)
        pass
    
    def update_weapon(self, enemies):
        self['x'] += self['speed'] * cos(self['angle'])
        self['y'] += self['speed'] * sin(self['angle'])

        for enemy in enemies[:]:
            distance = sqrt((self['x'] - enemy['x']) ** 2 + (self['y'] - enemy['y']) ** 2)
            if distance < 20:
                if enemy['element_type'] == self['strong_against']:
                    self['damage'] *= 1.5
                elif enemy['element_type'] == self['weak_against']:
                    self['damage'] *= 0.5
                enemy['health'] -= self['damage']
                self = None
                break  # A weapon can only hit one enemy
        
    
class WeaponManager:
    def __init__(self):
        self.weapons = []
    
    def remove_weapons(self):
        self.weapons = [w for w in self.weapons if w is not None]   
    
    def update_weapons(self):
        pass