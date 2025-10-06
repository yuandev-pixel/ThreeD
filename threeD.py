from numpy.typing import ArrayLike
import pygame
import sys
import numpy as np

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
    def __init__(self, *vertexs: Vertex) -> None:
        self.info = vertexs

class Object:
    def __init__(self, *faces: Face) -> None:
        self.info = faces

class Camera:
    def __init__(self, pos: tuple[float, float, float], rotation: tuple[float, float, float], fov: int) -> None:
        self.pos = self.x, self.y, self.z = pos
        self.rotation = self.rotation_x, self.rotation_y, self.rotation_z = rotation
        self.fov = fov

class Scene:
    def __init__(self, camera: Camera, *objects: Object) -> None:
        self.info = {"objects": objects, "camera": camera}

# TODO: add renderer

# why do you need two renderers
class Renderer:
    def __init__(self, scene: Scene) -> None:
        self.scene = scene
        self.buffer = {}

    def rotation_matrix_x(self, theta: float) -> ArrayLike:
        return np.array([
            [1, 0, 0],
            [0, np.cos(theta), -np.sin(theta)],
            [0, np.sin(theta), np.cos(theta)]
        ])

    def rotation_matrix_y(self, theta: float) -> ArrayLike:
        return np.array([
            [np.cos(theta), 0, np.sin(theta)],
            [0, 1, 0],
            [-np.sin(theta), 0, np.cos(theta)]
        ])

    def rotation_matrix_z(self, theta: float) -> ArrayLike:
        return np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])

    def rotate_x(self, vecter: ArrayLike, theta: float) -> ArrayLike:
        return np.dot(self.rotation_matrix_x(theta), vecter)

    def rotate_y(self, vecter: ArrayLike, theta: float) -> ArrayLike:
        return np.dot(self.rotation_matrix_y(theta), vecter)

    def rotate_z(self, vecter: ArrayLike, theta: float) -> ArrayLike:
        return np.dot(self.rotation_matrix_z(theta), vecter)
    
    def render(self) -> None:
        scene_obj = self.scene.info["objects"]
        scene_cam = self.scene.info["camera"]

    def push(self) -> None:
        pass

a_vertex = Vertex(0, 0, 0)
b_vertex = Vertex(1, 0, 0)
c_vertex = Vertex(0, 1, 0)
a_face = Face(a_vertex, b_vertex, c_vertex)
a_object = Object(a_face)
a_camera = Camera((0, 0, 0), (0, 0, 0), 60)
a_scene = Scene(a_camera, a_object)
render = Renderer(a_scene)
print(render.rotate_z(np.array([1, 1, 0]), np.pi/4))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    pygame.display.flip()
    pygame.display.update()

