from elements import elements

def weapon_factory(name, element_type, base_damage, attack_range, attack_speed, attack_type, projectile_speed, projectile_model, 
                  projectile_size, gold_cost):
    if element_type not in elements:
        raise ValueError("Invalid element type")
    
    if attack_type not in ['splash', 'single target', 'bounce', 'aura']:
        raise ValueError("Invalid attack type")

    weapon = {
        'name': name,
        'element_type': element_type,
        'base_damage': base_damage,
        'attack_range': attack_range,
        'attack_speed': attack_speed,
        'attack_type': attack_type,
        'color_code': elements[element_type]['color_code'],
        'projectile_speed': projectile_speed,
        'projectile_model': projectile_model,
        'projectile_size': projectile_size,
        'gold_cost': gold_cost
    }

    return weapon
