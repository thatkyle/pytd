from math import cos, sin, atan2, sqrt
import tower

# Initialize weapon parameters
weapons = []
weapon_damage = 50

def spawn_weapon(center_x, center_y, enemies):
    if enemies and tower.tower_health > 0:
        closest_enemy = min(enemies, key=lambda e: sqrt((center_x - e['x']) ** 2 + (center_y - e['y']) ** 2))
        angle = atan2(closest_enemy['y'] - center_y, closest_enemy['x'] - center_x)
        weapons.append({'x': center_x, 'y': center_y, 'speed': 5, 'angle': angle})

def update_weapons(enemies):
    global weapon_damage

    # Update weapons and check for collision with enemies
    for weapon in weapons[:]:
        weapon['x'] += weapon['speed'] * cos(weapon['angle'])
        weapon['y'] += weapon['speed'] * sin(weapon['angle'])

        for enemy in enemies[:]:
            distance = sqrt((weapon['x'] - enemy['x']) ** 2 + (weapon['y'] - enemy['y']) ** 2)
            if distance < 20:
                enemy['health'] -= weapon_damage
                weapons.remove(weapon)
                break  # A weapon can only hit one enemy

def draw_weapons(screen):
    for weapon in weapons:
        screen.draw.filled_circle((weapon['x'], weapon['y']), 5, 'blue')

def increase_damage(amount):
    global weapon_damage
    weapon_damage += amount
