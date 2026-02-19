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
    canvas.size = 1000, 800
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
        size=4
    )
    view.add(scatter)

    STEPS_PER_FRAME = 2
    def update(_):
        for _ in range(STEPS_PER_FRAME):
            sim.step()
        
        scatter.set_data(
            sim.positions.astype(np.float32),
            face_color=sim.colors.astype(np.float32),
            size=6
        )
        canvas.update()

    timer = app.Timer(interval=1/60, connect=update, start=True)

    @canvas.events.key_press.connect

    def on_key_press(event):
        """Handle keyboard inputs for interaction."""
        if event.text.lower() == 'r':
            sim.positions = np.random.uniform(SPACE_MIN, SPACE_MAX, size=(sim.n_particles, 2))
        
        elif event.text.lower() == 'm':
            sim.interaction.matrix = np.random.uniform(-1, 1, (4, 4))

        elif event.text.lower() == 'p':
            
            if timer.running:
                timer.stop()

            else:
                timer.start()
    
    
    app.run()


if __name__ == "__main__":
    main()

