import pgzrun
import tower
import enemy_logic
import weapon_logic

WIDTH = 640
HEIGHT = 480
enemies = []
center_x, center_y = WIDTH // 2, HEIGHT // 2
gold = 0

tower.initialize(WIDTH, HEIGHT)

def draw():
    screen.clear()
    if tower.tower_health > 0:
        tower.draw_tower(screen)
    enemy_logic.draw_enemies(screen, enemies) 
    weapon_logic.draw_weapons(screen)

    screen.draw.text(f"Gold: {gold}", topright=(WIDTH - 10, 10), fontsize=30, color="gold")

    button_rect = Rect(WIDTH // 2 - 50, HEIGHT - 60, 100, 50)
    screen.draw.filled_rect(button_rect, 'blue')
    screen.draw.text("+10 DMG\n-100G", center=(WIDTH // 2, HEIGHT - 60 + 25), fontsize=20, color='white')

def update():
    global gold
    tower.update_tower()
    enemy_logic.update_enemies(enemies, center_x, center_y, gold)
    weapon_logic.update_weapons(enemies)
                
def spawn_enemy():
    if tower.tower_health > 0:
        enemies.append(enemy_logic.create_enemy(WIDTH, HEIGHT))

def increase_gold():
    global gold  # Declare gold as global to modify it
    gold += 1

def on_mouse_down(pos, button):
    global gold  # Declare these as global to modify them

    if button == mouse.LEFT:
        x, y = pos
        button_rect = Rect(WIDTH // 2 - 50, HEIGHT - 60, 100, 50)

        if button_rect.collidepoint(x, y):
            if gold >= 100:  # Check if enough gold is available
                weapon_logic.increase_damage(10)
                gold -= 100

def call_spawn_weapon():
    weapon_logic.spawn_weapon(center_x, center_y, enemies)

# Schedule to spawn an enemy every 2 seconds
clock.schedule_interval(spawn_enemy, 2.0)
# Schedule to spawn a weapon every 0.5 seconds
clock.schedule_interval(call_spawn_weapon, 0.5)
# Schedule to increase gold every 0.3 seconds
clock.schedule_interval(increase_gold, 0.3)

pgzrun.go()
