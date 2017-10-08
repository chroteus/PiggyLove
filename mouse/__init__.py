import pyglet
class Mouse:
    def __init__(self, parent):
        self.window = parent.window
        self.x = 0
        self.y = 0
    def on_mouse_motion(self, x,y, dx,dy):
        self.x = x
        self.y = self.window.height - y
