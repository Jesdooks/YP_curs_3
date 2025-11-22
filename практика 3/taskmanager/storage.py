"""
Модуль storage - управление хранением задач в JSON файле.
"""

import json
from typing import List
from taskmanager.models import Task

def load_tasks(file_path: str):
    """
    Загрузка списка задач из файла JSON или CSV

    Args:
        file_path (str): строка с путем к файлу

    Returns:
        List[Task]: список объектов Task
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            return [Task.from_dict(x) for x in data]
    except (FileNotFoundError, json.JSONDecodeError) as e: #в () перечисл типы исключ
        # Если файла ещё нет или в нём пусто/мусор, просто считаем, что задач пока нет
        return []

def save_tasks(tasks: List[Task], file_path: str):
    """
    Сохранение списка задач в файл

    Args:
        tasks (list): список объектов Task
        file_path: путь к файлу, куда нужно сохранить список задачь (tasks)

    Returns:
        json файл: список словарей (каждая задача - словарь)
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4) #Преобразую каждую задачу в словарь to_dict(), indent-отступ для чтения
    except IOError as e:
        print(f"Ошибка сохранения файла: {e}")

def add_task(task: Task, file_path: str):
    """
    Добавление новой задачи task в файл по пути filepath

    Args:
        tasks (list): список объектов Task
        file_path: путь к файлу, куда нужно сохранить новую задачу

    Returns:
        json файл: список словарей (каждая задача - словарь)
    """
    tasks = load_tasks(file_path)  # функции выше
    tasks.append(task)
    save_tasks(tasks, file_path)


def delete_task(task_id, file_path: str):
    """
    Удаление задачи по её id из файла

    Args:
        task_id: id задача, котрую нужно удалить
        file_path: путь к файлу с задачами

    Returns:
        bool: True, если задача была найдена и удалена, иначе False
    """
    tasks = load_tasks(file_path)
    new_tasks = [t for t in tasks if t.id != task_id] #обращение к атрибуту .id объекта класса Task
    if len(new_tasks) == len(tasks):
        return False
    save_tasks(new_tasks, file_path)
    return True

def update_task_status(task_id, status, file_path: str):
    """
    Обновляет статус задачи с заданным id

    Args:
        task_id: id задача, котрую нужно обновить
        status: хранит статус выполнения, по умолчанию pending
        file_path: путь к файлу с задачами

    Returns:
        bool: True, если обновление прошло, иначе False
    """
    tasks = load_tasks(file_path)
    updated = False
    for task in tasks:
        if task.id == task_id:
            task.status = status
            updated = True
            break
    if updated:
        save_tasks(tasks, file_path)
    return updated



