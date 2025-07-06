from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from entities import *

app = Ursina()


initializeGround()
player = initializePlayer()
rock = initializeRock()
initializeSky()


flying = False  # track if rock is flying

def update():
    global flying
    rock.rotation_x = 90
    if held_keys['space']:
        if not flying:
            # detach & start flying
            rock.rotation_x = 90
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
            rock.position = player.position
            rock.rotation_x = 90
            flying = False

app.run()