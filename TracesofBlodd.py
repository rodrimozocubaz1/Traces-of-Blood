# Este juego se ejecuta con el programa renpy, estamos usando el visual studio code, para simplemente guardar nuestro cambios de código"

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Guía")
image guia = "guia.png" 



# El juego comienza aquí.

label start:
     # Tiempo Límite
    $ tiempo = 20
    
    # Medidor de vida
    $ Vida = 3

    $ renpy.music.play ("sounds/suspenso.mp3")
    
    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    image habi 2="habi 2.jpg"
    image habi 3="habi 3.jpg"
    image habi 4="habi 4.jpg"
    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show guia:
        ypos 100 xpos 270

    # Presenta las líneas del diálogo.

    e "Bienvenido a {b}Traces of blood{/b}"
    e "Este juego se trata de resolver tres casos"
    e "UNO: resolver un secuestro"
    e "DOS: resolver un homicidio"
    e "TRES: resolver un suicidio"
    e "Tú podrás elegir resolver cualquiera de estos tres casos de tu interés"
    e "Contarás con tres vidas de reposición para poder resolver tu caso iniciando nuevamente desde tu última ruta de juego"
    e "Caso contrario de agotar tu última vida reiniciarás el juego hasta que por tus habilidades y decisiones tomadas en el juego logres resolver el caso"
    e "La solución consiste en rescatar al secuestrado, identificar al homicida o determinar las razones de suicidio"
    e "Elige la opcion A, B o C:"
    
    menu:
        
        "A. Secuestro":
            jump secuestro
        
        "B. Homicidio":
            jump homicidio
        
        "C. Suicidio":
            jump suicidio

    

    
