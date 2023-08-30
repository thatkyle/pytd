from math import sqrt, atan2

def spawn_weapon(weapon_data, enemies, tower_health):
    attack_range = weapon_data['attack_range']

    if enemies and tower_health > 0:
        # Filter enemies within the attack_range
        enemies_in_range = [e for e in enemies if sqrt((center_x - e['x'])**2 + (center_y - e['y'])**2) <= attack_range]

        # If there are no enemies within the attack range, don't do anything
        if not enemies_in_range:
            return

        # Find the closest enemy within the attack range
        closest_enemy = min(enemies_in_range, key=lambda e: sqrt((center_x - e['x'])**2 + (center_y - e['y'])**2))

        # Calculate the angle between the tower and the closest enemy
        angle = atan2(closest_enemy['y'] - center_y, closest_enemy['x'] - center_x)

        # Add the weapon projectile to the weapons list
        weapons.append({'x': center_x, 'y': center_y, 'speed': weapon_data['projectile_speed'], 'angle': angle})
