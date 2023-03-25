import pygame
import mapdata
import math

pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()

# load images
plane = pygame.transform.scale(pygame.image.load("plane.png"), (128, 128))
map_chars = set([c for c in mapdata.map_text if c != "." and c != "\n"])
images = {c: pygame.image.load(f"insel{c}.png") for c in map_chars}

yy = 0
time = 0
while True:
    screen.fill(pygame.Color("#3e46a9"))
    delta_time = clock.tick(120) / 1000
    yy += delta_time * 180
    time += delta_time
    if yy > 64:
        yy = yy - 64
        mapdata.map = [mapdata.map[-1]] + mapdata.map[0:-1]  # shift map down

    for y, row in enumerate(mapdata.map[0:11]):
        for x, col in enumerate(row):
            if col != ".":
                screen.blit(images[col], [x * 64, y * 64 + yy - 64])

    screen.blit(plane, [260 + math.sin(time * 1.5) * 60 + math.sin(time * 1) * 60, 500])
    pygame.display.flip()
