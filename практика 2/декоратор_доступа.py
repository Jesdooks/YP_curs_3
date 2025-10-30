def require_role(allowed_roles):
    def decorator(func):
        def proverka(user, *args, **kwargs):
            if user.get('role') in allowed_roles:
                return func(user, *args, **kwargs)
            else:
                print(f"Доступ запрещён пользователю {user['name']}")
        return proverka
    return decorator


@require_role(["admin", 'user'])
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")


user1 = {'name': 'Иван', 'role': 'admin'}
user2 = {'name': 'Петр', 'role': 'manager'}
user3 = {'name': 'Петр', 'role': 'user'}

delete_database(user1)
delete_database(user2)
delete_database(user3)
