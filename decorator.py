# def null_decorator(func):
#     print(func())
#     return func


# def uper_case(func):
#     def wrapper():
#         original_result = func()
#         print(id(original_result))
#         modified_result = original_result.upper() + " World"
#         print(id(modified_result))
#         return modified_result
#     return wrapper

# def greet():
#     return " hello!"
# print(greet)
# print(null_decorator(greet))

# @null_decorator
# @uper_case
# def greet():
#     return " hello!"


# greet = null_decorator(greet)

# print(greet())

# ОЧЕНЬ ИНТЕРЕСНАЯ ШТУКА НУЖНО ЗАПОНИТЬ
def trace(func):
    def wrapper(*ferst, **second):
        print(f'TRACE: calling {func.__name__}() '
              f'with {ferst}, {second}')

        original_result = func(*ferst, **second)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result}')

        return original_result
    return wrapper

@trace
def pox(name, line):
    return f'{name}: {line}'


print(pox('Jane', 'Hello, World'))