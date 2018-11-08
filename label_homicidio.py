label homicidio:
    stop music fadeout 3.0
    $ renpy.music.play ("sounds/Stranger Things Opening Title Music (Extended).mp3")
    
    e"Suerte en tu misión, porque la necestirás"
    #Se muestran las imagenes de la historia
    
    scene golpe
    with fade
    e"La familia de Lucas era normal como cualquier otra, o al menos eso aparentaban. 
      El mayor defecto que podían tener, es que discutían demasiado, incluso hasta llegar a los golpes." 
    scene acuchillado
    with fade
      
    e"Inesperadamente, el 25 de septiembre, aparece el padre de Lucas acuchillado, en la sala de su casa."
    scene x
    show guia:
        ypos -140 xpos 465
    e"Yo te acompañaré en esta misión. Empecemos con los datos obtenidos de los entrevistados"
    e"-La madre de Lucas cuenta que no vio regresar a su esposo, pues salió a beber con sus amigos y supuso que regresaría muy tarde, así que se fue a dormir."
    e"-Un vecino dice que lo vio regresar en la madruga solo a su casa y muy ebrio."
    e"-Y Lucas no ha querido pronunciar ni una sola palabra con respecto al caso, quizás porque la tristeza lo consume."
    e"Nuestra misión será averiguar quién mato al padre de Lucas."
    hide guia
    with dissolve
    scene acuchillado
    with fade
    
    e"Primero empecemos descartando al menos culpable de la muerte. Tendrás que razonar bastante!!!"
    menu :
           
          "A. Madre de Lucas":
              $flag="error"
              
              jump error 
              
          "B. Lucas":
              $flag="error"
              
              jump error
              
          "C. Amigos del padre de Lucas":
              $flag="error"
              
              jump error
            
          "D. Vecinos":
              $flag="correcto"
              
              jump correcto
    if flag == "error":
           label error:
                e"Respuesta incorrecta, pierdes una vida."
                $ Vida -= 1
                
                if Vida == 0:
                    e"Has perdido todas tus vidas"
                    e"Serás trasladado al menu principal"
                    # Finaliza el juego:
                    return
                    
                e"sigue intentando"
                menu :
           
                  "A. Madre de Lucas":
                      $flag="error"
                      
                      jump error
                      
                  "B. Lucas":
                      $flag="error"
                      
                      jump error
                      
                  "C. Amigos del padre":
                      $flag="error"
                      
                      jump error
                    
                  "D. Vecinos":
                      $flag="correcto"
                      
                      jump correcto
           
       
    if flag == "correcto":
        label correcto:
            e"Muy bien has acertado, obviamente los vecinos quedan descartados, pues el asesinato se realizó dentro de la casa."
            
    scene x
    show guia:
        ypos -140 xpos 465
    with dissolve
    
    e"Además un dato extra que se obtuvo al entrevistar a un vecino, es que el papa de Lucas era una persona muy agresiva, y más cuando tomaba, por eso nadie del vecindario querría tener conflictos con él."
   
    e"Ahora avancemos por partes...... Que hay de los amigos del papa de Lucas. Los datos que obtuve para brindarte son: llevan 15 años de amistad, son promoción de la misma escuela y siempre se reúnen los fines de semana, como si fueran hermanos."               
    
    e"¿Es posible que algun amigo sea el asesino?"
    scene amigos
    with fade
      
    menu :
           
          "A. Obviamente, por envidia":
              $flag="error"
              
              jump error1 
              
          "B. No, debido al fuerte lazo que los une":
              $flag="correcto"
              
              jump correcto1
              
          "C. Tras una fuerte discusión,si":
              $flag="error"
              
              jump error1
            
          "D. Todos acordaron matarlo":
              $flag="error"
              
              jump error1
    if flag == "error":
           label error1:
                e"Respuesta incorrecta, pierdes una vida."
                $ Vida -= 1
                
                if Vida == 0:
                    e"Has perdido todas tus vidas"
                    e"Serás trasladado al menu principal"
                    # Finaliza el juego:
                    return
                    
                e"sigue intentando"
                menu :
           
                  "A. Obviamente, por envidia":
                      $flag="error"
                      
                      jump error1
                      
                  "B. No, debido al fuerte lazo que los une":
                      $flag="correcto"
                      
                      jump correcto1
                      
                  "C. Tras una fuerte discusión,si":
                      $flag="error"
                      
                      jump error1
                    
                  "D. Todos acordaron matarlo":
                      $flag="error"
                      
                      jump error1
           
       
    if flag == "correcto":
        label correcto1:
            e"Muy bien has acertado, Ya que a pesar de que se querían como si fueran hermanos, acuérdate del dato que decía que el padre de Lucas llegó a su casa sin que nadie lo acompañara, por ende quedan descartados los amigos."
            
            e"Mmmmm cada vez se pone más interesante el caso, porque despues del descarte, parece que el responsable del asesinato es un familiar."
    
    scene x
    show guia:
        ypos -140 xpos 465
    with dissolve
    
    e"Entonces por deducción solo nos quedan dos posibles asesinos............... Por lo tanto,
      
      ¿La madre de Lucas estará mintiendo al decir que estaba dormida, mientras asesinaban a su esposo?"
    scene mujer
    with fade
    menu :
           
          "A. No":
              $flag="error"
              
              jump error2 
              
          "B. Si":
              $flag="correcto"
              
              jump correcto2
              
    if flag == "error":
           label error2:
                e"Respuesta incorrecta, pierdes una vida."
                $ Vida -= 1
                
                if Vida == 0:
                    e"Has perdido todas tus vidas"
                    e"Serás trasladado al menu principal"
                    # Finaliza el juego:
                    return
                    
                e"sigue intentando"
                menu :
           
                  "A. No":
                      $flag="error"
                      
                      jump error2
                      
                  "B. Si":
                      $flag="correcto"
                      
                      jump correcto2
           
       
    if flag == "correcto":
        label correcto2:
            e"Muy bien has acertado,ya que el ser una muerte a cuchillazos, es imposible que no se haya depertado con los gritos del padre."
    
    e"¿Qué razones tendría la mamá de Lucas para matar al padre?"
    menu :
           
          "A. La encontró con una amante":
              $flag="error"
              
              jump error3 
              
          "B. Ya no lo quería":
              $flag="error"
              
              jump error3
              
          "C. Una fuerte discusión":
              $flag="correcto"
              
              jump correcto3
            
          "D. Su esposo se gasto toda su mensualidad en cerveza":
              $flag="error"
              
              jump error3
    if flag == "error":
           label error3:
                e"Respuesta incorrecta, pierdes una vida."
                $ Vida -= 1
                
                if Vida == 0:
                    e"Has perdido todas tus vidas"
                    e"Serás trasladado al menu principal"
                    # Finaliza el juego:
                    return
                    
                e"sigue intentando"
                menu :
           
                  "A. La encontró con una amante":
                      $flag="error"
                      
                      jump error3
                      
                  "B. Ya no lo quería":
                      $flag="error"
                      
                      jump error3
                      
                  "C. Una fuerte discusión":
                      $flag="correcto"
                      
                      jump correcto3
                    
                  "D. Su esposo se gasto toda su mensualidad en cerveza":
                      $flag="error"
                      
                      jump error3
           
       
    if flag == "correcto":
        label correcto3:
            e"Una de las posibles razones por la que ella podría ser la asesina, es que haya discutido con su esposo y se enojó tanto que lo mató."
    
    e"Entonces………. Deseas afirmar que la madre de Lucas es la asesina??? Ojo, esta es una pregunta reto, si te equivocas, automáticamente tu vida bajará a cero y perderás la partida."
    menu :
           
          "A. Si":
              $flag="error"
              
              jump error4 
              
          "B. No":
              $flag="correcto"
              
              jump correcto4
              
    if flag == "error":
           label error4:
                e"Respuesta incorrecta, pierdes todas tus vida."
                $ Vida = 0+0
                
                if Vida == 0:
                    e"Has perdido todas tus vidas"
                    e"Serás trasladado al menu principal"
                    # Finaliza el juego:
                    return
                    
                e"sigue intentando"
                menu :
           
                  "A. Si":
                      $flag="error"
                      
                      jump error4
                      
                  "B. No":
                      $flag="correcto"
                      
                      jump correcto4
           
       
    if flag == "correcto":
        label correcto4:
            e"Muy bien has superado el reto, estas mejorando como detective, ya que obviamente no puedes cerrar un caso con tan pocas conclusiones. Es más tenemos una buena noticia para ti, nos acaba de llegar un análisis de las huellas encontradas en la escena del crimen"
    e"¿Desea ver los resultados del análisis?"
    menu :
           
          "A. No, el caso esta ez, ya se quién es el asesino":
              $flag="error"
              
              jump error5 
              
          "B. Así es, un buen detective lo haría":
              $flag="correcto"
              
              jump correcto5
              
    if flag == "error":
           label error5:
                e"Respuesta incorrecta, pierdes una vida."
                $ Vida -=1
                
                if Vida == 0:
                    e"Has perdido todas tus vidas"
                    e"Serás trasladado al menu principal"
                    # Finaliza el juego:
                    return
                    
                e"sigue intentando"
                menu :
           
                  "A. No, el caso esta ez, ya se quién es el asesino":
                      $flag="error"
                      
                      jump error5
                      
                  "B. Así es, un buen detective lo haría":
                      $flag="correcto"
                      
                      jump correcto5
           
       
    if flag == "correcto":
        label correcto5:
            e"Claro un detective nunca se debe confiar. Los resultados del análisis dice que efectivamente no son las huellas de la madre, ya que corresponde a un lazo sanguíneo."
    scene x
    show guia:
        ypos -140 xpos 465
    with dissolve
    e"Estos son los posibles asesinos, según el análisis. ¿Quién podría ser?"
    scene sospechosos
    with fade
    menu :
           
          "A. Tío":
              $flag="error"
              
              jump error6
              
          "B. Hijo":
              $flag="correcto"
              
              jump correcto6
              
          "C. Sobrino":
              $flag="error"
              
              jump error6
            
              
    if flag == "error":
           label error6:
                e"Respuesta incorrecta, pierdes una vida."
                $ Vida -= 1
                
                if Vida == 0:
                    e"Has perdido todas tus vidas"
                    e"Serás trasladado al menu principal"
                    # Finaliza el juego:
                    return
                    
                e"sigue intentando"
                menu :
           
                  "A. Tío":
                      $flag="error"
                      
                      jump error6
                      
                  "B. Hijo":
                      $flag="correcto"
                      
                      jump correcto6
                      
                  "C. Sobrino":
                      $flag="error"
                      
                      jump error6
                    
           
       
    if flag == "correcto":
        label correcto6:
            e"Asi es, el hijo era el único que se encontraba en la casa, ninguno de los demás estaba de visita."
    show guia
    e"¿Qué motivo tendría el adolescente para matar a su padre?"
    menu :
           
          "A. No le quiso comprar un playstation":
              $flag="error"
              
              jump error7 
              
          "B. Lo castigaron por un año":
              $flag="error"
              
              jump error7
              
          "C. Su papá golpeaba y discutia con su madre":
              $flag="correcto"
              
              jump correcto7
            
          "D. No lo dejo ir a una fiesta":
              $flag="error"
              
              jump error7
    if flag == "error":
           label error7:
                e"Respuesta incorrecta, pierdes una vida."
                $ Vida -= 1
                
                if Vida == 0:
                    e"Has perdido todas tus vidas"
                    e"Serás trasladado al menu principal"
                    # Finaliza el juego:
                    return
                    
                e"sigue intentando"
                menu :
           
                  "A. No le quiso comprar un playstation":
                      $flag="error"
                      
                      jump error7
                      
                  "B. Lo castigaron por un año":
                      $flag="error"
                      
                      jump error7
                      
                  "C. Su papá golpeaba y discutia con su madre":
                      $flag="correcto"
                      
                      jump correcto7
                    
                  "D. No lo dejo ir a una fiesta":
                      $flag="error"
                      
                      jump error7
           
       
    if flag == "correcto":
        label correcto7:
            e"Muy bien, esta respuesta es una un paso muy fundamental para llegar a una reflexion. Todavía no saques una conclusión final."
    e"¿Cómo pudo el joven matar al padre tan fácilmente?"
    menu :
           
          "A. Lo acuchilló mientras le abría la puerta":
              $flag="error"
              
              jump error8 
              
          "B. Uso una pistola":
              $flag="error"
              
              jump error8
              
          "C. El padre aceptó que su hijo lo acuchillara":
              $flag="error"
              
              jump error8
            
          "D. El chico esperó a que su padre se durmiera por la ebriedad":
              $flag="correcto"
              
              jump correcto8
    if flag == "error":
           label error8:
                e"Respuesta incorrecta, pierdes una vida."
                $ Vida -= 1
                
                if Vida == 0:
                    e"Has perdido todas tus vidas"
                    e"Serás trasladado al menu principal"
                    # Finaliza el juego:
                    return
                    
                e"sigue intentando"
                menu :
           
                  "A. No le quiso comprar un playstation":
                      $flag="error"
                      
                      jump error8
                      
                  "B. Uso una pistola":
                      $flag="error"
                      
                      jump error8
                      
                  "C. El padre aceptó que su hijo lo acuchillara":
                      $flag="error"
                      
                      jump error8
                    
                  "D. El chico esperó a que su padre se durmiera por la ebriedad":
                      $flag="correcto"
                      
                      jump correcto8
           
       
    if flag == "correcto":
        label correcto8:
            e"Excelente, ya tienes casi todos los datos para realizar tu conclusión y entregárselo a las autoridades. "
    e"Entonces,¿cuál de todas estas opciones sería tu solución?"
    menu :
           
          "A. Madre culpable de homicidio":
              $flag="error"
              
              jump error9 
              
          "B. Madre cómplice e hijo homicida":
              $flag="correcto"
              
              jump correcto9
              
          "C. Madre e hijo inocentes, porque fue un acto en busca de paz":
              $flag="error"
              
              jump error9
            
          "D. Madre totalmente inocente e hijo culpable":
              $flag="error"
              
              jump error9
    if flag == "error":
           label error9:
                e"Respuesta incorrecta, pierdes una vida."
                $ Vida -= 1
                
                if Vida == 0:
                    e"Has perdido todas tus vidas"
                    e"Serás trasladado al menu principal"
                    # Finaliza el juego:
                    return
                    
                e"sigue intentando"
                menu :
           
                  "A. Madre culpable de homicidio":
                      $flag="error"
                      
                      jump error9
                      
                  "B. Madre cómplice e hijo homicida":
                      $flag="correcto9"
                      
                      jump correcto9
                      
                  "C. Madre e hijo inocentes, porque fue un acto en busca de paz":
                      $flag="error"
                      
                      jump error9
                    
                  "D. Madre totalmente inocente e hijo culpable":
                      $flag="error"
                      
                      jump error9
           
       
    if flag == "correcto":
        label correcto9:
            e"Felicidades, ya eres un gran detective. Date una vista por los otros niveles del juego, para que sigas mejorando tus habilidades. Gracias por jugar."
    # Finaliza el juego:

    return 