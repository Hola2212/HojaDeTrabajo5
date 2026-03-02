from Simulation import Simulation
from Grapher import Grapher

process_counts = [25, 50, 100, 150, 200]
intervals = [10, 5, 1]
grapher = Grapher()

for interval in intervals:
    print(f"\nINTERVALO = {interval}")
    for n in process_counts:
        sim = Simulation(n, interval)
        avg, std = sim.run()
        print(f"Procesos: {n}")
        print(f"Promedio: {avg:.4f}")
        print(f"Desv Std: {std:.4f}")

        # Store results using lists
        grapher.add_result(interval, n, avg)
# Generate the graph after all simulations
grapher.plot("Baseline System Performance")