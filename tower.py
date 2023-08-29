from pygame import Rect

# Initialize tower-specific variables
center_x, center_y = None, None  # These will be set in initialize()
tower_health = 100

def initialize(width, height):
    global center_x, center_y
    center_x, center_y = width // 2, height // 2

# Draw the tower and its health
def draw_tower(screen):
    if tower_health > 0:
        screen.draw.filled_circle((center_x, center_y), 50, 'white')

        tower_health_width = 100 * (tower_health / 100.0)
        screen.draw.filled_rect(Rect(center_x - 50, center_y - 70, tower_health_width, 10), 'green')  # Use Rect

# Update the tower health
def update_tower():
    global tower_health
    if tower_health <= 0:
        tower_health = 0
