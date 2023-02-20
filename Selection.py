import Menu
import PrintSelection


def user_selection():
    userSelection = Menu.menu_display()

    match userSelection:
        case 1:
            PrintSelection.print_pattern_count()

        case 2:
            PrintSelection.print_frequency_map()

        case 3:
            PrintSelection.print_frequent_words()
