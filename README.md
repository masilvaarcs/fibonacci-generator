## Fibonacci Generator

Este é um exemplo simples de um gerador Python para calcular a série de Fibonacci. A sequência de Fibonacci é uma série numérica em que cada número é a soma dos dois números anteriores, começando por 0 e 1.

### Como usar

1. Certifique-se de ter o Python 3.x instalado em seu sistema. Caso ainda não tenha, você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. Clone este repositório:

   ```bash
   git clone https://github.com/masilvaarcs/fibonacci_generator.git
   ```

3. Navegue até o diretório "fibonacci_generator":

   ```bash
   cd fibonacci_generator
   ```

4. Execute o arquivo "fibonacci_generator.py" para utilizar o gerador:

   ```bash
   python fibonacci_generator.py
   ```

5. O programa irá gerar a sequência de Fibonacci infinita, exibindo os números sequencialmente até que você interrompa a execução pressionando "Ctrl + C" no terminal.

### Como funciona o gerador

A função geradora `fibonacci_generator` é definida usando a palavra-chave `yield`, permitindo que ela retorne valores sem perder seu estado entre as chamadas. Cada vez que a função é chamada usando o gerador, ela calcula e retorna o próximo número da sequência de Fibonacci.

O arquivo "fibonacci_generator.py" contém a implementação do gerador. Você pode modificar o arquivo para ajustar o comportamento ou limitar a quantidade de números gerados, se necessário.

### Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

---

Criado por Seu Nome.
