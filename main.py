"""
This module randomly assigns household tasks to children.
"""
import random


def assign_tasks(kids, tasks):
    """
    Assigns a random task from the tasks list to each kid in the kids list.

    Parameters:
    kids (list): A list of children's names.
    tasks (list): A list of household tasks.

    Returns:
    dict: A dictionary with kids as keys and their assigned tasks as values.
    """
    # Shuffle the tasks list to ensure random assignment
    random.shuffle(tasks)

    # Assign a task to each kid
    assigned_tasks = {kid: tasks[i] for i, kid in enumerate(kids)}

    return assigned_tasks


# Assign tasks
task_assignment = assign_tasks(
    ["Yann", "Lana", "Alice"],
    [
        "Ranger la chambre",
        "Faire la vaisselle",
        "Passer l'aspirateur dans la maison",
        "Balayer le sol de la cuisine",
        "Sortir les poubelles",
        "Essuyer la table après les repas",
        "Laver les vitres",
        "Aider à préparer le dîner",
        "Plier et ranger le linge",
        "Arroser les plantes",
        "Faire une machine",
        "Etendre le linge",
        "Nettoyer la cuisinière"
    ])

# Print the assigned tasks
for kid, task in task_assignment.items():
    print(f"{kid}: {task}")
