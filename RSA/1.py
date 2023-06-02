import random

def generate_key_pair(p, q):
    # Крок 1: Генерація двох великих простих чисел, p і q
    n = p * q
    phi = (p - 1) * (q - 1)

    # Крок 2: Вибір цілого числа e такого, що 1 < e < phi і gcd(e, phi) = 1
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)

    # Крок 3: Обчислення модулярного мультиплікативного оберненого e за модулем phi
    d = mod_inverse(e, phi)

    # Повернення публічного та приватного ключів
    return ((e, n), (d, n))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError('Модулярний обернений елемент не існує')
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    return g, y - (b // a) * x, x

def encrypt(public_key, message):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(private_key, encrypted_message):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)

# Приклад використання
p = 61
q = 53

public_key, private_key = generate_key_pair(p, q)

message = "Привіт, RSA!"
encrypted_message = encrypt(public_key, message)
decrypted_message = decrypt(private_key, encrypted_message)

print("Початкове повідомлення:", message)
print("Зашифроване повідомлення:", encrypted_message)
print("Розшифроване повідомлення:", decrypted_message)
