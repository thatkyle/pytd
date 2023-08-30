from game import Game

def add_getter(func):
    Game.getters.append(func)
    return func

@add_getter
def get_shop_number_of_items(game):
    return game.shop.number_of_items