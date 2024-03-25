def fibonacci_sequence(n):
    fibonacci = [0, 1]
    
    while fibonacci[-1] < n:
        next_fib = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_fib)
    
    return fibonacci

def pertence_sequencia(numero, sequencia):
    if numero in sequencia:
        return True
    else:
        return False

numero = int(input("Digite um número: "))

sequencia_fibonacci = fibonacci_sequence(numero)

if pertence_sequencia(numero, sequencia_fibonacci):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")