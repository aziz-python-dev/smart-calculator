from typing import List, Union
# Этот модуль хранит операции над числами.

def sum_up(numbers: List[Union[int, float]]) -> str:
    """Функция sum_up возвращает сумму чисел."""
    result = 0
    if len(numbers) == 2:
        result = numbers[0] + numbers[1]
        result = f'Сумма чисел {numbers[0]:,} и {numbers[1]:,} равна {result:,}.'
    elif len(numbers) > 2:
        for number in numbers:
            result += number
        result = f'Сумма чисел равна {result:,}.'        
    
    return result

def subtract(numbers: List[Union[int, float]]) -> str:
    """Функция subtract возвращает разность чисел."""
    if len(numbers) == 2:
        result = numbers[0] - numbers[1]
        result = f'Разность чисел {numbers[0]:,} и {numbers[1]:,} равна {result:,}.'
    elif len(numbers) > 2:
        result = numbers[0]
        for index in range(1, len(numbers)):
            result -= numbers[index]
        result = f'Разность чисел равна {result:,}.'
       
    return result
    
def multiply(numbers: List[Union[int, float]]) -> str:
    """Функция multiply возвращает произведение чисел."""
    result = 1
    if len(numbers) == 2:
        result = numbers[0] * numbers[1]
        result = f'Произведение чисел {numbers[0]:,} и {numbers[1]:,} равно {result:,}.'
    elif len(numbers) > 2:
        for number in numbers:
            result *= number
        result = f'Произведение чисел равно {result:,}.'
        
    return result

def divide(numbers: List[Union[int, float]]) -> str:
    """ Функция divide возвращает частное двух чисел."""
    try:
        result = numbers[0]/numbers[1]
        result = f'Частное чисел равно {numbers[0]:,} и {numbers[1]:,} равно {result:,.4f}'
    except ZeroDivisionError:
        result = 'На ноль делить нельзя!(You can\'t divide by zero!)'
        
    return result

def raise_power(numbers: List[Union[int, float]]) -> str:
    """Функция raise_power возвращает степень для двух чисел."""
    if len(numbers) == 2:
        result = pow(numbers[0], numbers[1])
        result = f'Число {numbers[0]:,} в степени {numbers[1]:,} равно {result:^10,.2f}.'
    
    return result