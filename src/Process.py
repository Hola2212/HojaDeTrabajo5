class Packet:
    def __init__(self, env, name, size): #Inicializador de clase
        #Variables de clase. Tienen una funcion similar a las globales
        self.env = env
        self.name = name
        self.size = size        #Procesos que debe realizar antes de salirse.
        self.remaining = size   #Procesos restantes antes de salir
        self.arrival_time = env.now
        self.start_time = None
        self.finish_time = None