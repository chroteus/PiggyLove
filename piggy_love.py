from graphics import *
from mouse import *
import pyglet

class PiggyLove:
    def __init__(self, **window_kwargs):
        self.window = pyglet.window.Window(**window_kwargs)

        # load separate modules
        self.graphics = Graphics(self)
        self.mouse = Mouse(self)

        # set events to be called by pyglet
        self.window.on_draw = self.on_draw
        self.window.on_mouse_motion = self.mouse.on_mouse_motion

    def on_draw(self):
        self.window.clear()
        self.draw()

    def run(self):
        self.load()
        pyglet.clock.schedule_interval(self.update, 1/60.0)
        pyglet.app.run()

    def set_events(self, *events):
        for event in events:
            setattr(self, event.__name__, event)
