import pygame
import random
import time

class UI:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.buttons = [f"{i+1}" for i in range(10)]
        self.current_buttons = random.sample(self.buttons, 4)
        self.gold = 0
        self.last_gold_update = time.time()
        self.last_button_update = time.time()
        self.start_time = time.time()

    def update(self):
        # Update gold every 0.3 seconds
        if time.time() - self.last_gold_update >= 0.3:
            self.gold += 1
            self.last_gold_update = time.time()
        
        # Update buttons every 30 seconds
        if time.time() - self.last_button_update >= 30:
            self.current_buttons = random.sample(self.buttons, 4)
            self.last_button_update = time.time()

    def draw(self, screen):
        # Draw gold counter in the top right corner
        font = pygame.font.SysFont(None, 36)
        gold_text = font.render(f"Gold: {self.gold}", True, (255, 255, 255))
        screen.blit(gold_text, (self.screen_width - 150, 10))
        
        # Draw selected buttons in the bottom center of the screen
        button_y = self.screen_height - 50
        start_x = self.screen_width // 2 - 100
        for i, button in enumerate(self.current_buttons):
            button_x = start_x + i * 50
            pygame.draw.rect(screen, (255, 255, 255), (button_x, button_y, 40, 30))
            button_text = font.render(button, True, (0, 0, 0))
            screen.blit(button_text, (button_x + 5, button_y + 5))

    def enemy_died(self):
        self.gold += 10
