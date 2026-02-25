import random
'''
ARQUITECTURA DEL SISTEMA
def run(): # funcion principal del juego (correr)
    init() # inicializar el juego o el sistema
    while True: # ciclo principal del juego
        processInput() # recibir y procesar la entrada del jugador
        update() # actualizar el estado del juego
        render() # generar la salida o mostrar el resultado al jugador
'''

def init():
    '''
    Propósito: inicializar el juego
    Inputs: ninguno
    Outputs:
    gameStatus: estado del juego, por ahora es None, pero lo usaremos mas adelante
    magicNumber: el numero secreto que el jugador debe adivinar, generado aleatoriamente entre 1 y 100
    '''
    print("Bienvenido al juego Adivina Mi Numero!") # mensaje de bienvenida
    return None, random.randint(1, 100)

def processInput(): # este metodo procesa las entradas del usuario
    '''
    Propósito: recibir y procesar la entrada del jugador
    Inputs: ninguno
    Outputs: numeroJugador
    '''
    while True: # ciclo de validacion de entradas
        entrada = input("Escribe un numero entre 1 y 100 o 's' para salir: ")
        if entrada.lower() == 's': # si el jugador quiere salir
            print("Gracias por jugar, hasta la proxima!")
            return None # salir del juego
        
        try: # intentar convertir la entrada a un numero entero
            numeroJugador = int(entrada) 
            break # salir del ciclo de validacion si la conversion es exitosa
        except ValueError:
            print("Por favor, ingresa un numero valido.")
            continue # volver al inicio del ciclo de validacion
     # ---------------------------------------------------   
    return numeroJugador # retornar el numero del jugador
    # ---------------------------------------------------

# esta funcion actualiza el estado del sistema
def update(gameStatus, numeroJugador, numeroSecreto):
    '''
    Proposito: aqui se maneja la 'logica de negocio' o casos del juego
    Inputs: gamestatus, numeroJugador, numeroSecreto
    Outputs: gameStatus, numeroSecreto; gamestatus actualizado
    ''' 
    # 
    if numeroJugador is None: # caso 1: salir
        gameStatus = 'salir'
    elif numeroJugador == numeroSecreto: # caso 2: adivino el numero
        gameStatus = 'ganar'
    elif numeroJugador < numeroSecreto: # caso 3: numero por debajo
        gameStatus = 'bajo'
    else: # caso 4: numero por encima
        gameStatus = 'alto'
    return gameStatus, numeroSecreto
    # retornar el nuevo estado del juego y el numero secreto

def render(gameStatus, numeroSecreto):
    '''
    Proposito: esta funcion genera la salida o muestra el resultado al jugador
    Inputs: gameStatus, numeroSecreto
    Outputs: ninguno, pero muestra mensajes al jugador segun el estado del juego
    '''
    if gameStatus == 'salir': # caso 1: salir
        print("Gracias por jugar, hasta la proxima!")
    elif gameStatus == 'ganar': # caso 2: adivino el numero
        print("Felicidades! Adivinaste el numero secreto!")
    elif gameStatus == 'bajo': # caso 3: numero por debajo
        print("Numero incorrecto. El numero secreto es mas alto. Intenta de nuevo.")
    elif gameStatus == 'alto': # caso 4: numero por encima
        print("Numero incorrecto. El numero secreto es mas bajo. Intenta de nuevo.")
    else :
        raise ValueError("Estado del juego desconocido: " + str(gameStatus))
    
def runGame():
    gameStatus, numeroSecreto = init() # inicializar el juego
    # si no ha salido o no ha ganado, continuar el ciclo del juego
    while gameStatus != 'salir' and gameStatus != 'ganar': # ciclo principal del juego
        numeroJugador = processInput() # recibir y procesar la entrada del jugador
        gameStatus, numeroSecreto = update(gameStatus, numeroJugador, numeroSecreto) 
        render(gameStatus, numeroSecreto) # generar la salida o mostrar el resultado al jugador

# lanzar el juego
runGame()

            