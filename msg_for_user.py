def slash_N(main_part=None, second_part=None):
    """
    extacting verses of the poem from array to string.
    """

    main_part = ''
    for index, mesra in enumerate(main_part):
        if index == 0:
            # Adding poet's name to the beginning of the message
            main_part += f'«{mesra}»' + '\n'
        elif index == 2:
            # just to add some space between poem information and the poem itself
            main_part += '\n'
        else:
            main_part += mesra + '\n'
    
    second_part = ''
    for index, mesra in enumerate(second_part):
        second_part += mesra + '\n'

    return main_part, second_part