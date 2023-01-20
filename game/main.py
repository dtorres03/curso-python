import random


def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('Elige piedra, papel o tijera => ')
    user_option = user_option.lower()
    
    if not user_option in options:
        print('Esa no es una opcion valida')
        return None, None
    
    computer_option = random.choice(options)
    
    print('Tú escogiste =>', user_option)
    print('La computadora escogio =>', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Es un empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('Ganaste!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('Gana la computadora')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('Ganaste!')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('Gana la computadora')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('Ganaste!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('Gana la computadora')
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        
        print('computer_wins', computer_wins)
        print('user_wins', user_wins)
        rounds += 1
        
        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        
        if computer_wins == 2:
            print('El ganandor es la computadora')
            break
        
        if user_wins == 2:
            print('El usuario es el ganador')
            break
        
run_game()