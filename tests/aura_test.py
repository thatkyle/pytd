import pgzrun
import math

# Screen dimensions
WIDTH = 1000
HEIGHT = 1000

# Initialize variables for controlling the pulse
pulse = 0
direction = 1  # 1 for increasing, -1 for decreasing
elapsed_time = 0

# Update function to update the pulse
def update(dt):
    global pulse, direction, pulse_speed, elapsed_time
    elapsed_time += dt
    pulse_speed = math.sin(elapsed_time) * .05

    pulse += direction * pulse_speed
    if pulse > 5 or pulse < 0:
        direction *= -1

# Draw function to draw the circle with glowing edge
def draw():
    screen.fill((0, 0, 0))  # Fill the screen with black

    for i in range(50):
        color = (255, 255, 255, int(255 * (i / 50.0)))
        r = 375 + pulse  # Radius of the circle
        screen.draw.filled_circle((WIDTH//2, HEIGHT//2), r, color)
    screen.draw.filled_circle((WIDTH//2, HEIGHT//2), 370, (0,0,0))

pgzrun.go()
