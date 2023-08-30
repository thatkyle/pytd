# The get_ getter functions are loaded into the Game class in game.py and are used to
# facillitate passing attributes between classes. Any time you are reading data from
# one class in another class, you should define it here

from game import Game

def add_getter(func):
    Game.getters.append(func)
    return func

@add_getter
def get_shop_number_of_items(game):
    return game.shop.number_of_items