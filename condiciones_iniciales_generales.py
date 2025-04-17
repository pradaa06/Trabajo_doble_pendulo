def condiciones_iniciales_generales():



    import cinematica as cin
    from condiciones_iniciales_interactivas import condiciones_iniciales_interactivas
    import numpy as np
    '''
    variables = [theta1, theta2, w1, w2]
    condiciones = [[variables], L1, L2, m1, m2, tf, deltat]


    Este programa se encarga de gestionar las condiciones iniciales del doble pendulo,
    haciendo uso si se solicita del modulo que las gestiona de forma interactiva
    '''


    encabezado = "Este programa va a calcular la posición a lo largo del tiempo de un\
    doble pendulo en el que la primera masa m1\nforma un ángulo theta1 con la vertical y\
    cuelga de un hilo de longitud L1. De m1 cuelga una masa m2 que forma un ángulo\ntheta2\
    con la vertical desde un hilo con longitud L2\n"

    print(encabezado)


    #Selección de método de entrada
    metodo = str(input('¿De qué forma desea introducir los datos, Interactiva o Fichero? (I/F): ')).lower()
    while (metodo != 'i' and metodo != 'f'):
        print('El metodo seleccionado no es valido')
        metodo = str(input('¿De qué forma desea introducir los datos, Interactiva o Fichero? (I/F): ')).lower()



    #Selección del tiempos durante el que se va a calcular y en cuantos intervalos?
    tf = eval(input('¿Durante qué cantidad de segundos desea calcular el doble péndulo?: '))
    deltat = eval(input('¿Cuanto quiere que duren los intervalos de tiempo en segundos?: '))

    condiciones = []
    if metodo == 'i':
        npendulos = eval(input('¿Cuántos pendulos desea calcular?: '))
        
        for pendulo in range(npendulos):
            x1n,y1n, x2n, y2n, m1n,m2n  = condiciones_iniciales_interactivas()
            L1, theta1 = cin.cartesianas_a_polares(y1n,x1n)
            L2, theta2 = cin.cartesianas_a_polares(y2n-y1n, x2n-x1n)
            condiciones_n = np.asarray([np.asarray([theta1, theta2, 0, 0]), L1, L2, m1n, m2n, tf, deltat]).T
            condiciones.append(condiciones_n)
        print(condiciones)

        
    if metodo == 'f':
        direccion = str(input('Introduce la ruta del archivo que se desea leer: ')) #/media/uo306033@aulasuo.uniovi.es/0657-E7AA/IFC-Practicas/segundo-semestre/TRABAJO-DOBLE-PENDULO/data2.txt
        todo = np.loadtxt(direccion)
        if todo.ndim == 1:
            variables = np.array(todo[0:4])
            condiciones = [np.array([variables,todo[4],todo[5], todo[6], todo[7], tf, deltat])]
            #print(variables)
        else:
            variables = np.split(todo[:,0:4], np.shape(todo)[0])
            #print(todo)
            #print(variables)
            condiciones = [np.array([variables[i],todo[i,4],todo[i,5], todo[i,6], todo[i,7], tf, deltat]) for i in range(np.shape(todo)[0])]
        #print(todo)
        #print(variables)
        #print(condiciones)
    
    return condiciones
    
    
