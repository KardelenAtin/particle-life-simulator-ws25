#  Particle Life Simulator (Project DSAI, WS 25/26)

This project is a high-performance simulation of "Particle Life." It was created for the "Data Science and AI Infrastructure" module to show how life-like, complex patterns can emerge from very simple rules. By just telling different types of particles to either attract or repel each other, they begin to form structures that look like cells, swarms, or even tiny organisms.

---

##  Key Features

* **High-Performance Backend**: Deep integration of `numpy` and `numba` to eliminate Python interpreter overhead, achieving a ~400x speedup.
* **Massive Real-Time Simulation**: Smoothly handles over **2,000 particles** at **60-70 FPS** on standard hardware.
* **GPU-Accelerated Visualization**: Interactive rendering using `vispy` (OpenGL integration) for high frame rates.
* **Scientific Validation**: A test suite with **over 70% coverage** ensures the mathematical and physical integrity of the model.
* **Interactive Parameters**: Dynamic real-time control over the interaction matrix, particle distribution, and simulation flow.

---

##  Project Structure

The repository is organized to separate core logic, documentation, and quality assurance:

* `src/`: Core source code.
    * `simulation.py`: Physics engine featuring `@njit` optimized force loops.
    * `interaction.py`: Management of the asymmetric interaction matrix.
    * `visualization.py`: GUI logic and OpenGL marker rendering.
    * `config.py`: Global constants for colors, timing, and space limits.
* `tests/`: Unit tests for physics and data integrity.
* `docs/`: Detailed performance reports and hardware benchmarks.
* `Profiling.py`: Main utility script for runtime analysis and bottleneck identification.

---

##  User Guide

### Prerequisites
* Python 3.10 or newer.
* A graphics card supporting OpenGL (standard for most modern PCs).

### Installation
1.  **Clone the repository**:
    ```bash
    git clone (https://github.com/KardelenAtin/particle-life-simulator-ws25.git)
    cd particle-life-simulator-ws25
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### How to Run
Launch the interactive simulation via the main entry point:
```bash
python main.py
