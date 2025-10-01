import py5
r = 40
x=10
y=10
dx=10
dy=10
def setup(): 

    py5.size(800, 600) 
    py5.no_stroke() 

def draw(): 

    global x, y, dx, dy
    py5.background(255)


    x += dx
    y += dy


    if x - r < 0:
        x = r
        dx *= -1
    elif x + r > py5.width:
        x = py5.width - r
        dx *= -1


    if y - r < 0:
        y = r
        dy *= -1
    elif y + r > py5.height:
        y = py5.height - r
        dy *= -1


    py5.fill(200, 120, 40)
    py5.ellipse(x, y, r * 2, r * 2)



    paused = False

def key_pressed(): 
    global x, y, dx, dy, paused 
    if py5.key == 'r' or py5.key == 'R': 
        x = py5.width / 2 
        y = py5.height / 2 
        if py5.key == ' ': 
            paused = not paused 
            py5.no_loop() if paused else py5.loop()

py5.run_sketch()