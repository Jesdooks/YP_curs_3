from taskmanager.models import Task
from taskmanager.storage import add_task, load_tasks, delete_task, update_task_status
import uuid #генерации уникальных идентификаторов


def add_command(args):
    """
    Создание новой задачи и сохранение её

    Args:
        args: передаваемые параметры объекту класса Task
    """
    task = Task(
        id=str(uuid.uuid4()), # Генерация уникального ID в виде строки
        title=args.title,
        priority=args.priority or 'normal',
        due_date=args.due_date # Дата выполнения из аргументов
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
        tasks = [t for t in tasks if t.status == args.status]
    if args.priority:
        tasks = [t for t in tasks if t.priority == args.priority]
    for t in tasks:
        print(f"{t.id}: {t.title} [{t.status}] (priority: {t.priority})")


def done_command(args):
    """
    Обновление статуса конкретной задачи на "выполнена"

    Args:
        args: передаваемые параметры объекту класса Task
    """
    if update_task_status(args.task_id, 'done', args.filepath):
        print(f"Задача {args.task_id} помечена как выполненная.")
    else:
        print(f"Задача {args.task_id} не найдена.")


def delete_command(args):
    """
    Удаление задачи по ID

    Args:
        args: передаваемые параметры объекту класса Task
    """
    if delete_task(args.task_id, args.filepath):
        print(f"Задача {args.task_id} удалена.")
    else:
        print(f"Задача {args.task_id} не найдена.")



