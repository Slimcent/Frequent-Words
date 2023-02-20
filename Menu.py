def __validate_user_selection(user_choice):
    while True:
        try:
            user_choice = int(input(user_choice))
        except ValueError:
            print("Invalid number")
            continue
        else:
            if user_choice == 1 or user_choice == 2 or user_choice == 3:
                return user_choice
            else:
                print("Invalid selection")
                user_choice = user_choice


def menu_display():
    menu = __validate_user_selection("press 1 for Pattern Count "
                                     "\nPress 2 for Frequency Map \nPress 3 for Frequent Words\n")
    return menu
