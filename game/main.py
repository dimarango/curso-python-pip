import random

def game_logic():

  user_option = input('''Elije entre:

  1) Piedra

  2) Papel

  3) Tijeras

  (Introduce el número de tu elección)

  ''' )

  computer_option = random.choice(["Piedra", "Papel", "Tijeras"])

  if user_option == "1":

    user_option = "Piedra"

    if computer_option == "Tijeras":

      print("El usuario eligió" , user_option)

      print("La computadora eligió" , computer_option)

      print("Felicidades, usted ha ganado!")

    elif computer_option == "Papel":

      print("El usuario eligió" , user_option)

      print("La computadora eligió" , computer_option)

      print("La computadora ha ganado!")

    else:

      print("Es un empate!")

  elif user_option == "2":

    user_option = "Papel"

    if computer_option == "Piedra":

      print("El usuario eligió" , user_option)

      print("La computadora eligió" , computer_option)

      print("Felicidades, usted ha ganado!")

    elif computer_option == "Tijeras":

      print("El usuario eligió" , user_option)

      print("La computadora eligió" , computer_option)

      print( "La computadora ha ganado!")

    else:

      print("Es un empate!")

  elif user_option == "3":

    user_option = "Tijeras"

    if computer_option == "Papel":

      print("El usuario eligió" , user_option)

      print("La computadora eligió" , computer_option)

      print("Felicidades, usted ha ganado!")

    elif computer_option == "Piedra":

      print("El usuario eligió" , user_option)

      print( "La computadora eligió" , computer_option)

      print("La computadora ha ganado!")

    else:

      print("Es un empate!")

  else:

    print("Esa no es una jugada válida!")

    print('''

    Reiniciando el programa...

    

    

    ''')

    game_logic()

if __name__ == "__main__":

  game_logic()