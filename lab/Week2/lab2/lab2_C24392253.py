# Lab1 C24392253

import py5

mode = 0

def key_pressed():
    global mode
    if py5.key >= '0' and py5.key <= '9':
        mode = int(py5.key) - int('0')
        print(mode)


def setup():
    py5.size(720, 720)  

def draw():
    global mode
    print(mode)

    if mode == 0:
        py5.fill(30,240,70)
        py5.circle(py5.mouse_x, py5.mouse_y, 130)

    elif mode == 1:
        py5.fill(0,0,255)
        py5.rect(py5.mouse_x, py5.mouse_y, 200, 100)


py5.run_sketch()  
