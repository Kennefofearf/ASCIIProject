from item_module import Item


class Armor(Item):

    def __init__(self):
        super().__init__()

        self.ac = 0
        self.slot = ""
