#beecrowd exercise: 1013 - The Greatest

valueA, valueB, valueC = map(int, input().split());

maiorAB = int((valueA + valueB + abs(valueA - valueB)) / 2);
maiorABC = int((maiorAB + valueC + abs(maiorAB - valueC)) /2);

print(maiorABC, "eh o maior");
