from vispy import app, scene
import numpy as np
from src.simulation import Simulation
from src.config import SPACE_MIN, SPACE_MAX


def main():
    sim = Simulation([
        {"n":500, "type": 0}, 
        {"n":500, "type": 1}, 
        {"n":500, "type": 2}, 
        {"n":500, "type": 3}
    ])

    # GUI window
    canvas = scene.SceneCanvas(keys="interactive", show=True)
    canvas.size = 800, 600
    canvas.title = "Particles"

    view = canvas.central_widget.add_view()
    view.camera = scene.cameras.PanZoomCamera(aspect=1)
    view.camera.set_range(
        x=(SPACE_MIN, SPACE_MAX),
        y=(SPACE_MIN, SPACE_MAX),
        margin=0
    )

    scatter = scene.visuals.Markers()
    scatter.set_gl_state('translucent', blend=True, depth_test=False)
    scatter.set_data(
        sim.positions.astype(np.float32),
        face_color=sim.colors.astype(np.float32),
        size=6
    )
    view.add(scatter)

    frame_counter = 0
    
    def update(event):
        nonlocal frame_counter
        frame_counter += 1

        if frame_counter % 2 == 0:
            sim.step()
        
        scatter.set_data(
            sim.positions.astype(np.float32),
            face_color=sim.colors.astype(np.float32),
        )

    timer = app.Timer(interval=1/60, connect=update, start=True)
    app.run()


if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()

>>>>>>> 6f87155d27656805c05613fe31664fac6c9f9062
