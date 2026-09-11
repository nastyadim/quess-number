import random

number = random.randint(1, 100)
tries = 0
print("Я загадал число от 1 до 100. Угадай!")

while True:
    guess = int(input("Твой вариант: "))
    tries += 1
    if guess < number:
        print("Больше!")
    elif guess > number:
        print("Меньше!")
    else:
        print(f"Угадал! Попыток: {tries}")
        break
