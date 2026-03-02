from statistics import mean, stdev    #Calcular el promedio y el calculo de la desviación estandar
class Metrics:
    def __init__(self):
        self.times = []
    def record(self, start, end):
        self.times.append(end - start)
    def summary(self):
        if len(self.times) < 2:
            return mean(self.times), 0
        return mean(self.times), stdev(self.times)