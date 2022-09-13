import random
import monday

print("Bienvenido a Tic tac toe contra Monday")
print("----------------------")
monday.talk("Bienvenido a Tic Tac Toe")

possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
cols = 3

def printGameBoard():
  for x in range(rows):
    print("\n+---+---+---+")
    print("|", end="")
    for y in range(cols):
      print("", gameBoard[x][y], end=" |")
  print("\n+---+---+---+")

def modifyArray(num, turn):
  num -= 1
  if(num == 0):
    gameBoard[0][0] = turn
  elif(num == 1):
    gameBoard[0][1] = turn
  elif(num == 2):
    gameBoard[0][2] = turn
  elif(num == 3):
    gameBoard[1][0] = turn
  elif(num == 4):
    gameBoard[1][1] = turn
  elif(num == 5):
    gameBoard[1][2] = turn
  elif(num == 6):
    gameBoard[2][0] = turn
  elif(num == 7):
    gameBoard[2][1] = turn
  elif(num == 8):
    gameBoard[2][2] = turn

### Define function to check for a winner
def checkForWinner(gameBoard):
  ### X axis
  if(gameBoard[0][0] == 'X' and gameBoard[0][1] == 'X' and gameBoard[0][2] == 'X'):
    print("Haz ganado")
    monday.talk('Buena partida')
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[0][1] == 'O' and gameBoard[0][2] == 'O'):
    print("Monday ganó!")
    monday.talk('Gané, suerte para la proxima')
    return "O"
  elif(gameBoard[1][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[1][2] == 'X'):
    print("Haz ganado")
    monday.talk('Buena partida')
    return "X"
  elif(gameBoard[1][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[1][2] == 'O'):
    print("Monday ganó!")
    monday.talk('Gané, suerte para la proxima')
    return "O"
  elif(gameBoard[2][0] == 'X' and gameBoard[2][1] == 'X' and gameBoard[2][2] == 'X'):
    print("Haz ganado")
    monday.talk('Buena partida')
    return "X"
  elif(gameBoard[2][0] == 'O' and gameBoard[2][1] == 'O' and gameBoard[2][2] == 'O'):
    print("Monday ganó!")
    monday.talk('Gané, suerte para la proxima')
    return "O"
  ### Y axis
  if(gameBoard[0][0] == 'X' and gameBoard[1][0] == 'X' and gameBoard[2][0] == 'X'):
    print("Haz ganado")
    monday.talk('Buena partida')
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[1][0] == 'O' and gameBoard[2][0] == 'O'):
    print("Monday ganó!")
    monday.talk('Gané, suerte para la proxima')
    return "O"
  elif(gameBoard[0][1] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][1] == 'X'):
    print("Haz ganado")
    monday.talk('Buena partida')
    return "X"
  elif(gameBoard[0][1] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][1] == 'O'):
    print("Monday ganó!")
    monday.talk('Gané, suerte para la proxima')
    return "O"
  elif(gameBoard[0][2] == 'X' and gameBoard[1][2] == 'X' and gameBoard[2][2] == 'X'):
    print("Haz ganado")
    monday.talk('Buena partida')
    return "X"
  elif(gameBoard[0][2] == 'O' and gameBoard[1][2] == 'O' and gameBoard[2][2] == 'O'):
    print("Monday ganó!")
    monday.talk('Gané, suerte para la proxima')
    return "O"
  ### Cross wins
  elif(gameBoard[0][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][2] == 'X'):
    print("Haz ganado")
    monday.talk('Buena partida')
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][2] == 'O'):
    print("Monday ganó!")
    monday.talk('Gané, suerte para la proxima') 
    return "O"
  elif(gameBoard[0][2] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][0] == 'X'):
    print("Haz ganado")
    monday.talk('Buena partida')  
    return "X"
  elif(gameBoard[0][2] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][0] == 'O'):
    print("Monday ganó!")
    monday.talk('Gané, suerte para la proxima') 
    return "O" 
  else:
    return "N"

leaveLoop = False
turnCounter = 0

while(leaveLoop == False):
  ### It's the player turn
  if(turnCounter % 2 == 0):
    printGameBoard()
    monday.talk('Elige un número entre 1 y 9')
    numberPicked = int(input("\nChoose a number [1-9]: "))
    #numberPicked = int(monday.play())
    if(numberPicked == 0):
      print("Número inválido. Por favor prueba otro")
      monday.talk('número inválido. Por favor prueba otro')
    elif(numberPicked >= 1 or numberPicked <= 9):
      print(numberPicked)
      modifyArray(numberPicked, 'X')
      possibleNumbers.remove(numberPicked)
      turnCounter += 1
    else:
      print("Número inválido. Por favor prueba otro")
      monday.talk('número inválido. Por favor prueba otro')
    
  ### It's the computer's turn
  else:
    while(True):
      cpuChoice = random.choice(possibleNumbers)
      print("\nElección de Monday: ", cpuChoice)
      elec = str(cpuChoice)
      monday.talk('Elegí ' + elec)
      if(cpuChoice in possibleNumbers):
        modifyArray(cpuChoice, 'O')
        possibleNumbers.remove(cpuChoice)
        turnCounter += 1
        break
  
  winner = checkForWinner(gameBoard)
  if(winner != "N"):
    print("\nFin del juego! gracias por jugar conmigo:)")
    monday.talk('gracias por jugar conmigo')
    break