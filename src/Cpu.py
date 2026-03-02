import simpy

class CPU:
    def __init__(self, env, capacity, instructions_per_cycle, speed):
        self.env = env
        self.resource = simpy.Resource(env, capacity=capacity)
        self.instructions_per_cycle = instructions_per_cycle
        self.speed = speed

    def run(self, process):
        with self.resource.request() as req: #Better so it closse automatically after finishing the instruccions indented to the with
            yield req
            yield self.env.timeout(self.speed)
            executed = min(
                self.instructions_per_cycle,
                process.remaining_instructions
            )
            process.remaining_instructions -= executed