import pgzrun
import pygame
import math

WIDTH = 1000  # Width of the window
HEIGHT = 1000  # Height of the window

pulse = 0  # Initial pulse level
pulse_speed = 0.5  # Speed of the pulse
elapsed_time = 0  # Elapsed time since the start

def update(dt):
    global pulse, pulse_speed, elapsed_time

    # Calculate pulse using a combination of sine and exponential functions
    pulse = 5 * math.sin(2 * math.pi * elapsed_time * pulse_speed) * math.exp(-0.5 * elapsed_time) + 50

    elapsed_time += dt
    if elapsed_time > 2:
        elapsed_time = 0

def draw():
    screen.fill((0, 0, 0))  # Set the background color to black

    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    max_radius = min(WIDTH, HEIGHT) // 2  # Maximum radius of the circle

    for radius in range(max_radius, 0, -1):
        # Calculate the color for the current circle using a quadratic function
        color_value = int((1 - (radius / max_radius))**2 * 255)
        color = (color_value, 0, 0)

        # Draw the current circle
        pygame.draw.circle(screen.surface, color, (center_x, center_y), radius)
    
    for i in range(50):
        color = (0,0,0)
        r = max_radius - 200 + pulse  # Radius of the circle
        screen.draw.filled_circle((WIDTH//2, HEIGHT//2), r, color)
pgzrun.go()
