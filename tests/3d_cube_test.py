import pygame
import math

pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Cube in Pygame")
clock = pygame.time.Clock()

# Cube vertices and edges
vertices = [
    [100, 100, 100],
    [100, 100, -100],
    [100, -100, -100],
    [100, -100, 100],
    [-100, 100, 100],
    [-100, 100, -100],
    [-100, -100, -100],
    [-100, -100, 100]
]

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4)
]

def project(x, y, z, scale, angle_x, angle_y):
    # Rotation in 3D
    x1 = x * math.cos(angle_y) - z * math.sin(angle_y)
    z1 = x * math.sin(angle_y) + z * math.cos(angle_y)
    y1 = y * math.cos(angle_x) - z1 * math.sin(angle_x)
    z1 = y * math.sin(angle_x) + z1 * math.cos(angle_x)
    
    # Perspective projection (assuming z1 is never -scale)
    x1 = x1 * scale / (z1 + scale)
    y1 = y1 * scale / (z1 + scale)
    
    # Translate to screen position
    x1 += width // 2
    y1 += height // 2
    
    return int(x1), int(y1)

def draw_cube():
    angle_x = 0
    angle_y = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        angle_x += 0.02
        angle_y += 0.03
        
        screen.fill((0, 0, 0))
        
        for edge in edges:
            x1, y1, z1 = vertices[edge[0]]
            x2, y2, z2 = vertices[edge[1]]
            x1, y1 = project(x1, y1, z1, 400, angle_x, angle_y)
            x2, y2 = project(x2, y2, z2, 400, angle_x, angle_y)
            
            pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2))
        
        pygame.display.update()
        clock.tick(60)

draw_cube()
