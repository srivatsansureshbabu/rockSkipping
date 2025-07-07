from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from entities import *

from ursina import *

# state variables
flying = False
rock_velocity = Vec3(0, 0, 0)
gravity = Vec3(0, -9.8, 0)

def update_rock(rock, player, camera, held_keys, time):
    global flying, rock_velocity

    if held_keys['space']:
        if not flying:
            # detach & start flying
            rock.parent = scene
            rock.world_position = camera.world_position + camera.forward * 1
            rock.look_at(rock.world_position + camera.forward)
            rock.rotation_x = 90
            rock_velocity = camera.forward * 500  # set initial throw velocity
            flying = True
        
        if flying:
            # apply gravity and forward motion
            rock_velocity += gravity * time.dt
            rock.position += rock_velocity * time.dt
            rock.rotation_x = 90

            # optional: stop if it hits ground
            # if rock.y <= 0:
            #     rock.y = 0
            #     flying = False
            #     rock_velocity = Vec3(0,0,0)

    else:
        if flying:
            # reset back to hand
            rock.parent = camera
            rock.position = player.position + Vec3(0,5,0)
            rock.rotation_x = 90
            rock_velocity = Vec3(0,0,0)
            flying = False
