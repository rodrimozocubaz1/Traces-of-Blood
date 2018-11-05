label secuestro:
    stop music fadeout 3.0
    
    e"Buena suerte en tu misión"
        
    hide guia
    hide escena_pantalla_princ
    with fade
    
    #se muestra el escenario de un aeropuerto
    
    "El día 24 de Octubre del año 20XX en una inauguración de un programa académico de la USIL Miami,
      aproximadamente a las 10 a.m., secuestraron al Presidente del Directorio de la USIL"
    "La indentidad de los secuestradores es desconocida hasta ahora pero los han categorizado como una mafia
      internacional"
    "Esta mafia ha impuesto unas condiciones para el rescate del rehén, tienen que entregarles 2 millones de
      dólares en efectivo"
    "Por las características del secuestro y la solicitud de rescate, se hace necesario un personaje incógnito 
      para ayudar en las investigaciones de la policía USA-Miami para ubicar y rescatar al Presidente de la USIL"
    "El directorio de la USIL en Perú ha tomado la decisión de enviar un detective privado para apoyar las investigaciones
      y localización del secuestrado"
    "La policía de EEUU aceptó la propuesta del directorio y ha accedió a establecer un enlace con este detective
      en forma secreta y paralela, para sorprender a la mafia organizada que lleva a cabo el secuestro"
    "Se cuenta con 5 días para su rescate y/o muerte del Empresario"
    "El contacto de la policía de EEUU es un capitán de sexo femenino experta en solución de secuestros
      y destacada especialista en criminalística"
    "Fin del mensaje, buena suerte"
    
    #agregar al detective(perso principal) a la escena
    
    d"Conque eso es todo, eh?"
    d"Bueno, eso explica el porqué sabías de mi llegada, no es así?{w=1} Señora capitán~"
    
    #se muestra el personaje de la capitan
    
    c"Señorita! y no me digas capitán en público, no olvides que estamos en cubierto, nunca se sabe quien nos está
      escuchando"
    c"Solo llámame {color=99FF99}Teresa{/color}"
    cn"Ese es mi nombre"
    
    d"Entonces Teresa, será un gusto trabajar contigo"
    
    cn"Lo mismo digo, amm..."
    
    d"Oh! Lo siento, aún no me he presentado, mi nombre es..."
    
    # esto en el "label start:"
    $ povname = renpy.input("¿Cuál es tu nombre?")
    dn "Mi nombre es [dn]"
    
    cn"Bueno [dn] ahora que hemos terminado de presentarnos daremos inicio a la investigación"
    cn"¿Con qué deberíamos empezar?"
    
    dn"Creo que deberiamos investigar el lugar donde el presidente estuvo alojado el día anterior al secuestro
       y también sus últimas comunicaciones, ya sean escritas, verbales o telefónicas"
    
    cn"Entonces empecemos con el alojamiento, el Presidente de la USIL se hospedó en un hotel llamado {color=FFCC33}All Star{/color}"
    dn"All Star, no? Vamos"
    
    "Después de eso nos dirigimos hacia el hotel en el coche de Teresa, cuando llegamos inmediatamente nos pusimos a investigar las instalaciones
     y el cuarto de la víctima pero no hubo resultados positivos"
    "Horas más tarde rentamos la misma habitación en donde se hospedó el Presidente"
    
    # habitacion hotel 
    
    cn"Investigamos cada rincón del hotel y aún así no encontramos ninguna pista, que decepción"
 
    dn"Aún no podemos estar seguros de eso, tiene que haber algo, lo sé"
    
    "Decidí salir de la habitación para refrescar mi mente; momentos después, cuando caminaba por los 
     pasillos, me encontré con un señor, de unos 40 años aproximadamente"
    
    # pasillo hotel
    # mostrar señorhotel
    
    señorhotel"Hola chico, nunca te había visto por aquí,¿Eres un recién llegado?"
    
    dn"Sí señor, hoy es mi primer día en este hotel, espero que nos llevemos bien en mi corta estadía"

    señorhotel"Igualmente..."
    señorhotel"Oye, te daré un consejo, debes tener cuidado en este hotel, se han reportado casos de desapariciones,
                asi que tienes que proteger a tu {color=FFCC33}chica{/color}, ¿ok?"
    
    "El señor dijo algo que no debía de haber sabido, sé que te diste cuenta, o al menos eso espero"
    "Pero decidí continuar la conversación con normalidad"
    
    dn"Jajaja lo tendré en cuenta, muchas gracias"
    
    señorhotel"De nada, me alegra ser de ayuda, dicho esto me retiro"
    señorhotel"Hasta luego chico"
    
    "El señor se fue por las escaleras de subida y así me quedé solo"
    
    dn"Ese señor es peligroso, debo informarle de esto a Teresa"
    
    "Fui hasta la habitación y le conté que este hotel estaba sobre vigilancia enemiga, o al menos eso especulé"
    
    cn"¿Estás seguro de eso?"
    
    dn"Sólo es una corazonada, pero si se da el caso, debemos estar preparados para lo peor"
    
    cn"Entonces, ¿Qué hacemos?"
    
    dn"Esto es lo que haremos"
    
    "Me acerco a ella y le digo en el oído todo el plan"
    
    cn"Ya veo, pero será peligroso"
    
    dn"Descuida, aunque no lo creas soy fuerte"
    
    cn"Está bien, confiaré en ti"
    
    "Media hora después Teresa dejó la habitación en la que nos encontrábamos"
    
    dn"Bueno, ¿Y ahora que hago?"
    
    menu:
        
        "Dormir para recargar energía":
            $flag="dormir"
            jump muerte1
            
        "Quedarme haciendo guardia toda la noche":
            $flag="plan"
            jump continuar1
            
#-------------------------------------------------------------------------------------------------------------------------------------------------------            
    if flag=="dormir":
        label muerte1:
            dn"Creo que dormiré por el momento, despuésde todo no hay nada mejor que hacer"
            
            "Me tiré a la cama e inmediatamente me quedé dormido,sin preocuparme por nada, fui un estúpido..."
            
            "Al día siguiente Teresa me encontró muerto, con un cuchillo enterrado en mi corazón"
            
            # pantalla oscura
            
            e"Moriste, ¿Quieres volver a intentarlo?"
            
            menu:
                "Sí":
                    $flag="sí"
                    
                "No":
                    return
                    
            if flag=="sí":
                
                dn"Bueno, ¿Y ahora que hago?"
                
                menu:
        
                    "Dormir para recargar energía":
                        $flag="dormir"
                        jump muerte1
                        
                    "Quedarme haciendo guardia toda la noche":
                        $flag="plan"
                        jump continuar1
                        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------    
    if flag=="plan":
        label continuar1:
            dn"Creo que me quedaré despierto, no quiero que alguien me agarre con la guardia baja"
            
            "Pasaron la horas pero nada ocurría, todo estaba muy silencioso y oscuro, tan oscuro que me hacía pensar que estaba ciego"
            "Ya no podía más, mis párpados ya no aguantaban las ganas de caer rendidos"
            "Cada vez que pareciese que cayecen, yo forzosamente trataba de levantarlos, era una batalla contra el sueño"
            "Y así pasaron las horas..."
            "Hasta que de pronto escuché un ruido por la cocina, ese ruido me puso inmediatamente en guardia, todo mi sueño se había esfumado"
            "Se escuchaban los pasos de una persona, recorriendo por toda la sala"
            
            dn"¿Qué es lo que hago ahora?"
            
            menu:
                
                "Buscar algún objeto con el cual poder defenderme":
                    $flag="defensa"
                    jump continuar2
                    
                "Caminar sigilosamente hacia el sonido de los pasos en la sala":
                    $flag="chisme"
                    jump muerte2
#--------------------------------------------------------------------------------------------------------------------------------------------------------------                    
            if flag=="chisme":
                label muerte2:
                    "Caminé hacia el sonido sin hacer algún tipo de ruido, caminé lo más ligero posible para no alertar al usurpador de mi llegada"
                    "Al llegar a la entrada a la sala sentí que la presión que sentía comenzaba a aumentar pero ya era muy tarde para retroceder"
                    "Gire la manija y abrí la puerta muy lentamente, solo moví la puerta a un espacio para que puediera mirar con un ojo"
                    "Procedí a acercar mi cara al espacio entre mi cuarto y la sala, cuando finalmente podía ver hacia el otro lado toda mi vista de la parte
                     derecha se volvió oscura"
                    
                    dn"Eh?...{w=2}{size=+9}¡¡¡¡¡¡AAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHH!!!!!!{/size}"
                    
                    "Cuando me di cuenta de lo que había pasado pegué un grito de desesperación y caí al suelo"
                    "Me habían clavado un cuchillo en el ojo derecho, mis prendas estaban manchadas por mi sangre, no podía creerlo, toda esa mancha roja 
                     era mi sangre"
                    "Se escuchaban las pisadas en la sala mucho... mucho más cerca a mi ubicación, el sujeto abrió la puerta rápidamente con un arma en mano
                     y sin siquiera dudarlo apretó el gatillo una y otra y otra y otra y otra y otra y otra y otra vez hasta quedarse sin balas"
                    "Sin siquiera ver el rostro del culpable morí"
                    
                    e"¿Quieres volver a intentarlo?"
                    
                    menu:
                        
                        "Sí":
                            $flag="sí1"
                            
                        "No":
                            return
                            
                    if flag=="sí1":
                        dn"¿Qué es lo que hago ahora?"
            
                        menu:
                
                            "Buscar algún objeto con el cual poder defenderme":
                                $flag="defensa"
                                jump continuar2
                                
                            "Caminar sigilosamente hacia el sonido de los pasos en la sala":
                                $flag="chisme"
                                jump muerte2
 #------------------------------------------------------------------------------------------------------------------------------------------------------                       
            if flag=="defensa":
                label continuar2:
                    "Caminé sigilosamente hacia mis cajones porque ahí se encontraba el arma que me había entregado Teresa antes de irse"
                    #mostrar flashback
                            
                
    
    
    # Finaliza el juego:
    return