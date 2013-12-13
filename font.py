class Font:
    def __init__(self, name):
        self.name = name
        self.letters = {}

class FontLoader:
    def loadFont(self, directory):
        font = Font("fancy")

        font.letters['G'] = r" ____ \n(_  _)\n  )(  \n (__) \n"
        return font
