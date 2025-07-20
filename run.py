from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from entities import *
from actions import *
from random import uniform

app = Ursina()

# initialize entitites
[sand,water] = initializeGround()
player = initializePlayer()
rock = initializeRock()
initializeSky()
originalPos = 20

# this is mainly for the rock throws
flying = False 
rock_velocity = Vec3(0, 0, 0)   
gravity = Vec3(0, -9.8, 0) 


def update():
    update_rock(rock,player,camera,water,held_keys,time)
    jump(player,originalPos, held_keys)
    checkSplash(rock,water)

app.run()