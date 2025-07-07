from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from entities import *
from actions import *

app = Ursina()

initializeGround()
player = initializePlayer()
rock = initializeRock()
initializeSky()


flying = False  # track if rock is flying
rock_velocity = Vec3(0, 0, 0)   # initial velocity
gravity = Vec3(0, -9.8, 0)      # adjust as needed


def update():
    update_rock(rock,player,camera,held_keys,time)
    # global flying
    # global rock_velocity
    # global gravity 
    # if held_keys['space']:
    #     if not flying:
    #         # detach & start flying
    #         rock.parent = scene
    #         rock.world_position = camera.world_position + camera.forward * 1
    #         rock.look_at(rock.world_position + camera.forward)
    #         rock.rotation_x = 90  # enforce after look_at
    #         flying = True
        
    #     # move rock forward
    #     rock_velocity += gravity * time.dt
    #     rock.position += rock_velocity * time.dt
    #     rock.rotation_x = 90
    #     rock.position += camera.forward * 500 * time.dt
    #     rock.rotation_x = 90  # enforce during flight too

    # else:
    #     if flying:
    #         # reset back to hand
    #         rock.parent = camera
    #         rock.position = player.position
    #         rock.rotation_x = 90
    #         flying = False


app.run()