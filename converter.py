def getText():
    return 'Git'

class Font:
    pass

class FontLoader:
    def loadFont(self, directory):
        pass
        
text = getText()
font = FontLoader().loadFont('fancyFont/')
d = TextDrawer()
d.setFont(font)
d.draw(text)
