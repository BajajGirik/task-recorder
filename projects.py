import questionary
from constants import PROJECT_MENU_CHOICES
from db import projects_db
from utils import print_separator, print_header


def print_project(project):
    print(f"ID: {project['id']}")
    print(f"Title: {project['title']}")
    print(f"Description: {project['description']}")
    print(f"Created At: {project['created_at']}")
    print_separator()


def project_menu():
    project_menu_option = questionary.select(
        "Project Menu:",
        choices=PROJECT_MENU_CHOICES,
        use_arrow_keys=True,
        use_jk_keys=True,
    ).ask()

    match project_menu_option:
        case 1:
            projects = projects_db.get_all()

            print_header("Total Projects:", len(projects))

            for project in projects:
                print_project(project)

            print("")

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