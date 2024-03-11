#beecrowd exercise: 1012 - Area

valueA, valueB, valueC = map(float, input().split());
print(f'TRIANGULO: {valueA * valueC/2:.3f}');
print(f'CIRCULO: {(valueC**2) * 3.14159:.3f}');
print(f'TRAPEZIO: {((valueA + valueB) * valueC)/3:.3f}');
print(f'QUADRADO: {valueB ** 2:.3f}');
print(f'RETANGULO: {valueA * valueB:.3f}');