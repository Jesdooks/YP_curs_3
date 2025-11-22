"""
Модуль models - определяет модели данных для задач.
"""

from datetime import datetime


class Task:
    """
    Класс Task используется для представления задачи с атрибутами и методами для управления статусом, приоритетом и сроками

    Атрибуты:
         id (any): уникальный идентификатор задачи
         title (str): заголовок или краткое описание задачи
         status (str): статус задачи (по умолчанию 'pending' - в ожидании)
         priority (str): приоритет задачи (по умолчанию 'normal')
         created_at (datetime): дата и время создания задачи (если не указано, устанавливается текущая дата и время)
         due_date (datetime or None): крайний срок выполнения задачи (если есть)

    Методы:
         to_dict() -> dict:
             Преобразует объект задачи в словарь с серийными значениями (для сохранения или передачи)
             Даты преобразуются в ISO формат строк

         from_dict(data: dict) -> Task:
             Статический метод, создающий объект Task из словаря
             Преобразует строки с датами из ISO формата в datetime объекты
             Args:
                 data (dict): словарь со свойствами задачи, возможно, загруженный из JSON/CSV
             Returns:
                 Task: экземпляр задачи с заполненными атрибутами
             Значения по умолчанию:
                 status: 'pending'
                 priority: 'normal'
    """
    def __init__(self, id, title, status='pending', priority='normal', created_at=None, due_date=None):
        self.id = id
        self.title = title
        self.status = status
        self.priority = priority
        self.created_at = created_at or datetime.now()
        self.due_date = due_date

    def to_dict(self):
        """
        Преобразует объект Task в словарь для сериализации

        Returns:
            dict: словарь с данными задачи, пригодный для JSON или другого формата
        """
        return {
            'id': self.id,
            'title': self.title,
            'status': self.status,
            'priority': self.priority,
            'created_at': self.created_at.isoformat(),
            'due_date': self.due_date.isoformat() if self.due_date else None,
        }

    @staticmethod
    def from_dict(data):
        """
        Создает объект Task из словаря

        Args:
            data (dict): словарь с ключами и значениями атрибутов задачи,
                где даты представлены в ISO формате строк.

        Returns:
            Task: новый объект Task с заполненными атрибутами
        """
        created_at = datetime.fromisoformat(data['created_at']) if data.get('created_at') else None
        due_date = datetime.fromisoformat(data['due_date']) if data.get('due_date') else None
        return Task(
            id=data['id'],
            title=data['title'],
            status=data.get('status', 'pending'), #pending знач по умолчанию
            priority=data.get('priority', 'normal'), #normal знач по умолчанию
            created_at=created_at,
            due_date=due_date,
        )

