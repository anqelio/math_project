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

def test_area_3_and_5_negatie():
    """
    Тест вычисления площади с целыми отрицательными длинами сторон
    """
    # Arrange
    width = '-3'
    height = '5'
    expected_result = 15
    # Act
    actual_result = rectangle_area(width, height)
    # Assert
    assert actual_result == pytest.approx(expected_result)

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