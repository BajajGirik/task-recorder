import questionary
from constants import TASK_MENU_CHOICES, TASK_PRIORITY_CHOICES
from db import tasks_db, projects_db


def task_menu():
    task_menu_option = questionary.select(
        "Task Menu:",
        choices=TASK_MENU_CHOICES,
        use_arrow_keys=True,
        use_jk_keys=True,
    ).ask()

    match task_menu_option:
        case 1:
            for task in tasks_db.get_all():
                print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}")

        case 2:
            row = {}
            row["title"] = questionary.text("Enter title:").ask()
            row["description"] = questionary.text("Enter description:").ask()

            row["priority"] = questionary.select(
                "Select priority:",
                choices=TASK_PRIORITY_CHOICES,
            ).ask()

            row["projects"] = questionary.checkbox(
                "Projects involved:",
                choices=[questionary.Choice(row["title"], row["id"]) for row in projects_db.get_all()],
            ).ask()

            tasks_db.add(row)

        case 3:
            task_id = questionary.select(
                "Select task to delete:",
                choices=[questionary.Choice(task['title'], task['id']) for task in tasks_db.get_all()],
            ).ask()

            task = tasks_db.get_by_id(task_id)

            row = {}
            row["title"] = questionary.text("Enter title:", task["title"]).ask()
            row["description"] = questionary.text("Enter description:", task["description"]).ask()

            row["priority"] = questionary.select(
                "Select priority:",
                choices=TASK_PRIORITY_CHOICES,
                default=task["priority"],
            ).ask()

            projects = projects_db.get_all()
            project_choices = [questionary.Choice(row["title"], row["id"]) for row in projects]

            row["projects"] = questionary.checkbox(
                "Projects involved:",
                choices=project_choices,
                default=task["projects"],
            ).ask()

            tasks_db.update(row)

        case 4:
            task_id = questionary.select(
                "Select task to delete:",
                choices=[questionary.Choice(task['title'], task['id']) for task in tasks_db.get_all()],
            ).ask()

            tasks_db.delete(task_id)
        
        case _:
            print("Invalid option selected.")