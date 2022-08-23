import pygame
import pymunk
import sys

pygame.init()

size = width, height = 1000, 900
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 500)

white = (255, 255, 255)
red = (255, 0, 0)

circle_loc = (150, 450)

fps = 1 / 50
screen = pygame.display.set_mode(size)

space_toggle = False


def create_circle(space):
    body = pymunk.Body(2, 10, body_type=pymunk.Body.DYNAMIC)
    body.position = circle_loc
    shape = pymunk.Circle(body, 40)
    space.add(body, shape)
    return shape


def draw_circle(circle):
    pygame.draw.circle(screen, red, circle.body.position, 40)


# def pipes(space):changed in website tester
# TODO: Reserch about collision detection in pymunk
# I changed this in testing branch
# Ichanged this in main branch
def static_ball(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (150, 600)
    shape = pymunk.Circle(body, 40)
    space.add(body, shape)
    return shape


circle_main = create_circle(space)
static = static_ball(space)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.mod and pygame.K_SPACE:
                if not space_toggle:
                    circle_main.body.apply_impulse_at_local_point((0, -1000), (0, circle_main.body.position[1]))
                    # print(circles[0].body.position)
                    space_toggle = True
                else:
                    space_toggle = False

    screen.fill(white)
    draw_circle(circle_main)
    draw_circle(static)

    space.step(fps)
    pygame.display.update()
    clock.tick(120)
