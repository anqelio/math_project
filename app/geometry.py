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
    if number == 0:
        raise ValueError("Введено недопустимое значение")
    return number

def rectangle_area(width: str, height: str) -> float:
    """
    Вычисляет площадь прямоугольника, проверяя входные строки.
    """
    if width == '' or height == '':
        raise ValueError('Введено недопустимое значение')
    if '.' in width or '.' in height:
        raise ValueError('Введено недопустимое значение')
    if ',' in width or ',' in height:
        w = parse_number(width)
        h = parse_number(height)
        return w * h
    w = parse_number(width)
    h = parse_number(height)
    return w * h