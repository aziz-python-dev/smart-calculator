
def main():  
    show_info()

    string = 'да'
    
    while string.lower() == 'да':
        sentence = input('Дайте мне какой нибудь пример: ')
        
        if sentence == 'нет' or sentence == 'no':
            break
        elif sentence == 'да' or sentence == 'yes':
            continue        
        
        signs, numbers = analyze_sentence(sentence)
        
        perform_operation(signs, numbers)       
        
        string = input('\nХотите продолжить? (да/нет) ')
    else:
        print('До следующий встречи.')
        print('-------------------------------------------------------------')


def show_info():
    print('-------------------------------------------------------------')
    print('Эта программа выполняет простые арифметические операции.')
    print('Такие как сумма нескольких чисел, разность несколько чисел,')
    print('умножение нескольких чисел, деление двух чисел, возведение в степень числа.')
    print('Эта программа может выполнять только один тип операции за раз.')
    print('Пожалуйста вводите слова, знаки и цифры разделяя их пробелами.')
    print('Это необходимо для нормального функцианирования.\n')
          
def analyze_sentence(sentence): 
    """Выполнить анализ предложение."""
    parts = [el.lower() for el in sentence.split()]
    
    signs = [get_signs().get(el) for el in parts if el in get_signs()]
    
    signs = set(signs); signs = list(signs)
    if len(signs) != 1:
        signs = None
    
    parts = [el for el in parts if el not in get_signs()]
    
    numbers = []         
    for part in parts:
        for tuple in get_numbers().keys():
            if part in tuple:
                numbers.append(get_numbers().get(tuple))
                break
            
        if part.isdigit():
            part = int(part)
            numbers.append(part)
    
    return signs, numbers
    
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
            result = sum(numbers)
        elif '-' in signs:
            result = subtract(numbers)
        print(result)        
        
    except UnboundLocalError:
        print('Правильно введите пример. Разделяйте слова, знаки и цифры пробелами.')
        
    except:
        print('Не удалось выполнить пример.')  


def get_signs():
    """Функция get_signs возвращает словарь(слово:знак)."""
    
    signs = {'плюс': '+', 'сложи': '+', 'суммируй': '+', 'сумму': '+', 'сумма': '+', 'sum': '+', 'plus': '+', 'add-up': '+', '+': '+',
        'минус': '-', 'разность': '-', 'вычти': '-', 'difference': '-', 'subtract': '-', '-': '-',
        'умножить': '*', 'умнож': '*', 'произведение': '*', 'произведения': '*', 'умножим': '*', 'multiply': '*', 'product-of-numbers': '*', '*': '*',  
        'разделить': '/', 'раздели': '/', 'делить': '/', 'частное': '/', 'разделим': '/', 'divide': '/', '/': '/',
        'степень': '**', 'степени': '**', 'degree': '**',  '**': '**', 
    }
    return signs


def get_numbers():
    """Функция get_numbers возвращает словарь(слово:число)."""
    
    numbers = {
    ('ноль', 'zero',): 0, ('один', 'one',): 1, ('два', 'two',): 2, ('три', 'three',): 3, ('четыре', 'four',): 4, ('пять', 'five',): 5, ('шесть', 'six',): 6, ('семь', 'seven',): 7, ('восемь', 'eight',): 8,
    ('девять', 'nine',): 9, ('десять', 'ten',): 10, ('одиннадцать', 'eleven',): 11, ('двенадцать', 'twelve',): 12, ('тринадцать', 'thirteen',): 13, ('четырнадцать', 'fourteen',): 14,
    ('пятнадцать', 'fifteen',): 15, ('шестнадцать', 'sixteen',): 16, ('семнадцать', 'seventeen',): 17, ('восемнадцать', 'eighteen',): 18, ('девятнадцать', 'nineteen',): 19, ('двадцать', 'twenty',): 20,
    ('двадцать-один', 'twenty-one',): 21, ('двадцать-два', 'twenty-two',): 22, ('двадцать-три', 'twenty-three',): 23, ('двадцать-четыре', 'twentee-four',): 24, ('двадцать-пять', 'twentee-five',): 25,
    ('двадцать-шесть', 'twenty-six',): 26, ('двадцать-семь', 'twenty-seven',): 27, ('двадцать-восемь', 'twenty-eight',): 28, ('двадцать-девять', 'twenty-nine',): 29, ('тридцать', 'thirty',): 30, ('тридцать-один', 'thirty-one',): 31,
    ('тридцать-два', 'thirty-two',): 32, ('тридцать-три', 'thirty-three',): 33, ('тридцать-четыре', 'thirty-four',): 34, ('тридцать-пять', 'thirty-five', ): 35, ('тридцать-шесть', 'thirty-six',): 36,
    ('тридцать-семь', 'thirty-seven',): 37, ('тридцать-восемь', 'thirty-eight',): 38, ('тридцать-девять', 'thirty-nine',): 39, ('сорок', 'fourty',): 40, ('сорок-один', 'forty-one',): 41, ('сорок-два', 'forty-two',): 42,
    ('сорок-три', 'forty-three',): 43, ('сорок-четыре', 'forty-four',): 44, ('сорок-пять', 'forty-five',): 45, ('сорок-шесть', 'forty-six',): 46, ('сорок-семь', 'forty-seven',): 47, ('сорок-восемь', 'forty-eight',): 48,
    ('сорок-девять', 'forty-nine',): 49, ('пятьдесят', 'fifty',): 50, ('пятьдесят-один', 'fifty-one',): 51, ('пятьдесят-два', 'fifty-two',): 52, ('пятьдесят-три', 'fifty-three',): 53, ('пятьдесят-четыре', 'fifty-four',): 54,
    ('пятьдесят-пять', 'fifty-five',): 55, ('пятьдесят-шесть', 'fifty-six', '56'): 56, ('пятьдесят-семь', 'fifty-seven',): 57, ('пятьдесят-восемь', 'fifty-eight',): 58, ('пятьдесят-девять', 'fifty-nine',): 59,
    ('шестьдесят', 'sixty',): 60, ('шестьдесят-один', 'sixty-one',): 61, ('шестьдесят-два', 'sixty-two',): 62, ('шестьдесят-три', 'sixty-three',): 63, ('шестьдесят-четыре', 'sixty-four',): 64, ('шестьдесят-пять', 'sixty-five',): 65,
    ('шестьдесят-шесть', 'sixty-six',): 66, ('шестьдесят-семь', 'sixty',): 67, ('шестьдесят-восемь', 'sixty-eight',): 68, ('шестьдесят-девять', 'sixty-nine',): 69, ('семьдесят', 'seventy',): 70,
    ('семьдесят-один', 'seventy-one', ): 71, ('семьдесят-два', 'seventy-two',): 72, ('семьдесят-три', 'seventy-three',): 73, ('семьдесят-четыре', 'seventy-four',): 74, ('семьдесят-пять', 'seventy-five',): 75,
    ('семьдесят-шесть', 'seventy-six', ): 76, ('семьдесят-семь', 'seventy-seven',): 77, ('семьдесят-восемь', 'seventy-eight',): 78, ('семьдесят-девять', 'seventy-nine',): 79, ('восемьдесят', 'eighty',): 80,
    ('восемьдесят-один', 'eighty-one',): 81, ('восемьдесят-два', 'eighty-two',): 82, ('восемьдесят-три', 'eighty-three',): 83, ('восемьдесят-четыре', 'eighty-four',): 84, ('восемьдесят-пять', 'eighty-five',): 85,
    ('восемьдесят-шесть', 'eighty-six',): 86, ('восемьдесят-семь', 'eighty-seven',): 87, ('восемьдесят-восемь', 'eighty-eight',): 88, ('восемьдесят-девять', 'eighty-nine',): 89, ('девяносто', 'ninety',): 90,
    ('девяносто-один', 'ninety-one', ): 91, ('девяносто-два', 'ninety-two',): 92, ('девяносто-три', 'ninety-three',): 93, ('девяносто-четыре', 'ninety-four',): 94, ('девяносто-пять', 'ninety-five',): 95, ('девяносто-шесть', 'ninety-six',): 96,
    ('девяносто-семь', 'ninety-seven', ): 97, ('девяносто-восемь', 'ninety-eight',): 98, ('девяносто-девять', 'ninety-nine',): 99, ('сто', 'one-hundred',): 100,
    }
    
    return numbers

def sum(numbers):
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

def subtract(numbers):
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
    
def multiply(numbers):
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

def divide(numbers):
    """ Функция divide возвращает частное двух чисел."""
    try:
        result = numbers[0]/numbers[1]
        result = f'Частное чисел равно {numbers[0]:,} и {numbers[1]:,} равно {result:,.4f}'
    except ZeroDivisionError:
        result = 'На ноль делить нельзя!(You can\'t divide by zero!)'
        
    return result

def raise_power(numbers):
    """Функция raise_power возвращает степень для двух чисел."""
    if len(numbers) == 2:
        result = pow(numbers[0], numbers[1])
        result = f'Число {numbers[0]:,} в степени {numbers[1]:,} равно {result:^10,.2f}.'
    
    return result

if __name__ == '__main__':
    main()
