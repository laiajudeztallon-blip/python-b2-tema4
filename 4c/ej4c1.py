"""
Enunciado:
Desarrolla un test para la función implementada calculate_rectangle_area, la función recibe dos parámetros ancho y
alto, y devuelve el área del rectángulo, calculada como ancho * alto. utilizando el enfoque de Desarrollo Guiado
por Pruebas (TDD).

Se debe realizar los test en el archivo ej4c1_test.py considerando los distintos casos de prueba especificados en el
test.
"""

import pytest
from ej4c1 import calculate_rectangle_area

def test_calculate_rectangle_area():    
    width = 3
    height = 7
    expected_area = 21
    assert calculate_rectangle_area(width, height) == expected_area
    
def test_value_error_calculate_rectangle_area():
    width = -2
    height = 8
    
    with pytest.raises(ValueError):
        calculate_rectangle_area(width, height)
    

def test_type_error_calculate_rectangle_area():
    width = 'a'
    height = 5
    with pytest.raises(TypeError):
        calculate_rectangle_area(width, height)

    

# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     print(calculate_rectangle_area(5, 10))
