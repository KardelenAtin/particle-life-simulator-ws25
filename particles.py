import random 

particle_types = ['A', 'B', 'C', 'D']

#lists all particles in a dictionary 
particles = []

#gives the particles random position  and velocity
for i in range(4):
    p = {
        "x": random.randint(0,100), 
        "y": random.randint(0,100),
        "vx": random.randint(-1,1),
        "vy": random.randint(-1,1),
        "typ": particle_types[i]
    }
    particles.append(p)

#friction factor used to damp particle velocities 
friction = 0.99

def update_velocities(particles, friction):
        """
        Calculating the friction from the velocities. This reduces the velocity each
        simulation step and stabilizes the simulation.
        """
        for p in particles:
            p["vx"] *= friction
            p["vy"] *= friction

       
#delta_t is used for position updates
delta_t = 0.5

#calculates the new positon of the particles, through the velocity and delta_t
def update_positions(particles, delta_t):
    for p in particles:
        x, y = p["x"], p["y"]
        vx, vy = p["vx"], p["vy"]

        new_x = x + vx * delta_t 
        new_y = y + vy  * delta_t 

        p["x"] = new_x
        p["y"] = new_y


width, height = 100, 100

def apply_wraparound(particles, width, height):
     for p in particles: 
          new_width_x = p["x"] % width
          new_height_y = p["y"] % height

          p["x"] = new_width_x
          p["y"] = new_height_y

#Aufrufen von den zwei Funktionen
update_velocities(particles, friction)
update_positions(particles, delta_t)
apply_wraparound(particles, width, height)
print(particles)