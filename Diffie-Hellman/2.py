from random import randint

def generate_prime_number():
    # Генерує випадкове просте число.
    while True:
        prime_candidate = randint(2**15, 2**16)
        if is_prime(prime_candidate):
            return prime_candidate

def is_prime(num):
    # Перевіряє, чи є число простим.
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primitive_root(prime):
    # Генерує первісний корінь за модулем простого числа.
    phi = prime - 1
    primitive_roots = []
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            primitive_roots.append(i)
    return primitive_roots[randint(0, len(primitive_roots) - 1)]

def gcd(a, b):
    # Обчислює найбільший спільний дільник (НСД) двох чисел.
    while b:
        a, b = b, a % b
    return a

def diffie_hellman():
    # Генерує просте число та первісний корінь
    prime = generate_prime_number()
    primitive_root = generate_primitive_root(prime)
    
    # Генерує приватні ключі для обох сторін
    private_key_A = randint(2, prime - 1)
    private_key_B = randint(2, prime - 1)
    
    # Обчислює публічні ключі
    public_key_A = pow(primitive_root, private_key_A, prime)
    public_key_B = pow(primitive_root, private_key_B, prime)
    
    # Обчислює спільні секретні ключі
    shared_secret_A = pow(public_key_B, private_key_A, prime)
    shared_secret_B = pow(public_key_A, private_key_B, prime)
    
    # Виводить обчислені спільні секретні ключі
    print("Спільний секретний ключ, обчислений стороною А:", shared_secret_A)
    print("Спільний секретний ключ, обчислений стороною Б:", shared_secret_B)

# Запускаємо протокол Діффі-Хеллмана
diffie_hellman()
