from vispy import app, scene
import numpy as np


#GUI window
canvas = scene.SceneCanvas(show=True)
canvas.size = 800, 600
canvas.title = "GUI Window"

view = canvas.central_widget.add_view()
view.camera = scene.cameras.PanZoomCamera(aspect=1)

#draw particles
n_points = 1000
x = np.random.normal(loc=0.0, scale=10.0, size=n_points)
y = np.random.normal(loc=0.0, scale=10.0, size=n_points)

positions = np.column_stack((x, y))

types = np.random.randint(0, 4, size=n_points)

"""
#colors-array for particles
color_dict = {
    0: [1, 0, 0, 1], #red 
    1: [0, 1, 0, 1], #green
    2: [0, 0, 1, 1], #blue
    3: [1, 1, 0, 1], #yellow
}

#colors 
colors = []
for t in types:
    colors.append(color_dict[t])
colors = np.array(colors, dtype=np.float32)
"""

#scatter plot
scatter = scene.visuals.Markers()
scatter.set_data(positions, face_color=colors, size=10)
view.add(scatter)

if __name__ == '__main__':
    app.run()