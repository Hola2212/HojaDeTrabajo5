import simpy
import random
from Process import Process
from Cpu import CPU
from Memory import Memory
from Metrics import Metrics
from Config import *

class Simulation:
    def __init__(self, num_processes, interval, ram=RAM_CAPACITY, cpu_cap=CPU_CAPACITY, instr_cycle=INSTRUCTIONS_PER_CYCLE):
        random.seed(RANDOM_SEED)
        self.env = simpy.Environment()
        self.num_processes = num_processes
        self.interval = interval
        self.memory = Memory(self.env, ram)
        self.cpu = CPU(self.env, cpu_cap, instr_cycle, CPU_SPEED)
        self.metrics = Metrics()

    def generator(self):
        for i in range(self.num_processes):
            p = Process(self.env, f"P{i}", self.memory, self.cpu, self.metrics) #f"P{i}" Formato para colocar "P" + str(i)
            self.env.process(p.run())
            t = random.expovariate(1.0 / self.interval)
            yield self.env.timeout(t)

    def run(self):
        self.env.process(self.generator())
        self.env.run()
        return self.metrics.summary()