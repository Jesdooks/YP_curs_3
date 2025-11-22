import argparse
from taskmanager import commands

def parse_args():
    """
    Парсит аргументы командной строки для консольного менеджера задач.

    Возвращает объект с распарсенными аргументами.

    Команды:
    - add: добавить задачу с параметрами title, priority, due_date
    - list: вывести список задач с фильтрами по статусу и приоритету
    - done: отметить задачу как выполненную по ID
    - delete: удалить задачу по ID

    Args:
        None

    Returns:
        argparse.Namespace: объект с аргументами командной строки и выбранной командой
    """

    #объект парсера с описанием программы для пользователя
    parser = argparse.ArgumentParser(description='Консольный менеджер задач')
    parser.add_argument('--file_path', default='tasks.json', help='Путь к файлу с задачами')

    #создание подкоманд add, list, done, delete
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('--title', required=True, help='Название задачи')
    add_parser.add_argument('--priority', choices=['низкий', 'обычный', 'высокий'], help='Приоритет задачи')
    add_parser.add_argument('--due_date', help='Срок выполнения задачи в формате YYYY-MM-DD')

    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('--status', choices=['в ожидании', 'выполнена'], help='Фильтр по статусу')
    list_parser.add_argument('--priority', choices=['низкий', 'обычный', 'высокий'], help='Фильтр по приоритету')

    done_parser = subparsers.add_parser('done')
    done_parser.add_argument('task_id', help='ID задачи для пометки как выполненной')

    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('task_id', help='ID задачи для удаления')

    return parser.parse_args()

def main():
    args = parse_args()
    try:
        if args.command == 'add':
            commands.add_command(args)
        elif args.command == 'list':
            commands.list_command(args)
        elif args.command == 'done':
            commands.done_command(args)
        elif args.command == 'delete':
            commands.delete_command(args)
        else:
            print("Неизвестная команда. Используйте --help для справки.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
