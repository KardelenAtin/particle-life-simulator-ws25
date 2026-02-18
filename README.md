#  Particle Life Simulator (Project DSAI, WS 25/26)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Numba](https://img.shields.io/badge/Acceleration-Numba-orange)
![NumPy](https://img.shields.io/badge/Backend-NumPy-green)

##  Project Description

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
    git clone https://github.com/KardelenAtin/particle-life-simulator-ws25.git
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
   ```

---

### Controls
| Key | Action | Description |
| :--- | :--- | :--- |
| **R** | Reset | Re-initializes particle positions within the simulation space. |
| **M** | Randomize Matrix | Generates a new interaction matrix (triggers behavioral shifts). |
| **P** | Pause/Play | Toggles the simulation state (active/idle). |

---

## Developer Guide

### 1.Performance & Benchmarking
The core physics loop is compiled into machine code using *Numba (Just-In-Time compilation)*. This is crucial for handling the  complexity of particle-to-particle interactions:

| Version | Performance |
|----------|------------|
| **Baseline (Pure Python)** | ~0.17 FPS |
| **Optimized (Numba JIT)** | ~68.0 FPS |

To perform a runtime analysis:

   ```
   python Profiling.py
   snakeviz simulation.profile
   ```

For a more detailed performance breakdown including SnakeViz visualizations and kernel-level analysis, see:
[Profiling Report](docs/profiling.md)

### 2.Continuous Integration (CI)
All quality checks are automatically executed via our CI pipeline.
Each push and pull request triggers:

* Unit test execution
* Coverage validation (>70%)
* Linting checks
* Dependency verification

This ensures early detection of regressions and guarantees consistent code quality across environments.

### 3.Quality Assurance
We maintain code reliability using the following tools:

- **Testing:** pytest  
- **Coverage:** pytest --cov=src  
- **Linting:** ruff check 

---

## Physics Model
The engine utilizes a *Smoothstep force function* implemented within the JIT kernels:

* **Repulsion Zone**: At a proximity of <15% of the MAX_RADIUS, particles experience strong repulsion to prevent overlapping.
* **Interaction Zone**: Between 15% and 60% of the radius, attraction or repulsion is applied based on the values defined in the Interaction matrix.
* **Vectorization**: Position and velocity updates are performed as vectorized array operations to maximize memory throughput.

---

##  Project Team
* *Kardelen Atin* -Backend
* *Meriem Nora Bouazza* -Backend
* *Vipusiny Vijayakumar* -Backend
* *Melina Tsigka* - Frontend
