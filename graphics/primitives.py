import pyglet,math
_circle_angles = []
#use pre-computed angles to minimize usage of expensive trig functions
for i in range(201):
    x = math.cos(2*math.pi*(i/200))
    y = math.sin(2*math.pi*(i/200))
    _circle_angles.append((x,y))

class PrimitivesMixin:
    def polygon(self, mode, *vertices):
        if mode == "fill":
            mode = pyglet.gl.GL_POLYGON
        elif mode == "line":
            mode = pyglet.gl.GL_LINE_LOOP
        else:
            try:
                mode = getattr(pyglet.gl, mode)
            except AttributeError:
                print("GL Mode for primitives named " + mode + " does not exist!")

        vertices_num = int(len(vertices)/2)
        pyglet.graphics.draw(
            vertices_num,
            mode,
            ("v2f", vertices),
            ("c4B", self.current_color*vertices_num)
        )

    def rectangle(self, mode, x,y,width,height):
        self.polygon(mode, x+width,y, x,y,  x,y+height, x+width,y+height)

    def circle(self, mode, x,y, radius, segments=50):
        vertices = []
        if segments < len(_circle_angles):
            ratio = len(_circle_angles)/segments
            for i in range(segments):
                i = round(i*ratio)
                angle = _circle_angles[i]
                vx = x + radius*angle[0]
                vy = y + radius*angle[1]
                vertices.append(vx)
                vertices.append(vy)
        else:
            for i in range(segments):
                angle = 2*math.pi*(i/segments)
                vx = x + radius*math.cos(angle)
                vy = y + radius*math.sin(angle)
                vertices.append(vx)
                vertices.append(vy)

        self.polygon(mode, *vertices) #asterisk unpacks the list as args

    def line(self, *vertices):
        # "LINE" == pyglet.gl.LINE != pyglet.gl.LINE_LOOP (which is used for line polygons)
        self.polygon("LINE", *vertices)
