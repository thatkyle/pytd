import pygame
import math
import os
from elements import elements

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 30, 30
CX, CY = WIDTH // 2, HEIGHT // 2

# Initialize directory for saving PNGs
os.makedirs("stars", exist_ok=True)

# Function to draw a 20-pointed star
def draw_star(surface, x, y, color, points=20, radius=10):
    angle = 360 / points
    coords = []

    for i in range(points):
        theta = math.radians(i * angle)
        
        # Alternate between a shorter and longer distance from the center
        factor = 0.4 if i % 2 == 0 else 1
        
        x_coord = x + radius * factor * math.cos(theta)
        y_coord = y + radius * factor * math.sin(theta)
        
        coords.append((x_coord, y_coord))

    pygame.draw.polygon(surface, color, coords)

# Generate stars for each element
for element, attributes in elements.items():
    for radius in [10, 15, 20]:  # small, medium, large
        # Create a surface with transparency
        surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        
        # Draw the star
        draw_star(surface, CX, CY, attributes['color_code'], radius=radius)
        
        # Save as PNG
        filename = f"stars/{attributes['color_name'].lower()}_{radius}.png"
        pygame.image.save(surface, filename)
        print(f"Saved {filename}")
