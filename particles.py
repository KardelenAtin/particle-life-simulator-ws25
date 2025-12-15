import numpy as np
import random 
particles_typ = ['A','B','C','D']
particles = []

for i in range(4):
    p = {
        "x": random.randint(0,100),
        "y": random.randint(0,100),
        "vx": random.randint(-1,1),
        "vy": random.randint(-1,1),
        "typ": particles_typ[i]
    }
    particles.append(p)

delta_t = 0.5

    
for p in particles:
    x, y = p["x"], p["y"]
    vx, vy = p["vx"], p["vy"]

    new_x = x + vx * delta_t 
    new_y = y + vy  * delta_t 

    p["x"] = new_x
    p["y"] = new_y

print(particles)

