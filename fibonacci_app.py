"""
Código criado usando os
Gerador para calcular a série de Fibonacci.
A sequência de Fibonacci é uma série numérica em que cada número é a soma dos dois números
anteriores, começando por 0 e 1. A sequência começa assim: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
e assim por diante.

A função geradora é definida usando a palavra-chave yield, que torna a função especial,
permitindo que ela retorne um valor sem perder seu estado entre as chamadas.
"""


def fibonacci_generator():
    """Gerador para calcular a série de Fibonacci."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main():
    # Inicializa o gerador
    fibonacci_gen = fibonacci_generator()

    # Calcula os 50 primeiros números da série de Fibonacci
    for _ in range(50):
        fibonacci_number = next(fibonacci_gen)
        print(fibonacci_number, end=" ")


if __name__ == "__main__":
    main()
