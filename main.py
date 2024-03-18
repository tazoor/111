
# Шифр простой замены (подстановочный шифр)
def simple_substitution_encrypt(text, key, alphabet):
    alphabet = alphabet.lower()
    result = ''
    for char in text:
        if char.isalpha() and char.lower() in alphabet:
            index = alphabet.index(char.lower())
            if char.islower():
                result += key[index].lower()
            else:
                result += key[index].upper()
        else:
            result += char
    return result


def simple_substitution_decrypt(cipher_text, key, alphabet):
    alphabet = alphabet.lower()
    result = ''
    for char in cipher_text:
        if char.isalpha() and char.lower() in key:
            index = key.index(char.lower())
            if char.islower():
                result += alphabet[index].lower()
            else:
                result += alphabet[index].upper()
        else:
            result += char
    return result


# Аффинный шифр
def affine_cipher_encrypt(text,a,b,alphabet):
    alphabet = alphabet.lower()
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                index = (a * (ord(char) - ord('a')) + b) % 26
                result += alphabet[index].lower()
            else:
                index = (a * (ord(char) - ord('A')) + b) % 26
                result += alphabet[index].upper()
        else:
            result += char
    return result


def affine_cipher_decrypt(cipher_text,a,b,alphabet):
    a = int(input('Введите значение первого ключа:'))
    b = int(input('Введите значение второго ключа:'))
    alphabet = alphabet.lower()
    result = ''
    a_inv = 0
    for i in range(len(alphabet)):
        if (a * i) % len(alphabet) == 1:
            a_inv = i
    for char in cipher_text:
        if char.isalpha():
            if char.islower():
                index = (a_inv * (ord(char) - ord('a') - b)) % len(alphabet)
                result += alphabet[index].lower()
            else:
                index = (a_inv * (ord(char) - ord('A') - b)) % len(alphabet)
                result += alphabet[index].upper()
        else:
            result += char
    return result


# Рекурсивный афинный шифр
def recurrent_affine_cipher_encrypt(text,a,b, alphabet):
    alphabet = alphabet.lower()
    result = text
    for i in range(5):  # Encrypt the text 5 times (can be adjusted)
        result = affine_cipher_encrypt(result, a, b, alphabet)
    return result
def recurrent_affine_cipher_decrypt(text,a,b, alphabet):
    alphabet = alphabet.lower()
    result = text
    for i in range(5):  # Encrypt the text 5 times (can be adjusted)
        result = affine_cipher_decrypt(result, a, b, alphabet)
    return result

print("Каким шифром вы хотите воспользоваться? ")

ans = (int(input("1 - Шифр простой замены, 2 - Аффинный шифр, 3 - Рекурсивный аффинный шифр \n")))
if ans == 1:
    ans1 =(int(input('Выберите, что хотите выполнить? \n 1 - шифровать, 2 - дешифровать \n')))
    if ans1 == 1:
        ans2 = (int(input('Выберите, с помощью какого алфавита будете шифровать \n 1 - русский, 2-английский \n ')))
        if ans2 == 1:
            ans2 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            ans3 = str(input('Введите ключ для шифрования:\n'))
            ans4 = str(input('Введите, что будете шифровать : \n'))
            print(simple_substitution_encrypt(ans4, ans3, ans2))
        if ans2 == 2:
            ans2 = 'abcdefghijklmnopqrstuvwxyz'
            ans3 = str(input('Введите ключ для шифрования:\n'))
            ans4 = str(input('Введите, что будете шифровать : \n'))
            print(simple_substitution_encrypt(ans4, ans3, ans2))
    elif ans1 == 2:
        ans2 = (int(input('Выберите, с помощью какого алфавита будете шифровать \n 1 - русский, 2-английский \n ')))
        if ans2 == 1:
            ans2 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            ans3 = str(input('Введите ключ для дешифрования:\n'))
            ans4 = str(input('Введите, что будете дешифровать : \n'))
            print(simple_substitution_decrypt(ans4, ans3, ans2))
        elif ans2 == 2:
            ans2 = 'abcdefghijklmnopqrstuvwxyz'
            ans3 = str(input('Введите ключ для дешифрования:\n'))
            ans4 = str(input('Введите, что будете дешифровать : \n'))
            print(simple_substitution_decrypt(ans4,ans3,ans2))
if ans == 2:
    ans1 =(int(input('Выберите, что хотите выполнить? \n 1 - шифровать, 2 - дешифровать \n')))
    if ans1 == 1:
        ans2 = (int(input('Выберите, с помощью какого алфавита будете шифровать \n 1 - русский, 2-английский \n ')))
        if ans2 == 1:
            ans2 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            a = int(input('Введите значение первого ключа:'))
            b = int(input('Введите значение второго ключа:'))
            ans4 = str(input('Введите, что будете шифровать : \n'))
            print(affine_cipher_encrypt(ans4,a,b ans2))
        if ans2 == 2:
            ans2 = 'abcdefghijklmnopqrstuvwxyz'
            a = int(input('Введите значение первого ключа:'))
            b = int(input('Введите значение второго ключа:'))
            ans4 = str(input('Введите, что будете шифровать : \n'))
            print(affine_cipher_encrypt(ans4,a,b ans2))
    elif ans1 == 2:
        ans2 = (int(input('Выберите, с помощью какого алфавита будете шифровать \n 1 - русский, 2-английский \n ')))
        if ans2 == 1:
            ans2 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            a = int(input('Введите значение первого ключа:'))
            b = int(input('Введите значение второго ключа:'))
            ans4 = str(input('Введите, что будете дешифровать : \n'))
            print(affine_cipher_decrypt(ans4,a,b,ans2))
        elif ans2 == 2:
            ans2 = 'abcdefghijklmnopqrstuvwxyz'
            a = int(input('Введите значение первого ключа:'))
            b = int(input('Введите значение второго ключа:'))
            ans4 = str(input('Введите, что будете дешифровать : \n'))
            print(affine_cipher_decrypt(ans4,a,b, ans2))
if ans == 3:
    ans1 =(int(input('Выберите, что хотите выполнить? \n 1 - шифровать, 2 - дешифровать \n')))
    if ans1 == 1:
        ans2 = (int(input('Выберите, с помощью какого алфавита будете шифровать \n 1 - русский, 2-английский \n ')))
        if ans2 == 1:
            ans2 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            a = int(input('Введите значение первого ключа:'))
            b = int(input('Введите значение второго ключа:'))
            ans4 = str(input('Введите, что будете шифровать : \n'))
            print(recurrent_affine_cipher_encrypt(ans4,a,b ans2))
        if ans2 == 2:
            ans2 = 'abcdefghijklmnopqrstuvwxyz'
            a = int(input('Введите значение первого ключа:'))
            b = int(input('Введите значение второго ключа:'))
            ans4 = str(input('Введите, что будете шифровать : \n'))
            print(recurrent_affine_cipher_encrypt(ans4,a,b ans2))
    elif ans1 == 2:
        ans2 = (int(input('Выберите, с помощью какого алфавита будете шифровать \n 1 - русский, 2-английский \n ')))
        if ans2 == 1:
            ans2 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            a = int(input('Введите значение первого ключа:'))
            b = int(input('Введите значение второго ключа:'))
            ans4 = str(input('Введите, что будете дешифровать : \n'))
            print(recurrent_affine_cipher_decrypt(ans4,a,b,ans2))
        elif ans2 == 2:
            ans2 = 'abcdefghijklmnopqrstuvwxyz'
            a = int(input('Введите значение первого ключа:'))
            b = int(input('Введите значение второго ключа:'))
            ans4 = str(input('Введите, что будете дешифровать : \n'))
            print(recurrent_affine_cipher_decrypt(ans4,a,b, ans2))