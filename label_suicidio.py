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
                e"Respuesta incorrecta,sigue intentando"
                $ Vida -= 1
                if Vida == 0:
                    e"Has perdido totas tus vidas. Serás trasladdo el menú principal"
                    return
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
                e"Buen trabajo,continuemos..."
                
        j"{size=+15}{i}PTDQHZ DRBZOZQ. PTDQHZ DRBZOZQ CD LH LHRLN. CD SH.{/i}{/size}"
                                                                                      
                                                                                      
        e"¿Qué queria Joe?"
       
       
       
        menu :
           
              "A. Escapar":
                  $flag="correcto2"
                  
                  jump acierto2
                  
              "B. Morir":
                  $flag="error2"
                  
                  jump opcion2
                  
              "C. Desaparecer":
                  $flag="error2"
                  
                  jump opcion2
                
              "D. Cambiar":
                  $flag="error2"
                  
                  jump opcion2
                  
        if flag == "error2":
            
            label opcion2:
                e"Respuesta incorrecta,sigue intentando"
                $ Vida -= 1
                if Vida == 0:
                    e"Has perdido totas tus vidas. Serás trasladdo el menú principal"
                    return
               
                menu :
           
                  "A. Escapar":
                      $flag="correcto2"
                      
                      jump acierto2 
                      
                  "B. Morir":
                      $flag="error2"
                    
                      jump opcion2
                      
                  "C. Desaparecer":
                      $flag="error2"
                      
                      jump opcion2
                    
                  "D. Cambiar":
                      $flag="error2"
                      
                      jump opcion2
           
       
        if flag == "correcto2":
           label acierto2:
                e"Bien,sigamos..."
                

    
        j"{size=+15}{i}OTDCN UDQKN. ZK EHMZK. DR SNCN LH BTKOZ.{/i}{/size}"
                                                                                      
                                                                                      
        e"¿A quién culpa Joe?"
       
       
       
        menu :
           
              "A. A sus compañeros":
                  $flag="error3"
                  
                  jump opcion3
                  
              "B. A la vida":
                  $flag="error3"
                  
                  jump opcion3
                  
              "C. A su familia":
                  $flag="error3"
                  
                  jump opcion3
                
              "D. A si mismo":
                  $flag="correcto3"
                  
                  jump acierto3
                  
        if flag == "error3":
            
            label opcion3:
                e"Respuesta incorrecta,sigue intentando"
                $ Vida -= 1
                if Vida == 0:
                    e"Has perdido totas tus vidas. Serás trasladdo el menú principal"
                    return
                menu :
           
                  "A. A sus compañeros":
                      $flag="error3"
                      
                      jump opcion3
                      
                  "B. A la vida":
                      $flag="error3"
                      
                      jump opcion3
                      
                  "C. A su familia":
                      $flag="error3"
                      
                      jump opcion3
                    
                  "D. A si mismo":
                      $flag="correcto3"
                      
                      jump acierto3
       
        if flag == "correcto3":
           label acierto3:
                e"Vamos!! ahora se mas rapido..."   
                
       
        j"{size=+15}{i}LD OQDFTMSD ONQ PTD DRSNX UHUHDMCN.RNRN ONQPTD RH.SNCNR RNKN UHUDM.{/i}{/size}"
                                                                                      
                                                                                      
        e"¿Por qué según Joe, el estába viviendo?"
       
       
       
        menu :
           
              "A. Por su familia":
                  $flag="error4"
                  
                  jump opcion4
                  
              "B. Porque no estaba muerto":
                  $flag="error4"
                  
                  jump opcion4
                  
              "C. Porque tenia metas":
                  $flag="error4"
                  
                  jump opcion4
                
              "D. Porque si":
                  $flag="correcto4"
                  
                  jump acierto4
       
           
        if flag == "error4":
            
            label opcion4:
               e"Respuesta incorrecta,sigue intentando"
               $ Vida -= 1
               if Vida == 0:
                    e"Has perdido totas tus vidas. Serás trasladdo el menú principal"
                    return        
        
        
        menu :
               
                  "A. Por su familia":
                      $flag="error4"
                      
                      jump opcion4
                      
                  "B. Porque no estaba muerto":
                      $flag="error4"
                      
                      jump opcion4
                      
                  "C. Porque tenia metas":
                      $flag="error4"
                      
                      jump opcion4
                    
                  "D. Porque si":
                      $flag="correcto4"
                      
                      jump acierto4
                      
        if flag == "correcto4":
           label acierto4:
                e"Buen trabajo, sigamos..."
               
        
        j"{size=+15}{i}CNBSNQDR,¿DRSZM DRBTGZMCN DRSZR OZKZAQZR?MN,MN GHBD MZCZ LZK.{/i}{/size}"
                                                                                      
                                                                                      
        e"¿A quién se dirige Joe en estas líneas?"
       
       
       
        menu :
           
              "A. Padres":
                  $flag="error5"
                  
                  jump opcion5
                  
              "B. Doctores":
                  $flag="correcto5"
                  
                  jump acierto5
                  
              "C. Vecinos":
                  $flag="error5"
                  
                  jump opcion5
                
              "D. Amigos":
                  $flag="error5"
                  
                  jump opcion5
        
         
        if flag == "error5":
            
            label opcion5:
                 e"Respuesta incorrecta,sigue intentando"
                 $ Vida -= 1
                 if Vida == 0:
                      e"Has perdido totas tus vidas. Serás trasladdo el menú principal"
                      return
        menu :
               
                  "A. Padres":
                      $flag="error5"
                      
                      jump opcion5
                      
                  "B. Doctores":
                      $flag="correcto5"
                      
                      jump acierto5
                      
                  "C. Vecinos":
                      $flag="error5"
                      
                      jump opcion5
                    
                  "D. Amigos":
                      $flag="error5"
                      
                      jump opcion5
                      
        if flag == "correcto5":
           label acierto5:
                e"Excelente, has demostrado tu gran capacidad intelectual.Ahora, hagamos esto un poco mas complicado."
               
        e"Veamos que tanta suerte tienes. Descubre cual es la palabra dentro de cada fórmula..."
        
        scene chico
        
        $ renpy.music.play ("sounds/Tokyo Ghoul OST - Symphonie.mp3")
          
        j"{size=+10}{i} Estaba con sufrimiento y preocupaciones. Nunca aprendi como convertir el aburrimiento y los(8d+1s-2o+4l*3o/6r-7e)en alegría. Los(8d+1s-2o+4l*3o/6r-7e) son (8d+1s-2o+4l*3o/6r-7e).{/i}{/size}"
        
        e"¿Cuál es la palabra escondida en(8d+1s-2o+4l*3o/6r-7e)?"
          
        menu:
              
    
           
              "A. Miedos":
                  $flag="error6"
                  
                  jump opcion6
                  
              "B. Dolores":
                  $flag="correcto6"
                  
                  jump acierto6
                  
              "C. Temores":
                  $flag="error6"
                  
                  jump opcion6
                
              "D. Errores":
                  $flag="error6"
                  
                  jump opcion6
        
        if flag == "error6":
            
            label opcion6:
                  e"Respuesta incorrecta,sigue intentando"
                  $ Vida -= 1
                  if Vida == 0:
                      e"Has perdido totas tus vidas. Serás trasladdo el menú principal"
                      return
        menu:
              
    
           
              "A. Miedos":
                  $flag="error6"
                  
                  jump opcion6
                  
              "B. Dolores":
                  $flag="correcto6"
                  
                  jump acierto6
                  
              "C. Temores":
                  $flag="error6"
                  
                  jump opcion6
                
              "D. Errores":
                  $flag="error6"
                  
                  jump opcion6   
            
        if flag == "correcto6":
           label acierto6:
                 e"Bien! Has acertado.Continuemos..."
            
        j"{size=+10}{i}¿A qué se refieren con encontrar porqué estaba(7d-2o+5c*1a+8n-0a/9s)?¿Deseas que haya más detrás de la historia{/i}{/size}?"
         
        e"¿Qué palabra se esconde en (7d-2o+5c*1a+8n-0a/9s)?"
        
        menu:
              
    
           
              "A. ido":
                  $flag="error7"
                  
                  jump opcion7
                  
              "B. deprimido":
                  $flag="error7"
                  
                  jump opcion7
                  
              "C. cansado":
                  $flag="correcto7"
                  
                  jump acierto7
                
              "D. aturdido":
                  $flag="error7"
                  
                  jump opcion7
        
        if flag == "error7":
            
            label opcion7:
                  e"Respuesta incorrecta,sigue intentando"
                  $ Vida -= 1
                  if Vida == 0:
                      e"Has perdido totas tus vidas. Serás trasladdo el menú principal"
                      return
        menu:
              
    
           
              "A. ido":
                  $flag="error7"
                  
                  jump opcion7
                  
              "B. deprimido":
                  $flag="error7"
                  
                  jump opcion7
                  
              "C. cansado":
                  $flag="correcto7"
                  
                  jump acierto7
                
              "D. aturdido":
                  $flag="error7"
                  
                  jump opcion7 
         
         
        if flag == "correcto7":
           label acierto7:
                 e"Correcto, continuemos..."
         
         
        j"{size=+10}{i} Ya les conté la historia.No estaban pretendiendo escuchar ¿verdad?, Lo que puede ser superado, no deja(1c+9c-2a*5c-4e/0s*8i-3t+2i/4r).{/i}{/size}"         
        e"Según Joe, que no deja lo que puede ser superado?"
        
        menu:
            
              "A. Cicatricez":
                  $flag="correcto8"
                  
                  jump acierto8
                  
              "B. Marcas":
                  $flag="error8"
                  
                  jump opcion8
                  
              "C. Huellas":
                  $flag="error8"
                  
                  jump opcion8
                
              "D. Rastro":
                  $flag="error8"
                  
                  jump opcion8
        
        if flag == "error8":
            
            label opcion8:
                  e"Respuesta incorrecta,sigue intentando"
                  $ Vida -= 1
                  if Vida == 0:
                      e"Has perdido totas tus vidas. Serás trasladdo el menú principal"
                      return
        menu:
            
              "A. Cicatricez":
                  $flag="correcto8"
                  
                  jump acierto8
                  
              "B. Marcas":
                  $flag="error8"
                  
                  jump opcion8
                  
              "C. Huellas":
                  $flag="error8"
                  
                  jump opcion8
                
              "D. Rastro":
                  $flag="error8"
                  
                  jump opcion8
         
        if flag == "correcto8":
           label acierto8:
                 e"Buen trabajo.Cada vez estas mas cerca de descubrir la verdad..."
        
        
        $ renpy.music.play ("sounds/Kuroshitsuji II Ost - Danse Macabre -.mp3")
        
                 
        j"{size=+10}{i} Fue dificil siempre(5s*3r-0e+7o/1n+8i-2r).¿Por qué lo hacia? Era gracioso.Hasta ahora lo he aguantado bien.{/i}{/size}" 
                 
        e"¿Qué fue siempre dificil para Joe?"
            
        menu:
            
              "A. Vivir":
                  $flag="error9"
                  
                  jump opcion9
                  
              "B. Salir":
                  $flag="error9"
                  
                  jump opcion9
                  
              "C. Sonreir":
                  $flag="correcto9"
                  
                  jump acierto9
                
              "D. Reir":
                  $flag="error9"
                  
                  jump opcion9
        
        if flag == "error9":
            
            label opcion9:
                e"Respuesta incorrecta,sigue intentando"
                $ Vida -= 1
                if Vida == 0:
                    e"Has perdido totas tus vidas. Serás trasladdo el menú principal"
                    return
                 
        menu:
            
              "A. Vivir":
                  $flag="error9"
                  
                  jump opcion9
                  
              "B. Salir":
                  $flag="error9"
                  
                  jump opcion9
                  
              "C. Sonreir":
                  $flag="correcto9"
                  
                  jump acierto9
                
              "D. Reir":
                  $flag="error9"
                  
                  jump opcion9
        
        if flag == "correcto9":
            label acierto9:
                e"Bien! Estas a solo un paso...."
                
                
        j"{size=+10}{i} ¿Qué otras palabras hay? Solo digan-(3h+1z+2a-8l+0o+3b*2e/1i*0n-1h+3c/5h*9o+4e)-.Con tan poco esta bien.{/i}{/size}"
        j"{size=+10}{i} Solo diganme eso.Incluso aunque no puedas sonreir o reir, no me heches la culpa.{/i}{/size}"
        j"{size=+10}{i} Ustedes han trabajado duro.Ustedes han pasado por mucho. Adiós. {/i}{/size}"
        
        
        e"¿Qué quería Joe que le dijeran?"
        
            
        menu:
            
              "A. Eres importante":
                  $flag="error10"
                  
                  jump opcion10
                  
              "B. Lo has logrado":
                  $flag="error10"
                  
                  jump opcion10
                  
              "C. Eres unico":
                  $flag="error10"
                  
                  jump opcion10
                
              "D. Lo has hecho bien":
                  $flag="correcto10"
                  
                  jump acierto10
        
        if flag == "error10":
            
            label opcion10:
                  
                  e"Respuesta incorrecta,sigue intentando"
                  $ Vida -= 1
                  if Vida == 0:
                        e"Has perdido totas tus vidas. Serás trasladdo el menú principal"
                        return
                  
        menu:
            
              "A. Eres importante":
                  $flag="error10"
                  
                  jump opcion10
                  
              "B. Lo has logrado":
                  $flag="error10"
                  
                  jump opcion10
                  
              "C. Eres unico":
                  $flag="error10"
                  
                  jump opcion10
                
              "D. Lo has hecho bien":
                  $flag="correcto10"
                  
                  jump acierto10
                  
                  
        if flag == "correcto10":
            label acierto10:
                e"Felicitaciones! Has hecho un buen trabajo.Lograste descifrar la carta de Joe"
        
        
        scene carta
        
        $ renpy.music.play ("sounds/musica de fondo (terror).mp3")
        
        e"Ahora que ya descifraste el mensaje que dejo Joe antes de su muerte podemos deducir que las causas que lo impulsaron a que se quite la vida fueron..."
        e"el no sentirse lo suficientemente bueno en lo que hacia, sentir que vivia por el simple hecho de que todos lo hacian, sonreir cuando no tenia motivo para hacerlo......"
        e"se podria decir que Joe se canso no de la vida, Joe se canso de su vida y acabo con ella..."
        
        
        
        
        
        
                 
                 
                 
                 
                 
                 
                 
                 
         
        # Finaliza el juego:

    