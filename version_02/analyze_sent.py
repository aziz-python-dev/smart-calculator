# Этот модуль содержит функцию check_sentence которая анализирует предложение.
# Определяет тип операции и выполняет ее.
from get_objects import *

   
def analyze_sentence(sentence):
    """Выполнить анализ предложение."""
    parts = [el.replace(',', '').lower() if ',' in el else el.lower() for el in sentence.split()]
    
    signs = [get_operators().get(el) for el in parts if el in get_operators()]
    
    signs = set(signs); signs = list(signs)
    if len(signs) != 1:
        signs = None
    
    parts = [el for el in parts if el not in get_operators()]
               
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