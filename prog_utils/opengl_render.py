import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import time

cube_list = []
counter = 0
cur_time = time.clock()
prev_time = 0
for x in range(0, 10):
    cube_list.append([])
    for y in range(0, 10):
        if random.randint(0, 1) == 1:
            cube_list[x].append(1)
        else:
            cube_list[x].append(0)

# The display() method does all the work; it has to call the appropriate
# OpenGL functions to actually display something.
def draw():
    global cube_list, prev_time, counter, cur_time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glClearColor(0.5, 0.5, 0.75, 0.0)
    cur_time = time.clock()
    interval = cur_time - prev_time
    counter += 1
    if interval > 1:
        print(counter)
        prev_time = cur_time
        counter = 0
    # glPushMatrix()
    glRotatef(0.1 , 1, 1, 1)
    for x, line in enumerate(cube_list):
        for y, block in enumerate(line):
            if block == 1:
                draw_cube((x - 5, 0,  y - 5))
    #draw_cube((0, 0, 0))
    #draw_cube((1, 0, 0))
    #draw_cube((0, 1, 0))
    glutSolidTeapot(1)
    # glPopMatrix()
    glutSwapBuffers()


def refresh2d(width, height):
    global pixel_per_unit
    pix_width = int(width / pixel_per_unit)
    pix_height = int(height / pixel_per_unit)
    print(pix_height, pix_width)
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-pix_width / 2, pix_width / 2, -pix_height / 2, pix_height / 2, -1000, 1000)
    # glOrtho(0.0, width, 0.0, height, -1000, 1000)
    glMatrixMode(GL_MODELVIEW)
    glOrtho(-pix_width / 2, pix_width / 2, -pix_height / 2, pix_height / 2, -1000, 1000)
    glLoadIdentity()
    init()


def refresh3d(x, y):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluPerspective(45, 1, 1, 15)
    gluLookAt(0, 2, 5, 0, 0, -1, 0, 1, 0)


def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                   # start drawing a rectangle
    glVertex2f(x, y)                    # bottom left point
    glVertex2f(x + width, y)            # bottom right point
    glVertex2f(x + width, y + height)   # top right point
    glVertex2f(x, y + height)           # top left point
    glEnd()


def draw_cube(position):
    # We only draw the top and the front of the cube.
    glBegin(GL_QUADS)
    # Front
    glNormal3d(0, 0, 1)
    glVertex3i(position[0], position[1], position[2])
    glVertex3i(position[0], position[1] + 1, position[2])
    glVertex3i(position[0] + 1, position[1] + 1, position[2])
    glVertex3i(position[0] + 1, position[1], position[2])
    # Top
    glNormal3d(0, 1, 0)
    glVertex3f(position[0], position[1] + 1, position[2])
    glVertex3f(position[0], position[1] + 1, position[2] - 1)
    glVertex3f(position[0] + 1, position[1] + 1, position[2] - 1)
    glVertex3f(position[0] + 1, position[1] + 1, position[2])
    glEnd()


def main_loop(window_name, size=(900, 600)):
    global pixel_per_unit
    pixel_per_unit = 160
    window_name = str.encode(window_name)  # Transform string to bytes
    glutInit(sys.argv)  # initialize glut
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(size[0], size[1])  # set window size
    glutInitWindowPosition(0, 0)  # set window position

    glutCreateWindow(window_name)  # create window with title
    glutReshapeFunc(refresh2d)
    glutDisplayFunc(draw)  # set draw function callback
    glutIdleFunc(draw)  # draw all the time
    glutMainLoop()


def init():
    ambient = [0.2, 0.2, 0.2]
    diffuse = [1.0, 1.0, 1.0]
    specular = [1.0, 1.0, 1.0]
    position = [2, 0, 2]

    lmodel_ambient = [0.2, 0.2, 0.2, 1.0]
    local_view = [0.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT0, GL_POSITION, position)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lmodel_ambient)
    glLightModelfv(GL_LIGHT_MODEL_LOCAL_VIEWER, local_view)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_AUTO_NORMAL)
    glFrontFace(GL_CW)
    glShadeModel(GL_SMOOTH)


main_loop("hallo")
