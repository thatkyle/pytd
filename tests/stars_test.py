import pgzrun
import random
import os
from pgzero.actor import Actor

# Constants
WIDTH = 1000
HEIGHT = 1000

# Load all star PNGs from the 'stars' directory
star_files = [f for f in os.listdir('images') if f.endswith('.png')]
stars = []

# Class to represent a star with properties
class Star:
    def __init__(self, image, x, y, angle_speed, move_speed):
        self.actor = Actor(image)
        self.actor.pos = (x, y)
        self.angle = 0
        self.angle_speed = angle_speed
        self.move_speed = move_speed
        self.move_direction = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])

# Initialize random stars
for _ in range(50):  # Initialize 5 stars, change this number to have more or fewer stars
    image = random.choice(star_files)
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    angle_speed = random.uniform(2, 10)
    move_speed = random.uniform(1, 5)
    stars.append(Star(image, x, y, angle_speed, move_speed))

# Update the stars' positions and angles
def update():
    for star in stars:
        star.angle += star.angle_speed
        star.actor.angle = star.angle
        star.actor.x += star.move_speed * star.move_direction[0]
        star.actor.y += star.move_speed * star.move_direction[1]
        
        # Loop around the screen if the star goes out of bounds
        if star.actor.x > WIDTH:
            star.actor.x = 0
        elif star.actor.x < 0:
            star.actor.x = WIDTH

        if star.actor.y > HEIGHT:
            star.actor.y = 0
        elif star.actor.y < 0:
            star.actor.y = HEIGHT

# Draw the stars on the screen
def draw():
    screen.fill((0, 0, 0))  # Fill the screen with a black background
    for star in stars:
        star.actor.draw()

pgzrun.go()
