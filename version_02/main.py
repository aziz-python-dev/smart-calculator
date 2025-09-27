from analyze_sent import analyze_sentence; from perform_opr import perform_operation

def main(): 
    show_info(); string = 'да' 
    
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
        print('-' * 70)

def show_info():
    """ Эта функцию выводит ознакомительную информацию для пользователя."""
       
    print('-' * 70)
    print('Эта программа выполняет простые арифметические операции.')
    print('Такие как сумма нескольких чисел, разность несколько чисел,')
    print('умножение нескольких чисел, деление двух чисел, возведение в степень числа.')
    print('Эта программа может выполнять только один тип операции за раз.')
    print('Пожалуйста вводите слова, знаки и цифры разделяя их пробелами.')
    print('Это необходимо для нормального функцианирования.\n')
         
if __name__ == '__main__':
    main()