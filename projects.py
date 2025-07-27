import questionary
from constants import PROJECT_MENU_CHOICES
from db import projects_db


def project_menu():
    project_menu_option = questionary.select(
        "Project Menu:",
        choices=PROJECT_MENU_CHOICES,
        use_arrow_keys=True,
        use_jk_keys=True,
    ).ask()

    match project_menu_option:
        case 1:
            for project in projects_db.get_all():
                print(f"ID: {project['id']}, Title: {project['title']}, Description: {project['description']}")

        case 2:
            row = {}
            row["title"] = questionary.text("Enter title:").ask()
            row["description"] = questionary.text("Enter description:").ask()

            projects_db.add(row)

            print("Project added successfully.")
        
        case 3:
            project_id = questionary.select(
                "Select project to update:",
                choices=[questionary.Choice(project['title'], project['id']) for project in projects_db.get_all()],
            ).ask()


            project = projects_db.get_by_id(project_id)

            row = {}
            row["title"] = questionary.text("Enter title:", project["title"]).ask()
            row["description"] = questionary.text("Enter description:", project["description"]).ask()

            projects_db.update(project_id, row)

            print("Project updated successfully.")
        
        case 4:
            project_id = questionary.select(
                "Select project to delete:",
                choices=[questionary.Choice(project['title'], project['id']) for project in projects_db.get_all()],
            ).ask()

            projects_db.delete(project_id)
        
        case _:
            print("Invalid option selected.")