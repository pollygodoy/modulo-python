# 3. Solicite ao usuário que digite uma temperatura em graus Celsius e converta-a para:
# A fórmula de conversão é: Fahremheit = Celsius * 9/5 + 32.

celsius = int(input("Digite a temperatura em Celsius para converter: "));
fahrenheit = (celsius * 9/5) + 32;

print("%s Celsius é igual Fahrenheit %s" % (celsius, int(fahrenheit)));
print();

""" RESULTADO (TERMINAL)

Digite a temperatura em Celsius para converter: 28
28 Celsius é igual Fahrenheit 82

"""