from vispy import app, scene
import numpy as np

canvas = scene.SceneCanvas(show=True)
canvas.size = 800, 600
canvas.title = "GUI Window"

view = canvas.central_widget.add_view()
view.camera = scene.cameras.PanZoomCamera(aspect=1)

if __name__ == '__main__':
    app.run()
