import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800,600))

class Vertex:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.pos = self.x, self.y, self.z = x, y, z

# INFO: useful for later?
class Line:
    def __init__(self, vertex_a: Vertex, vertex_b: Vertex) -> None:
        self.info = [vertex_a, vertex_b]

class Face:
    def __init__(self, *vertexs) -> None:
        self.info = vertexs

a_vertex = Vertex(1, 1, 1)
b_vertex = Vertex(-1, 1, 1)
a_face = Face(a_vertex, b_vertex)
print(a_face.info)

# TODO: add renderer

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    pygame.display.flip()
    pygame.display.update()

