def fibonacci():
    choice = int(input('inserisci un numero: '))
    fib_sequence = []
    a, b = 0, 1
    while a <= choice:
        fib_sequence.append(a)
        a, b = b, a + b
        if a == choice:
            print(fib_sequence)
            print("Your number is included in fibonacci's sequence")
    return fib_sequence

print(fibonacci())