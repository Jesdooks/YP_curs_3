from datetime import datetime


class Task:
    def __init__(self, id, title, status='pending', priority='normal', created_at=None, due_date=None):
        self.id = id
        self.title = title
        self.status = status
        self.priority = priority
        self.created_at = created_at or datetime.now()
        self.due_date = due_date

    def to_dict(self):
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

