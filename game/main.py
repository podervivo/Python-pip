import random 

options = ('piedra', 'papel', 'tijera')

user_option = input('piedra, papel o tijera => ').lower().strip()
if not user_option in options:
    print('esa opcion no esta dentro de las opciones validas')
computer_option = random.choice(options)

print('User option => ', user_option)
print('Computer option => ', computer_option)


if user_option == computer_option:
    print('Empate')                                                                                                                                                                                                                                                                                                                                                                                                         
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('piedra gana a tijera')
        print('user win')
    else:
        print('papel gana a piedra')
        print('computer win')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('papel gana a tijera')
        print('user win')
    else:
        print('tijera gana a papel')
        print('computer win')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print('tijera gana a papel')
        print('user win')
    else:
        print('piedra gana a tijera')
        print('computer win')
            