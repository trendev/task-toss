"""
This module randomly assigns household tasks to children.
"""
import random

kids = ["Yann", "Lana", "Alice"]
tasks = [
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
]


def assign_tasks():
    """
    Assigns a random task from the tasks list to each kid in the kids list.

    Parameters:
    kids (list): A list of children's names.
    tasks (list): A list of household tasks.

    Returns:
    dict: A dictionary with kids as keys and their assigned tasks as values.
    """
    # Shuffle the tasks list to ensure random assignment
    global tasks
    random.shuffle(tasks)

    # Assign a task to each kid
    assigned_tasks = {}
    for i, k in enumerate(kids):
        assigned_tasks[k] = tasks[i]
        tasks = tasks[1:]  # task assigned, can be removed

    return assigned_tasks


def print_assigned_tasks(assignement):
    """
    Print the assigned tasks
    """
    for k, task in assignement.items():
        print(f"{k}: {task}")


# Assign tasks
task_assignment = assign_tasks()

print("\nAttribution initiale des tâches ménagères...")
print_assigned_tasks(task_assignment)

print("Faut-il changer la tâche d'un enfant? Si oui, saisir le nom de l'enfant")
kid = input("Choix:")

if kid in task_assignment:
    task_assignment[kid] = tasks[0]  # assign first task
    print_assigned_tasks(task_assignment)
