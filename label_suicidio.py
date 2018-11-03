 label suicidio:
        
       
       $ renpy.music.play ("sounds/Marc Shaiman - Misery's Return.mp3")
       
       scene habi 2
       
       #Presenta las lineas de dialogo
       
       e"Joe es un joven cuyo fin fue impuesto mediante el suicidio"
       e"Los motivos por los cuales se suicido hasta el dia de hoy son un misterio"
       
       scene habi 3
       
       e"Según testimonio de sus vecinos, Joe aparentemente era un joven alegre y sociable con todos.Si sufria de algun tipo de depresión ellos nunca lo notaron"
       
       scene habi 4
       
       e"La misión sera descubrir por que Joe se suicido"
       e"A continuación se mostraran los mensajes que conforman la carta que dejo Joe antes de quitarse la vida,los cuales tendras que descifrar para poder resolver el caso"
       e"¿Qué tan bueno eres con el cifrado y la encriptación de mensajes?Descubramoslo...."
       e"Lee detalladamente las siguientes lineas y trata de decifrar el mensaje,recuerda, el cifrado de Cesar consiste en reemplazar cada letra con su consecuente"
       
       $ renpy.music.play ("sounds/Friday the 13th (1980) soundtrack suite - Harry Manfredini.mp3")
       
       
        
        
       j" {size=+15}{i}DRSZUZ QNSN ONQ CDMSQN
          KZ SQHRSDYZ LD DRSZAZ BNLHDMCN KDMSZLDMSD{/i}{/size}"
    
       e"¿Que es lo que estaba comiendo lentamente a Joe?"
       
       
       
       
       menu :
           
              "A. Soledad":
                  $flag="error"
                  
                  jump opcion 
                  
              "B. Nostalgia":
                  $flag="error"
                  
                  jump opcion
                  
              "C. Tristeza":
                  $flag="correcto"
                  
                  jump acierto
                
              "D. Problemas":
                  $flag="error"
                  
                  jump opcion
                  
       if flag == "error":
           label opcion:
                e"Respuesta incorrecta, pierdes una vida"
                $ Vida -= 1
                
                if Vida == 0:
                    e"Has perdido todas tus vidas"
                    e"Serás trasladado al menu principal"
                    # Finaliza el juego:
                    return
                    
                e"sigue intentando"
                menu :
           
                  "A. Soledad":
                      $flag="error"
                      
                      jump opcion 
                      
                  "B. Nostalgia":
                      $flag="error"
                      
                      jump opcion
                      
                  "C. Tristeza":
                      $flag="correcto"
                      
                      jump acierto
                    
                  "D. Problemas":
                      $flag="error"
                      
                      jump opcion
           
       
       if flag == "correcto":
           label acierto:
                e"Buen trabajo,continuemos"
    
       
       
       
                  
        
        # Finaliza el juego:

    