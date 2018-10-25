# Este juego se ejecuta con el programa renpy, estamos usando el visual studio code, para simplemente guardar nuestro cambios de código"

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("detective")


# El juego comienza aquí.

label start:
     # Tiempo Límite
    $ tiempo = 20
    
    # Medidor de vida
    $ Vida = 3

    #$ renpy.music.play ("sounds/suspenso.mp3")
    
    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy

    # Presenta las líneas del diálogo.

    e "Bienvenido a tu primera misión después de graduarte de la academia de detectives "

    e "espero que puedas dar una buena demostración de lo que puedes hacer novato"

    e "existen casos que no pueden ser resueltos por la policía por más que se esfuercen"

    e "y ahí es donde entramos nosotros, los detectives"

    # Finaliza el juego:

    return
