from init import InitGame
from enemy import EnemyManager
from tower import Tower
from ui import UI
from constants import *
from shop import Shop
from weapon import Weapon, WeaponManager
import pygame

class Game(InitGame):
    getters = []
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'Tower Defense')
        # IMPORTANT - THE NEXT 2 LINES LOAD ALL OF THE GETTERS IN getters.py into self.get_... attributes (i.e. self.get_shop_number_of_item)
        for getter in Game.getters:
            setattr(self, getter.__name__, lambda getter=getter: getter(self))
        self.enemy_manager = EnemyManager(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.tower = Tower(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.shop = Shop()
        # self.get_shop_number_of_items, and all other self.get_... attributes come from getters.py and are set above by
        # for getter in Game.getters: setattr(self, getter.__name__, lambda getter=getter: getter(self)) for conciseness
        self.ui = UI(SCREEN_WIDTH, SCREEN_HEIGHT, self.get_shop_number_of_items)
        self.weapon_manager = WeaponManager()
        self.next_time_to_act = pygame.time.get_ticks()
        
    def update(self):
        self.ui.update()
        self.enemy_manager.spawn_enemy()
        self.enemy_manager.update_enemies()
        
        # Remove enemies with zero or less health
        for enemy in self.enemy_manager.enemies[:]:
            if enemy.current_health <= 0:
                self.enemy_manager.enemies.remove(enemy)
                self.ui.enemy_died()

        if self.tower is not None:
            for enemy in self.enemy_manager.enemies[:]:
                if abs(enemy.x - self.tower.x) < 5 and abs(enemy.y - self.tower.y) < 5:
                    self.tower.damage(10)
                    self.enemy_manager.enemies.remove(enemy)

            if self.tower.current_health <= 0:
                self.tower = None

        self.weapon_manager.update_weapons(self.enemy_manager.enemies)
        self.weapon_manager.remove_weapons()
        
    def draw(self):
        self.screen.fill(BLACK)
        self.ui.draw(self.screen)
        self.tower.draw(self.screen)
        self.enemy_manager.draw_enemies(self.screen)
        self.weapon_manager.draw_weapons(self.screen)
    
        current_time = pygame.time.get_ticks()
        if current_time >= self.next_time_to_act:
            attack_speed = self.weapon_manager.add_weapon(self.screen)
            self.next_time_to_act = current_time + attack_speed
