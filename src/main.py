from Simulation import Simulation
from Grapher import Grapher
#To show all graphs at once
#import matplotlib.pyplot as plt

process_counts = [25, 50, 100, 150, 200]
intervals = [10, 5, 1]

def run_condition(title, ram, cpu_cap, instr_cycle):
    print("\n==============================")
    print(title)
    print("==============================")
    grapher = Grapher()
    for interval in intervals:
        print(f"\nINTERVALO = {interval}")
        for n in process_counts:
            sim = Simulation(
                num_processes=n,
                interval=interval,
                ram=ram,
                cpu_cap=cpu_cap,
                instr_cycle=instr_cycle
            )
            avg, std = sim.run()
            print(f"Procesos: {n}")
            print(f"Promedio: {avg:.4f}")
            print(f"Desv Std: {std:.4f}")
            grapher.add_result(interval, n, avg)
    grapher.plot(title)

# Baseline
run_condition(
    title="Baseline (RAM=100, CPU=1, Instr=3)",
    ram=100,
    cpu_cap=1,
    instr_cycle=3
)

# RAM = 200
run_condition(
    title="RAM = 200",
    ram=200,
    cpu_cap=1,
    instr_cycle=3
)

# CPU = 6 instrucciones
run_condition(
    title="CPU = 6 Instructions per Cycle",
    ram=100,
    cpu_cap=1,
    instr_cycle=6
)

# 2 CPUs
run_condition(
    title="2 CPUs",
    ram=100,
    cpu_cap=2,
    instr_cycle=3
)
#Show all graphs at once
#plt.show()