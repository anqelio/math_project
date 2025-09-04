import pytest
from app.geometry import rectangle_area

def test_area_3_and_5_positive():
    """
    Тест вычисления площади с целыми положительными длинами сторон
    """
    # Arrange
    width = '3'
    height = '5'
    expected_result = 15
    # Act
    actual_result = rectangle_area(width, height)
    # Assert
    assert actual_result == pytest.approx(expected_result)

def test_area_3_and_5_negative():
    """
    Тест вычисления площади с целыми отрицательными длинами сторон
    """
    # Arrange
    width = '-3'
    height = '5'
    expected_result = -15
    # Act
    actual_result = rectangle_area(width, height)
    # Assert
    assert actual_result == expected_result

def test_area_with_empty_string():
    """
    Тест вычисления площади с пустой строкой в качестве длины стороны
    """
    # Arrange
    width = ""
    height = "5"
    # Act
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    # Assert
    assert str(exc_info.value) == "Введено недопустимое значение"

def test_area_0():
    '''
    Тест вычисления площади, если длина равно нулю
    '''
    # Arrange
    width = '0'
    height = '5'
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
        # Assert
    assert str(exc_info.value) == "Введено недопустимое значение"

def test_area_float_int():
    '''
    Тест вычисления площади, если длина равна числу с плавающей точкой
    '''
    # Arrange
    width = '3.0'
    height = '5.0'
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
        # Assert
    assert str(exc_info.value) == "Введено недопустимое значение"

def test_area_float_int_with_comma():
    '''
    Тест вычисления площади, если длина равна числу с плавающей запятой
    '''
    # Arrange
    width = '3,0'
    height = '5,0'
    expected_result = 15
    # Act
    actual_result = rectangle_area(width, height)
    # Assert
    assert actual_result == expected_result

def test_area_text():
    '''
    Тест вычисления площади, если введены не те данные
    '''
    # Arrange
    width = 'lala'
    height = '5'
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
        # Assert
    assert str(exc_info.value) == "Введено недопустимое значение"