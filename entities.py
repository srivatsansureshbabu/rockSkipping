from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from entities import *

def initializeGround():
    # Initializes sand
    sand = Entity(
    model = "plane",
    texture = 'Background/sandTexture.jpg',
    collider = "mesh",
    scale = (2000,1,200)
    )
    water = Entity(
        model = "plane",
        texture = 'Background/waterTexture.jpg',
        collider = 'box',
        scale = (2000,1,2000),
        position = (0,0,1100),
    )
    return [sand,water]



def initializePlayer():
    # player = Entity(model='cube', color=color.azure, position=(0,20,0))
    player = FirstPersonController()
    player.y += 20
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
        position=original_pos,
        collider= 'box'
        # parent=player.children[0],  # the camera entity named "entity"
    )
    
    return rock

    