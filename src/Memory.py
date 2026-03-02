import simpy

class Memory:
    def __init__(self, env, capacity):
        self.container = simpy.Container(env, init=capacity, capacity=capacity)
    def request(self, amount):
        return self.container.get(amount)
    def release(self, amount):
        return self.container.put(amount)