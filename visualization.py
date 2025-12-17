from vispy import app, scene
import numpy as np
from simulation import Simulation
from config import SPACE_MIN, SPACE_MAX

sim = Simulation([
    {"n":25, "type": 0}, 
    {"n":25, "type": 1}, 
    {"n":25, "type": 2}, 
    {"n":25, "type": 3}])

#GUI window
canvas = scene.SceneCanvas(keys="interactive", show=True)
canvas.size = 800, 600
canvas.title = "Particles"

view = canvas.central_widget.add_view()
view.camera = scene.cameras.PanZoomCamera(aspect=1)
view.camera.set_range(
    x=(SPACE_MAX, SPACE_MIN),
    y=(SPACE_MAX, SPACE_MIN)
)

#scatter plot
scatter = scene.visuals.Markers()
scatter.set_data(
    sim.positions.astype(np.float32),
    face_color = sim.colors.astype(np.float32),
    size = 10
)
view.add(scatter)


def update(event):
    sim.step()
    scatter.set_data(
        sim.positions.astype(np.float32),
        face_color = sim.colors.astype(np.float32),
    )

timer = app.Timer(interval=1/60, connect=update, start=True)

if __name__ == '__main__':
    app.run()
