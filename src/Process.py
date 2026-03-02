import random

class Process:
    def __init__(self, env, name, memory, cpu, metrics):
        self.env = env
        self.name = name
        self.memory = memory
        self.cpu = cpu
        self.metrics = metrics
        self.arrival_time = env.now
        self.memory_needed = random.randint(1, 10)
        self.remaining_instructions = random.randint(1, 10)

    def run(self):
        #NEW
        yield self.memory.request(self.memory_needed)
        # READY
        while self.remaining_instructions > 0:
            yield self.env.process(self.cpu.run(self))
            #TERMINATED
            if self.remaining_instructions <= 0:
                break
            # Decide if it goes to WAITING
            r = random.randint(1, 21)
            if r == 1:
                # WAITING
                yield self.env.timeout(1)
            #elif and else are not necessary as they don't
            # really do anything, but it is a representation
            # to see how the simulation handles them
            elif r == 2:
                # READY (explicit but no delay)
                pass
            else:
                # CONTINUE
                pass

        # TERMINATED
        yield self.memory.release(self.memory_needed)
        self.metrics.record(self.arrival_time, self.env.now)