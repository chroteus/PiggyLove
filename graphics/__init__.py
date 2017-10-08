from graphics import image, primitives
class Graphics(image.ImageMixin,primitives.PrimitivesMixin):
    def __init__(self, parent):
        self.parent = parent
        self.current_color = (255,255,255,255)

    def set_color(self, r,g,b,a=255):
        self.current_color = (r,g,b,a)
