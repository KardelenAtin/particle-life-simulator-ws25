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


class Simulation:
    def __init__(
            self,
            settig = None,
            mass: float = 1.0,
            bounciness: float = 1.0      
        ):

        if setting is None:
            setting = [{"n":3,"type":2},{"n":4, "type":0}]

        self.types = np.column_stack([
            self.positions[:,0],
            self.positions[:,1],
            self.velocities[:,0],
            self.velocities[:,1],
            self.types
        ]).astype(float)

    def update_particles_view(self):
        self.particles[:, 0:2] = self.positions
        self.particles[:, 2:4] = self.velocities
        self.particles[:, 4] = self.types

if __name__ == "__main__":
    sim = Simulation([{"n": 103, "typ": 2}, {"n": 14, "typ": 0}])
    print("n_particles:", sim.n_particles)
    print("particles shape:", sim.particles.shape)
    print(sim.particles[:5])



    

