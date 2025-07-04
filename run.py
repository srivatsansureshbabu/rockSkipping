from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()




ground = Entity(
    model = "plane",
    texture = "grass",
    collider = "mesh",
    scale = (200,1,200)
)

sky = Sky(texture='sky_sunset')  # or 'sky_default', or your own panoramic sky

player = FirstPersonController()
destroy(player.cursor)

player.speed = 100
player.gravity = 0  # optional, so you don't fall through the plane
# Add some rocks (optional)

original_pos = Vec3(0.5, -0.5, 1)

rock = Entity(
    model='Objects/skipping rock/tinker.obj',
    texture=None,
    color=color.gray,
    scale=0.5,
    position=original_pos
    # parent=player.children[0],  # the camera entity named "entity"
)
rock.rotation = 90

flying = False  # track if rock is flying

def update():
    global flying

    if held_keys['space']:
        if not flying:
            # detach & start flying
            rock.parent = scene
            rock.world_position = camera.world_position + camera.forward * 1
            rock.look_at(rock.world_position + camera.forward)
            flying = True
        
        # move rock forward
        rock.position += camera.forward * 500 * time.dt

    else:
        if flying:
            # reset back to hand
            rock.parent = camera
            rock.position = original_pos
            flying = False

app.run()