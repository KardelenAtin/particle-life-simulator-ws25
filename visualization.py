from vispy import app, scene
import numpy as np
from simulation import Simulation


sim = Simulation([
    {"n":250, "type": 0}, 
    {"n":250, "type": 1}, 
    {"n":250, "type": 2}, 
    {"n":250, "type": 3}])

#GUI window
canvas = scene.SceneCanvas(keys="interactive", show=True)
canvas.size = 800, 600
canvas.title = "Particles"

view = canvas.central_widget.add_view()
view.camera = scene.cameras.PanZoomCamera(aspect=1)


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
        size = 10
    )

timer = app.Timer(interval=1/120, connect=update, start=True)

if __name__ == '__main__':
    app.run()
