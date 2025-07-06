from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from entities import *

def initializeGround():
    ground = Entity(
    model = "plane",
    texture = "grass",
    collider = "mesh",
    scale = (200,1,200)
    )

def initializePlayer():
    player = Entity(model='cube', color=color.azure, position=(0,0,0))
    player = FirstPersonController()
    destroy(player.cursor)
    player.speed = 100
    player.gravity = 0  # optional, so you don't fall through the plane
    return player

def initializeSky():
    sky = Sky(texture='sky_sunset')  # or 'sky_default', or your own panoramic sky

def initializeRock():
    original_pos = Vec3(0.5, -0.5, 1)
    rock = Entity(
        model='Objects/skipping rock/tinker.obj',
        texture=None,
        color=color.gray,
        scale=0.5,
        position=original_pos
        # parent=player.children[0],  # the camera entity named "entity"
    )
    return rock
