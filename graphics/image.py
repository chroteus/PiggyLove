import pyglet, math

class ImageMixin:
    def new_image(self, path):
        image = pyglet.image.load(path) #returns: instance of AbstractImage
        image.sprite = pyglet.sprite.Sprite(image, x=0,y=0, subpixel=True)

        return image

    def draw(self, drawable, x,y, angle=0, scale_x=1,scale_y=1, offset_x=0,offset_y=0):
        if drawable.__class__.__name__ == "Sprite":
            drawable.anchor_x = offset_x
            drawable.anchor_y = offset_y
            drawable.sprite.rotation = angle*(180/math.pi) #convert radian angle to degrees as pyglet wants
            drawable.sprite.scale_x = scale_x
            drawable.sprite.scale_y = scale_y

            drawable.sprite.draw(x,y)
