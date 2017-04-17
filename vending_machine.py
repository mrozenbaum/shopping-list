# Vending machine fun in the console
sodas = ['cherry', 'pepsi','diet', 'coke']

chips = ['doritos', 'pringles', 'ruffles', 'tortilla']

candy = ['m&m', 'chocolate', 'gummies']

while True:
    choice = input('Would you like a SODA, some CHIPS, or CANDY?').lower()
    try:

        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        else:
            print('Sorry, I didnt understand that.')
            continue
    except IndexError:
        print('Were all out of {}: sorry!'.format(choice))

    else:
        print('Heres your {}: {}'.format(choice, snack))  
