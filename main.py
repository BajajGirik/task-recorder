import questionary
from constants import MAIN_MENU_CHOICES
from tasks import task_menu
from projects import project_menu


def menu():
    main_menu_option = questionary.select(
        "Main Menu:",
        choices=MAIN_MENU_CHOICES,
        use_arrow_keys=True,
        use_jk_keys=True,
    ).ask()

    match main_menu_option:
        case 1:
            task_menu()
        case 2:
            project_menu()
        case _:
            exit(1)


if __name__ == "__main__":
    while True:
        menu()