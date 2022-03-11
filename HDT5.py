import simpy
import random
random.seed(0)

def proceso(nombre, env, llegada, tiempoEnCPU, usoRam):
    # Simulate driving to the BCS
    yield env.timeout(llegada)

    # Request one of its charging spots
    print('%s proceso en cola NEW %d' % (nombre, env.now))
    
    yield ram.get(usoRam)
    
    with cpu.request() as req:
        yield req
        
        # Charge the battery
        print('%s proceso en cola READY %s' % (nombre, env.now))
        #yield env.timeout(charge_duration)
        print('%s ha dejado la cola READY %s' % (nombre, env.now))
        # se hizo release automatico del cargador bcs
            
#
env = simpy.Environment()  #crear ambiente de simulacion
ram = simpy.Container(env, 100, init = 0) #crea el container de la ram
cpu = simpy.Resource(env, capacity=1) #se crea el procesador con capacidad establecida
procesos = 5 #cantidad de procesos a generar

    

for i in range(procesos):
    llegada = random.expovariate(1.0/10) #tiempo en el que llegan los procesos
    tiempoEnCPU = random.randint(1, 10) #cantidad de operaciones por proceso
    UsoRam = random.randint(1, 10) #cantidad de ram que requiere cada proceso
    env.process(proceso('proceso %d'%i,env,llegada,tiempoEnCPU,UsoRam))
    
# correr la simulacion
env.run()