import random
import numpy as np
# from config import SPACE_MIN, SPACE_MAX, N_PARTICLE_TYPES, COLOR_DISTRIBUTION , friction, delta_t, width, height

class Simulation:
    def __init__(self, setting = [{"n":3,"type":2},{"n":4,"type":0}]): 
        particles = []
        for s in setting:
            for p in range(s["n"]):
                particle = np.array([random.randint(0, 100), random.randint(0, 100), 0, 0, s["type"]])
                particles.append(particle)
        self.particles = np.vstack(particles)
        print(self.particles)

        
if __name__ == "__main__":
    ll= Simulation([{"n":103,"type":2},{"n":14,"type":0}])
