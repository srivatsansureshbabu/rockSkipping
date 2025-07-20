from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from entities import *
from ursina import *
import time
from random import randint, uniform

# state variables
flying = False
rock_velocity = Vec3(0, 0, 0)
gravity = Vec3(0, -9.8, 0)

def update_rock(rock, player, camera, water, held_keys, time):
    global flying, rock_velocity

    if held_keys['left mouse']:
        if not flying:
            # detach & start flying
            rock.parent = scene
            rock.world_position = camera.world_position + camera.forward * 1
            # rock.look_at(rock.world_position + camera.forward)
            rock.rotation_x = 90
            rock_velocity = camera.forward * 250  # set initial throw velocity
            flying = True
        
        if flying:
            # apply gravity and forward motion
            rock_velocity += gravity * time.dt
            rock.position += rock_velocity * time.dt
            rock.rotation_x = 90
            rock.rotation_y +=1
            if rock.intersects(water).hit:
                rock_velocity.y = -rock_velocity.y
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

def jump(player,originalPos,held_keys):
    jumpAmount = abs(player.y - originalPos)
    if held_keys["space"]:
        if jumpAmount <= 40:
            player.y += 1
    else:
        if player.y >= originalPos:
            player.y = player.y - 0.5


def spawnSplash(position):
    # droplets
    for _ in range(50):
        droplet = Entity(
            model='sphere',
            scale=uniform(0.05*30, 0.15*30),
            color=color.cyan,
            position=position - Vec3(0,8,0),
        )
        direction = Vec3(
            uniform(-1,1), 
            abs(uniform(0.5,2)),  # always upward
            uniform(-1,1)
        ).normalized()
        speed = uniform(0.5, 2)
        droplet.animate_position(
            droplet.position + direction * speed, 
            duration=0.5, 
            curve=curve.linear
        )
        droplet.animate_scale(0, duration=0.5, curve=curve.in_expo)
        destroy(droplet, delay=0.5)

    # ripples
    for i in range(2):
        ripple = Entity(
            model='circle',
            color=color.rgba(65,150,189,100),
            position=position + Vec3(0,0.01,0),
            scale=0.1,
            rotation_x=90
        )
        ripple.animate_scale(1.5 + i*0.5, duration=0.5 + i*0.2)
        ripple.animate_color(color.rgba(65,150,189,0), duration=0.5 + i*0.2)
        destroy(ripple, delay=0.7 + i*0.2)

    # mist spray
    for _ in range(10):
        mist = Entity(
            model='quad',
            scale=0.02,
            color=color.rgba(65,150,189,100),
            position=position,
            rotation_x=90
        )
        mist_direction = Vec3(
            uniform(-1,1), 
            uniform(0.2,0.5), 
            uniform(-1,1)
        ).normalized() * uniform(1, 2)
        mist.animate_position(
            mist.position + mist_direction, 
            duration=0.3, 
            curve=curve.linear
        )
        mist.animate_scale(0, duration=0.3)
        destroy(mist, delay=0.3)

def checkSplash(rock, water):
    if rock.intersects(water).hit:
        spawnSplash(rock.position)
        return True
    return False
