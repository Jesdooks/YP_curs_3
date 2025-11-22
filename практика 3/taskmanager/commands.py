"""
Модуль commands - команды для управления задачами.
"""

from taskmanager.models import Task
from taskmanager.storage import add_task, load_tasks, delete_task, update_task_status
from datetime import datetime
import uuid  # генерации уникальных идентификаторов

# Словари для перевода на русский язык
STATUS_TRANSLATIONS = {
    'pending': 'в ожидании',
    'done': 'выполнена'
}

PRIORITY_TRANSLATIONS = {
    'low': 'низкий',
    'normal': 'обычный',
    'high': 'высокий'
}

# Обратные словари для конвертации русских значений в английские
PRIORITY_FROM_RU = {
    'низкий': 'low',
    'обычный': 'normal',
    'высокий': 'high'
}

STATUS_FROM_RU = {
    'в ожидании': 'pending',
    'выполнена': 'done'
}


def add_command(args):
    """
    Создание новой задачи и сохранение её

    Args:
        args: передаваемые параметры объекту класса Task
    """
    # Преобразуем строку даты в datetime, если она указана
    due_date = None
    if args.due_date:
        try:
            # Ожидаем формат YYYY-MM-DD
            due_date = datetime.strptime(args.due_date, '%Y-%m-%d')
        except ValueError:
            print("Неверный формат даты. Используйте формат YYYY-MM-DD, например 2025-11-20.")
            return

    # Конвертируем русский приоритет в английский для хранения
    priority = args.priority or 'обычный'
    priority = PRIORITY_FROM_RU.get(priority, 'normal')

    task = Task(
        id=str(uuid.uuid4()),  # Генерация уникального ID в виде строки
        title=args.title,
        priority=priority,
        due_date=due_date  # Дата выполнения как datetime или None
    )
    add_task(task, args.file_path)
    print(f"Задача '{task.title}' добавлена.")


def list_command(args):
    """
    Вывод списка задач с возможностью фильрации

    Args:
        args: передаваемые параметры объекту класса Task
    """
    tasks = load_tasks(args.file_path) # загрузка задач из файла

    # Фильтрация по статусу, приоритету, дате и пр.
    if args.status:
        # Конвертируем русский статус в английский для сравнения
        status = STATUS_FROM_RU.get(args.status, args.status)
        tasks = [t for t in tasks if t.status == status]
    if args.priority:
        # Конвертируем русский приоритет в английский для сравнения
        priority = PRIORITY_FROM_RU.get(args.priority, args.priority)
        tasks = [t for t in tasks if t.priority == priority]
    for t in tasks:
        status_ru = STATUS_TRANSLATIONS.get(t.status, t.status)
        priority_ru = PRIORITY_TRANSLATIONS.get(t.priority, t.priority)
        print(f"{t.id}: {t.title} [{status_ru}] (приоритет: {priority_ru})")


def done_command(args):
    """
    Обновление статуса конкретной задачи на "выполнена"

    Args:
        args: передаваемые параметры объекту класса Task
    """
    if update_task_status(args.task_id, 'done', args.file_path):
        print(f"Задача {args.task_id} помечена как выполненная.")
    else:
        print(f"Задача {args.task_id} не найдена.")


def delete_command(args):
    """
    Удаление задачи по ID

    Args:
        args: передаваемые параметры объекту класса Task
    """
    if delete_task(args.task_id, args.file_path):
        print(f"Задача {args.task_id} удалена.")
    else:
        print(f"Задача {args.task_id} не найдена.")



