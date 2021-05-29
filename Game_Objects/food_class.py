from Game_Objects.collectable_class import Collectable


class Food(Collectable):
    def __init__(self, window, char: chr = '◉', color_pair: int = 1):
        super().__init__(window, char, color_pair)
