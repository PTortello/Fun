def select_from_menu(menu_options: dict):
    selection = input('Make selection: ')
    # do some dodgy things
    action = menu_options.get(int(selection), None)
    if action is None:
        print('')
        print('Invalid selection')
        print('')
    else:
        print('')
        action()
        print('')
