    #Sono necessarie le seguenti quattro righe di codice per poter semplicemente interrompere il programma
    events = pygame.event.get()#vengono prese tutte le azioni eseguite in input e memorizzate in questa lista
    for event in events:
        if event.type == pygame.QUIT:#se viene registrato un evento di chiusura forzata
            pygame.quit() #allora viene interrotto il programma