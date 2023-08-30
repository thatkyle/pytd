import pygame
import random
import time
from ui_styles import STYLES

class UI:
    def __init__(self, screen_width, screen_height, shop_number_of_items):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.shop_number_of_items = shop_number_of_items
        self.buttons = [f"{i+1}" for i in range(10)]
        self.current_buttons = random.sample(self.buttons, self.shop_number_of_items)
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
            self.current_buttons = random.sample(self.buttons, self.shop_number_of_items)
            self.last_button_update = time.time()

    def draw(self, screen):
        # Draw gold counter in the top right corner
        font = pygame.font.SysFont(STYLES['base_font'], STYLES['gold_counter']['font_size'])
        gold_text = font.render(f"Gold: {self.gold}", True, STYLES['gold_counter']['font_color'])
        screen.blit(gold_text, STYLES['gold_counter']['abs_pos'])
        
        # Draw selected buttons in the bottom center of the screen
        button_y = self.screen_height - (STYLES['shop_button']['height'] + STYLES['shop_button']['bottom_margin'])

        # Calculate total width of all buttons plus the spacing between them
        total_width = self.shop_number_of_items * STYLES['shop_button']['width'] + (self.shop_number_of_items - 1) * STYLES['shop_button']['right_margin']

        # Calculate the starting x-coordinate to center the buttons
        start_x = (self.screen_width - total_width) // 2

        for i, button in enumerate(self.current_buttons):
            button_x = start_x + i * (STYLES['shop_button']['width'] + STYLES['shop_button']['right_margin'])
            pygame.draw.rect(screen, (255, 255, 255), (button_x, button_y, STYLES['shop_button']['width'], STYLES['shop_button']['height']))
            button_text = font.render(button, True, (0, 0, 0))
            screen.blit(button_text, (button_x + 5, button_y + 5))

    def enemy_died(self):
        self.gold += 10
