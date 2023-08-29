from init import InitGame
from enemy import EnemyManager
from tower import Tower
from ui import UI
from constants import *

class Game(InitGame):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'Tower Defense')
        self.enemy_manager = EnemyManager(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.tower = Tower(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.ui = UI(SCREEN_WIDTH, SCREEN_HEIGHT)
        
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

    def draw(self):
        self.screen.fill(BLACK)
        self.ui.draw(self.screen)
        self.tower.draw(self.screen)
        self.enemy_manager.draw_enemies(self.screen, RED)
