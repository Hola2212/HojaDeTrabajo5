from statistics import mean     #Calcular el promedio. Se puede reemplazar por datos.sum()/len(datos)
class Metrics:
    def __init__(self):
        self.completed_packets = []
    def record(self, packet):
        self.completed_packets.append(packet)
    def summary(self):
        turnaround_times = []
        for p in self.completed_packets:
            turnaround_time = p.finish_time - p.arrival_time
            turnaround_times.append(turnaround_time)
        waiting_times = []
        for p in self.completed_packets:
            waiting_time = p.start_time - p.arrival_time
            waiting_times.append(waiting_time)
        #Genera un diccionario con los resultados de esta prueba. Si no hay paquetes, regresa 0 en todos los valores del diccionario.
        summary = {"total_packets": len(self.completed_packets), "avg_turnaround": mean(turnaround_times) if turnaround_times else 0, "avg_waiting": mean(waiting_times) if waiting_times else 0}
        return summary