import random

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_characters = '!@#$%^&*()'

all_characters = lowercase + uppercase + numbers + special_characters

password_length = int(input('Введите длину пароля: '))

password = ''.join(random.choices(all_characters, k=password_length))

print('Ваш пароль:', password)