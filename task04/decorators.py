from functools import wraps

def input_error(func):
    # Перезаписуємо метадані оригінальної функції
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No such name in contacts."
        except ValueError:
            return "Enter the argument for the command"
        except IndexError:
            return "Enter user name."
        except Exception as e:
            return f"{e}"
    return inner
