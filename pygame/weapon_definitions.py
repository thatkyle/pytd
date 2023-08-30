from weapon_factory import weapon_factory

all_weapons = []

# Air weapons
all_weapons.append(weapon_factory("Windfang", "Air", 100, 300, 1000, 'single target', 10, 'circle', 'small', 500))
all_weapons.append(weapon_factory("Zephyrblade", "Air", 40, 4, 0.8, 'splash', 15, 'triangle', 'small', 1000))
all_weapons.append(weapon_factory("Galeforce", "Air", 60, 5, 0.7, 'bounce', 20, 'star', 'medium', 2000))
all_weapons.append(weapon_factory("Tempeststrike", "Air", 100, 6, 0.5, 'splash', 25, 'square', 'medium', 5000))
all_weapons.append(weapon_factory("Cycloneshard", "Air", 160, 7, 0.4, 'aura', 30, 'hexagon', 'large', 10000))

# Fire weapons
all_weapons.append(weapon_factory("BlazeFury", "Fire", 25, 3, 1.0, 'single target', 10, 'circle', 'small', 500))
all_weapons.append(weapon_factory("CinderWing", "Fire", 40, 4, 0.8, 'splash', 15, 'triangle', 'small', 1000))
all_weapons.append(weapon_factory("Emberclaw", "Fire", 60, 5, 0.7, 'bounce', 20, 'star', 'medium', 2000))
all_weapons.append(weapon_factory("Pyroflame", "Fire", 100, 6, 0.5, 'splash', 25, 'square', 'medium', 5000))
all_weapons.append(weapon_factory("Infernite", "Fire", 160, 7, 0.4, 'aura', 30, 'hexagon', 'large', 10000))

# Water weapons
all_weapons.append(weapon_factory("Tidebreaker", "Water", 25, 3, 1.0, 'single target', 10, 'circle', 'small', 500))
all_weapons.append(weapon_factory("AquaScepter", "Water", 40, 4, 0.8, 'splash', 15, 'triangle', 'small', 1000))
all_weapons.append(weapon_factory("Oceanhorn", "Water", 60, 5, 0.7, 'bounce', 20, 'star', 'medium', 2000))
all_weapons.append(weapon_factory("Wavecrusher", "Water", 100, 6, 0.5, 'splash', 25, 'square', 'medium', 5000))
all_weapons.append(weapon_factory("Floodgate", "Water", 160, 7, 0.4, 'aura', 30, 'hexagon', 'large', 10000))

# Earth weapons
all_weapons.append(weapon_factory("Stoneheart", "Earth", 25, 3, 1.0, 'single target', 10, 'circle', 'small', 500))
all_weapons.append(weapon_factory("Rockmender", "Earth", 40, 4, 0.8, 'splash', 15, 'triangle', 'small', 1000))
all_weapons.append(weapon_factory("Terrashield", "Earth", 60, 5, 0.7, 'bounce', 20, 'star', 'medium', 2000))
all_weapons.append(weapon_factory("Quakehammer", "Earth", 100, 6, 0.5, 'splash', 25, 'square', 'medium', 5000))
all_weapons.append(weapon_factory("Mountainpeak", "Earth", 160, 7, 0.4, 'aura', 30, 'hexagon', 'large', 10000))

# Ice weapons
all_weapons.append(weapon_factory("Frostbite", "Ice", 25, 3, 1.0, 'single target', 10, 'circle', 'small', 500))
all_weapons.append(weapon_factory("Snowfall", "Ice", 40, 4, 0.8, 'splash', 15, 'triangle', 'small', 1000))
all_weapons.append(weapon_factory("Chillwind", "Ice", 60, 5, 0.7, 'bounce', 20, 'star', 'medium', 2000))
all_weapons.append(weapon_factory("Icetooth", "Ice", 100, 6, 0.5, 'splash', 25, 'square', 'medium', 5000))
all_weapons.append(weapon_factory("GlacierEdge", "Ice", 160, 7, 0.4, 'aura', 30, 'hexagon', 'large', 10000))

# Chaos weapons
all_weapons.append(weapon_factory("AbyssWing", "Chaos", 25, 3, 1.0, 'single target', 10, 'circle', 'small', 500))
all_weapons.append(weapon_factory("Voidlash", "Chaos", 40, 4, 0.8, 'splash', 15, 'triangle', 'small', 1000))
all_weapons.append(weapon_factory("Netherclaw", "Chaos", 60, 5, 0.7, 'bounce', 20, 'star', 'medium', 2000))
all_weapons.append(weapon_factory("Darkpulse", "Chaos", 100, 6, 0.5, 'splash', 25, 'square', 'medium', 5000))
all_weapons.append(weapon_factory("Eclipsion", "Chaos", 160, 7, 0.4, 'aura', 30, 'hexagon', 'large', 10000))
