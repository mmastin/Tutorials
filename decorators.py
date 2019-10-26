# _functions = {}
# def register(f):
#     global _functions
#     _functions[f.__name__] = f
#     return f

# @register
# def foo():
#     return 'bar'

# foo()

class Store(object):
    def get_food(self, username, food):
        if username != 'admin':
            raise Exception('this user not allowed to get food')
        return self.storage.get(food)

    def put_food(self, username, food):
        if username != 'admin':
            raise Exception('this user not allowed to put food')
        self.storage.put(food)


def check_is_admin(username):
    if username != 'admin':
        raise Exception('this user is not allowed to get or put food')

class Store2(object):
    def get_food(self, username, food):
        check_is_admin(username)
        return self.storage.get(food)

    def put_food(self, username, food):
        check_is_admin(username)
        self.storage.put(food)


def check_is_admin2(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception('this user not allowed to get or put food')
        return f(*args, **kwargs)
        return wrapper

class Store3(object):
    @check_is_admin2
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_is_admin2
    def put_food(self, username, food):
        self.storage.put(food)


def check_user_is_not(username):
    def user_check_decorator(f):
        def wrapper(*args, **kwargs):
            if kwargs.get('username') == usernmae:
                raise Exception('this user not allowed to get food')
            return f(*args, **kwargs)
        return wrapper
    return user_check_decorator

class Store4(object):
    @check_user_is_not('admin')
    @check_user_is_not('user123')
    def get_food(self, username, food):
        return self.storage.get(food)


# Class decorators - less common
import uuid

def set_clase_name_and_id(klass):
    klass.name = str(klass)
    klass.random_id = uuid.uuid4()
    return klass

@set_clase_name_and_id
class SomeClass(object):
    pass 

# another example
class CountCalls(object):
    def __init__(self, f):
        self.f = f
        self.called = 0

    def __call__(self, *args, **kwargs):
        self.called += 1
        return self.f(*args, **kwargs)

@CountCalls
def print_hello():
    print('hello')


# a decorator for decorators
import functools
def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception('this user is not allowed to get food')
        return f(*args, **kwargs)
    return wrapper

class Store(object):
    @check_is_admin
    def get_food(self, username, food):
        """Get food from storage."""
        return self.storage.get(food)