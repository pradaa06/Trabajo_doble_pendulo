x1, y1, x2, y2, markersize1, markersize2 = 0,-1, 0, -2, 6, 6
def condiciones_iniciales_interactivas():
    global x1, y1, x2, y2, markersize1, markersize2

    '''
    Este modulo se encarga de gestionar la entrada de condiciones iniciales de forma interactiva para el problema del doble péndulo
    '''
    import matplotlib.pyplot as plt
    from matplotlib.widgets import RadioButtons, Slider, Button
    import numpy as np
    
    #Creamos la figura, delimitamos los ejes y añadimos los puntos y lineas iniciales

    fig, ax = plt.subplots(figsize = (11,9))
    plt.subplots_adjust(left = 0.25, bottom = 0.25)
    ax.set_xlim(-10,10)
    ax.set_ylim(-20,0)
    l1, = plt.plot([0,x1], [0,y1], 'k--', alpha = 0.8)
    l2, = plt.plot([x1,x2], [y1,y2], 'k--', alpha = 0.8)
    marker1, = plt.plot(x1,y1, 'bo', markersize = markersize1)
    marker2, = plt.plot(x2,y2, 'ro', markersize = markersize2)

    #Añadimos la posicion relativa de los widgets y creamos los objetos de cada widget

    axslider1 = fig.add_axes([0.25, 0.1, 0.65, 0.03]) 
    axslider2 = fig.add_axes([0.25, 0.05, 0.65, 0.03])
    axradiobutton = fig.add_axes([0.0225, 0.5, 0.15, 0.15], facecolor = 'aquamarine')
    axbutton = fig.add_axes([0.0225, 0.1, 0.10, 0.10], facecolor = 'aquamarine')



    slider1 = Slider(axslider1, 'Masa 1', 1, 20, valinit = 1, valstep = 1,color = 'b')
    slider2 = Slider(axslider2, 'Masa 2', 1, 20, valinit = 1, valstep = 1, color = 'r')
    radiobutton = RadioButtons(axradiobutton, ('Colocar Masa 1', 'Colocar Masa 2', 'Cambiar masas'))
    button = Button(axbutton, 'Confirmar', color = 'aquamarine', hovercolor = 'b')


    #Creamos las funciones que actualizan los widgets

    #DESLIZADORES
    def update_size(val):
        global markersize1, markersize2
        if radiobutton.value_selected == 'Cambiar masas':  #Detecta que el selector esté en cambiar masas
            markersize1 = 5 + slider1.val
            markersize2 = 5 + slider2.val
            marker1.set_markersize(markersize1)
            marker2.set_markersize(markersize2)   #Le asigna el nuevo tamaño a las bolas del pendulo
            fig.canvas.draw_idle()


    #DOBLE CLICK
    def update_position(event):
        global x1,y1,x2,y2
        if event.dblclick:  #Comprueba que haya un doble click (El click normal es problematico, haces click para cambiar el selector)
            if radiobutton.value_selected == 'Colocar Masa 1':   #Comprueba el selector y coje las coordenadas del doble click y se las asigna
                x1, y1 = event.xdata, event.ydata
            if radiobutton.value_selected == 'Colocar Masa 2':
                x2, y2 = event.xdata, event.ydata
            l1.set_data([0,x1], [0,y1])   #Actualiza todas las lineas y todos los marcadores y vuelve a hacer el dibujo
            l2.set_data([x1,x2], [y1,y2])
            marker1.set_data(x1,y1)
            marker2.set_data(x2,y2)
            fig.canvas.draw_idle()

    #CERRAR GRAFICA
    def close_graph(event):
        global x1,y1,x2,y2,markersize1, markersize2
        plt.close(fig)
        return x1,y1,x2,y2, markersize1, markersize2


    #Conectamos los botones a su función
    slider1.on_changed(update_size)
    slider2.on_changed(update_size)    
    fig.canvas.mpl_connect('button_press_event', update_position)
    button.on_clicked(close_graph)

    #Mostramos la grafica en la que sucede todo

    plt.show()


    return x1,y1,x2,y2, markersize1, markersize2

#fin



























