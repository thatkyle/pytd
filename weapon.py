from elements import elements
from constants import *
from math import atan2, sqrt, cos, sin
from weapon_definitions import all_weapons
import pygame

class Weapon:
    def __init__(self, name, element_type, base_damage, attack_range, attack_speed, attack_type,
                projectile_speed, projectile_model, projectile_size, gold_cost, 
                x = SCREEN_WIDTH // 2, y = SCREEN_HEIGHT // 2, angle = None):
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
        self.is_destroyed = False

    def draw_weapon(self, screen):
        pygame.draw.circle(screen, self.color_code, (self.x, self.y), 5)
    
    def fire_weapon(self, enemies):
        enemies_in_range = [e for e in enemies if sqrt((self.x - e.x)**2 + (self.y - e.y)**2) <= self.attack_range]
        # can only fire weapon if there is an enemy in range to target
        can_fire_weapon = len(enemies_in_range) > 0
        if can_fire_weapon == False:
            # can't add a new weapon until the existing weapon fires
            can_add_weapon = False
            # we return can_add_weapon to 1) notify WeaponManager that a new weapon can't be added, and 
            # 2) break out of the function before firing the weapon
            return can_add_weapon
        closest_enemy = min(enemies_in_range, key=lambda e: sqrt((self.x - e.x)**2 + (self.y - e.y)**2))
        self.angle = atan2(closest_enemy.y - self.y, closest_enemy.x - self.x)
        can_add_weapon = True
        return can_add_weapon
    
    # def spawn_weapon(self, weapons):
    #     weapons.append({'x': self.x, 'y': self.y, 'speed': self.projectile_speed, 'angle': self.angle, 'model': self.projectile_model, 'size': self.projectile_size})

    def load_model(self):
        # load model with matching shape/model, color and size from images file (need to load images files first)
        pass
    
    def update_weapon(self, enemies):
        self.x += self.projectile_speed * cos(self.angle)
        self.y += self.projectile_speed * sin(self.angle)

        if (self.x > SCREEN_WIDTH or self.x < 0 or self.y < 0 or self.y > SCREEN_HEIGHT):
            self.is_destroyed = True

        for enemy in enemies[:]:
            distance = sqrt((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2)
            if distance < 10:
                if enemy.element == self.strong_against:
                    self.damage *= 1.5
                elif enemy.element == self.weak_against:
                    self.damage *= 0.5
                enemy.current_health -= self.damage
                self.is_destroyed = True
                break  # A weapon can only hit one enemy
        
        
class WeaponManager:
    def __init__(self):
        self.weapons = []
        self.can_add_weapon = True

    def add_weapon(self):
        weapon = Weapon(
            all_weapons[0]['name'],
            all_weapons[0]['element_type'],
            all_weapons[0]['base_damage'],
            all_weapons[0]['attack_range'],
            all_weapons[0]['attack_speed'],
            all_weapons[0]['attack_type'],
            all_weapons[0]['projectile_speed'],
            all_weapons[0]['projectile_model'],
            all_weapons[0]['projectile_size'],
            all_weapons[0]['gold_cost']
        )
        self.weapons.append(weapon)
        return weapon.attack_speed
    
    def draw_weapons(self, screen):
        for weapon in self.weapons:
            weapon.draw_weapon(screen)
    
    def remove_weapons(self):
        self.weapons = [w for w in self.weapons if w.is_destroyed == False]

    def update_weapons(self, enemies):
        for weapon in self.weapons:
            if weapon.angle == None:
                self.can_add_weapon = weapon.fire_weapon(enemies)
            else:
                weapon.update_weapon(enemies)
