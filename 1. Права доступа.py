from typing import Callable
import functools


def check_permission_with_variables(permission: str):
    def check_permission(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if permission not in user_permissions:
                    raise PermissionError
                return func(*args, **kwargs)
            except PermissionError as exc:
                print(f"PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")

        return wrapper
    return check_permission


user_permissions = ['admin']


@check_permission_with_variables('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission_with_variables('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
