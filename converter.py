from font import Font, FontLoader

def getText():
    return 'Git'

class TextDrawer:
    def setFont(self, font):
        pass

    def draw(self, text):
        pass
        
text = getText()
font = FontLoader().loadFont('fancyFont/')
d = TextDrawer()
d.setFont(font)
d.draw(text)
