from ast import While
import simpy
import random

random.seed(0)
listaProcesos = {}
listaCPU = {}
listaIO = {}
tiempo = {}
TiempoInicial = {}
intervalos = 0

#
env = simpy.Environment()  # crear ambiente de simulacion
ram = simpy.Container(env, 100, init=100)  # crea el container de la ram
cpu = simpy.Resource(env, capacity=2)  # se crea el procesador con capacidad establecida
procesos = 200  # cantidad de procesos a generar

for i in range(procesos):
    
    llegada = intervalos  # tiempo en el que llegan los procesos
    tiempoEnCPU = random.randint(1, 10)  # cantidad de operaciones por proceso
    UsoRam = random.randint(1, 10)  # cantidad de ram que requiere cada proceso
    #env.process(proceso('proceso %d' % i, env, ram, llegada, tiempoEnCPU, UsoRam))
    iString = str(i)
    listaProcesos["proceso " + iString] = ["proceso " +iString ,env,ram,llegada,tiempoEnCPU, UsoRam]
    intervalos = intervalos + 1

  
    
 
#while len(listaCPU) > 0 or len(listaIO) > 0 or len(listaProcesos) > 0:   
def proceso(nombre, env, memoria, llegada, tiempoEnCPU, usoRam):
    # Simula la llegada de los procesos
    yield env.timeout(llegada)
    
    
    #print('%s en cola New -- %d cantidad ram %d' % (nombre, env.now, usoRam))
    

    memoria.get(usoRam)
    procesoEnUso = listaProcesos.get(nombre)
    listaCPU[nombre] = procesoEnUso
    #listaProcesos.pop(nombre)
    
    # Simula el uso de memoria RAM
    
    
    #print('%s en cola Ready -- %d cantidad ram %d, disponible %d' % (nombre, env.now, usoRam, memoria.level))
    
    
    with cpu.request() as req:
        yield req

        # Pide el uso del CPU
        
        
        #print('%s en cola Running -- %s' % (nombre, env.now))
        
        
        # Resta el las instrucciones realizadas por el CPU
        tiempoEnCPU = tiempoEnCPU - 3
        #listaCPU[nombre] = listaProcesos[nombre]
        
    if tiempoEnCPU <= 0:
        
        
        print('%s ha dejado la cola Running -- %s' % (nombre, env.now))
        tiempoFinal = env.now
        tiempoInicial = TiempoInicial[nombre]
        promedio = tiempoFinal - tiempoInicial
        tiempo[nombre] = [promedio]
        memoria.put(usoRam)
        listaCPU.pop(nombre)
        for i in range(len(tiempo)):
            key = list(tiempo.items())[i][0]
            print(tiempo[key])
        
        
        # Si ya no tiene mas instrucciones por realizar deja la cola
    elif tiempoEnCPU > 0:
        #num1 = random.randint(1, 2)
        #if num1 == 1:
        
        
        #listaCPU[nombre] = listaProcesos.get(nombre)
        num1 = random.randint(1, 2)
        if num1 == 1:
            
            
            #print('%s en cola Ready -- %s' % (nombre, env.now))
            
            
            procesoEnUso = listaCPU.get(nombre)
            nombre = procesoEnUso[0]
            env = procesoEnUso[1]
            memoria = procesoEnUso[2]
            llegada = procesoEnUso[3]
            tiempoEnCPU = tiempoEnCPU
            UsoRam = procesoEnUso[5]
            
            
            #listaCPU[nombre] = procesoEnUso
            #listaCPU.pop(llave2)
            
            
            env.process(proceso(nombre, env, memoria, llegada, tiempoEnCPU, UsoRam))
        else:
            
            listaIO[nombre] = listaCPU.get(nombre)
            
            
            #print('%s en cola Waiting -- %s' % (nombre, env.now))
            
            
            #listaProcesos.pop(nombre)
            
    while len(listaIO) > 0:      
        if len(listaIO) >= 1:
                num2 = random.randint(1,2)
                #llaves = listaIO.keys()
                #print(llaves)
                if num2 == 1:
                    #listaCPU.get(llaves[0])
                    llave = list(listaIO.items())[0][0]
                    #print(llave)
                    #listaCPU[llave] = listaIO.get(llave)
                    
                    
                    #print('%s en cola Ready -- %s' % (nombre, env.now))
                    
                    
                    procesoEnUso = listaIO.get(llave)
                    nombre = procesoEnUso[0]
                    env = procesoEnUso[1]
                    memoria = procesoEnUso[2]
                    llegada = procesoEnUso[3]
                    tiempoEnCPU = tiempoEnCPU
                    UsoRam = procesoEnUso[5]
                    listaIO.pop(llave)
                    
                    #listaCPU[nombre] = procesoEnUso
                    #listaCPU.pop(llave2)
                    
                    
                    env.process(proceso(nombre, env, memoria, llegada, tiempoEnCPU, UsoRam))
                    
                #else:
                    #listaIO[llaves[0]] = listaIO.get(llaves[0])
                    
                        
                    
            #memoria.put(usoRam)
            
            #if len(listaProcesos) > 0:
                #llave2 = list(listaProcesos.items())[0][0]
                #listaCPU[llave2] = listaProcesos.get(llave2)
                #listaProcesos.pop(llave2)
                
            #else:
                #llave2 = list(listaCPU.items())[0][0]
            
            
            
            
            
            #else:
                #listaIO[nombre] = listaProcesos.get(nombre)
                #print('%s en cola Waiting -- %s' % (nombre, env.now))
                #listaProcesos.pop(nombre)

    
    

                
         
        
                
            
        

for i in range (len(listaProcesos)):
    iString = str(i)
    procesoEnUso = listaProcesos.get("proceso " +iString)
    nombre = procesoEnUso[0]
    env = procesoEnUso[1]
    memoria = procesoEnUso[2]
    llegada = procesoEnUso[3]
    tiempoEnCPU = procesoEnUso[4]
    UsoRam = procesoEnUso[5]
    TiempoInicial[nombre] = llegada
    env.process(proceso(nombre, env, memoria, llegada, tiempoEnCPU, UsoRam)) 
    



# correr la simulacion
env.run()
