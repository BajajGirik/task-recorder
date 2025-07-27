from questionary import Choice

MAIN_MENU_CHOICES = [
    Choice("Tasks", 1),
    Choice("Projects", 2),
]

TASK_MENU_CHOICES = [
    Choice("View Tasks", 1),
    Choice("Add Task", 2),
    Choice("Edit Task", 3),
    Choice("Delete Task", 4),
]

TASK_PRIORITY_CHOICES = [
    Choice("High", "P0"),
    Choice("Medium", "P1"),
    Choice("Low", "P2"),
]

PROJECT_MENU_CHOICES = [
    Choice("View Projects", 1),
    Choice("Add Project", 2),
    Choice("Edit Project", 3),
    Choice("Delete Project", 4),
]