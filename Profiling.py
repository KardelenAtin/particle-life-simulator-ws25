import cProfile
import pstats
import io
import time

from src.simulation import Simulation

def run_benchmark():
    """
    Measures simulation performance and saves data for Snakeviz visualization.
    """
    
    setup = [{"n": 500, "type": i} for i in range(4)]
    sim = Simulation(setup)
    steps = 200

    # 1. JIT Warmup (Crucial for Numba)
    print("JIT Warmup...")
    sim.step()

    # 2. Profiling
    print(f"Starting profiling for {steps} steps...")
    profiler = cProfile.Profile()
    
    start_t = time.time()
    profiler.enable()

    for i in range(steps):
        if i % 10 == 0:
            print(f"Step {i}/{steps}")
        sim.step()

    profiler.disable()
    end_t = time.time()

    # 3. Results
    duration = end_t - start_t
    print("\n--- Performance Results ---")
    print(f"Total Time: {duration:.2f}s")
    print(f"Simulation Speed: {steps / duration:.2f} FPS")

    # Save for Snakeviz visualization
    profiler.dump_stats('simulation.profile')

    # Quick console summary
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).sort_stats('cumtime')
    stats.print_stats(15)
    print("\n--- Top 15 Bottlenecks ---")
    print(stream.getvalue())
    print("\nDONE: Run 'snakeviz simulation.profile' to see the visual report.")

if __name__ == "__main__":
    run_benchmark()