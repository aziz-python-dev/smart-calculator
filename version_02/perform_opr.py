# Этот модуль содержит функцию perfrom_operation которая
# выполняет операции над числами.
from operations import *

def perform_operation(signs, numbers):
    """Определить тип операции и получить результат."""
    
    try:
        if signs is None:
            print('Эта программа может выполнять только один тип операции за раз.')
        elif len(numbers) == 0:
            print('Не получилось определить числа. Пожалуста правильно введите числа.')
        elif len(numbers) == 1:
            print('Пожалуста введите минимум два числа для выполнения операции.')  
            
        elif '**' in signs:
            result = raise_power(numbers)
        elif '*' in signs:
            result = multiply(numbers)
        elif '/' in signs:
            result = divide(numbers)
        elif '+' in signs:
            result = sum_up(numbers)
        elif '-' in signs:
            result = subtract(numbers)
        print(result)        
        
    except UnboundLocalError:
        print('Правильно введите пример. Разделяйте слова, знаки и цифры пробелами.')
        
    except:
        print('Не удалось выполнить пример.')