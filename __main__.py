import piggy_love
love = piggy_love.PiggyLove(width=900,height=900)

def load():
    pass

def update(dt):
    pass

def draw():
    love.graphics.set_color(200,20,20)
    love.graphics.circle("fill", 500,500, 100)

love.set_events(load,update,draw)
love.run()
