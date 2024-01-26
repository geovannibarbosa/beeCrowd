#beecrowd exercise: 1010 - Simple Calculate

valueA, valueB, valueC = map(float, input().split());
valueD, valueE, valueF = map(float, input().split());
toPay = (valueB * valueC) + (valueE * valueF);
print(f'VALOR A PAGAR: R$ {toPay:.2f}');