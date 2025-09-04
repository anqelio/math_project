def parse_number(value: str) -> float:
    '''
    Преобразует строку в положительное число с плавающей точкой,
    проверяет корректность и положительность значения.
    '''

    s = value.strip().replace(',', '.')
    if not s:
        raise ValueError("Введено недопустимое значение")
    try:
        number = float(s)
    except ValueError:
        raise ValueError("Введено недопустимое значение")
    return number

def rectangle_area(width: str, height: str) -> float:
    """
    Вычисляет площадь прямоугольника, проверяя входные строки.
    """
    if w == '' or h == '':
        raise ValueError('Введена пустая строка')
    w = parse_number(width)
    h = parse_number(height)
    return w * h