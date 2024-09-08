# 1. Verificação de um número na sequência de Fibonacci
def is_fibonacci(num):
    if num < 0:
        return False
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

# Teste com um número
numero = int(input("Informe um número: "))
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

# 2. Contagem da letra 'a' em uma string
def contar_letra_a(s):
    count = s.lower().count('a')
    return count

# Teste com uma string
string = input("Informe uma string: ")
quantidade = contar_letra_a(string)
print(f"A letra 'a' aparece {quantidade} vezes na string.")

# 3. Cálculo da variável SOMA
# Código em C para calcular a soma
'''
#include <stdio.h>

int main() {
    int INDICE = 12, SOMA = 0, K = 1;
    while (K < INDICE) {
        K = K + 1;
        SOMA = SOMA + K;
    }
    printf("%d\n", SOMA);
    return 0;
}
'''

# 4. Complete a sequência
# a) 1, 3, 5, 7, ___
def proximo_elemento_a():
    return 9

# b) 2, 4, 8, 16, 32, 64, ____
def proximo_elemento_b():
    return 128

# c) 0, 1, 4, 9, 16, 25, 36, ____
def proximo_elemento_c():
    return 49

# d) 4, 16, 36, 64, ____
def proximo_elemento_d():
    return 100

# e) 1, 1, 2, 3, 5, 8, ____
def proximo_elemento_e():
    return 13

# f) 2, 10, 12, 16, 17, 18, 19, ____
def proximo_elemento_f():
    return 20

# Teste os resultados
print("a:", proximo_elemento_a())
print("b:", proximo_elemento_b())
print("c:", proximo_elemento_c())
print("d:", proximo_elemento_d())
print("e:", proximo_elemento_e())
print("f:", proximo_elemento_f())
